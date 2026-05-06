"""Валидатор базы знаний MedAssist."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import (
    ALLOWED_DIAGNOSTIC_CATEGORIES,
    ALLOWED_PROTOCOL_CATEGORIES,
    ALLOWED_PHARM_CATEGORIES,
    ALLOWED_DOMAINS,
    ALLOWED_RELATION_TYPES,
    ALLOWED_STATUS,
    ALLOWED_URGENCY,
    FOLDER_CATEGORY_RULES,
    REQUIRED_FIELDS,
)
from .models import KnowledgeCard
from .repository import KnowledgeRepository

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    code: str
    file_path: str
    card_id: str
    message: str


@dataclass
class ValidationReport:
    total_cards: int
    issues: list[ValidationIssue] = field(default_factory=list)
    parse_errors: list[str] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "ERROR"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "WARNING"]

    @property
    def is_valid(self) -> bool:
        return not self.parse_errors and not self.errors

    def to_markdown(self) -> str:
        lines = [
            "# Отчёт проверки базы знаний MedAssist",
            "",
            f"Проверено карточек: **{self.total_cards}**.",
            f"Ошибок парсинга: **{len(self.parse_errors)}**.",
            f"Структурных ошибок: **{len(self.errors)}**.",
            f"Предупреждений: **{len(self.warnings)}**.",
            f"Итог: **{'проверка пройдена' if self.is_valid else 'требуются исправления'}**.",
            "",
        ]

        if self.parse_errors:
            lines.extend(["## Ошибки парсинга", ""])
            for error in self.parse_errors:
                lines.append(f"- {error}")
            lines.append("")

        if self.issues:
            lines.extend([
                "## Найденные замечания",
                "",
                "| Уровень | Код | ID | Файл | Сообщение |",
                "|---|---|---|---|---|",
            ])
            for issue in self.issues:
                lines.append(
                    f"| {issue.severity} | {issue.code} | {issue.card_id} | {issue.file_path} | {issue.message} |"
                )
        return "\n".join(lines)


class KnowledgeBaseValidator:
    """Проверяет структурную целостность базы знаний."""

    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def validate(self) -> ValidationReport:
        report = ValidationReport(
            total_cards=len(self.repository.cards),
            parse_errors=list(self.repository.parse_errors),
        )
        self._validate_unique_ids(report)

        known_ids = {card.id for card in self.repository.cards if card.id}
        for card in self.repository.cards:
            self._validate_required_fields(card, report)
            self._validate_basic_values(card, report)
            self._validate_sources_and_disclaimer(card, report)
            self._validate_links(card, known_ids, report)
            self._validate_folder_category(card, report)
            self._validate_dates(card, report)

        return report

    def save_report(self, output_path: Path) -> ValidationReport:
        report = self.validate()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report.to_markdown(), encoding="utf-8")
        return report

    def _add_issue(
        self,
        report: ValidationReport,
        card: KnowledgeCard,
        severity: str,
        code: str,
        message: str,
    ) -> None:
        report.issues.append(
            ValidationIssue(
                severity=severity,
                code=code,
                file_path=str(card.file_path),
                card_id=card.id or "<no id>",
                message=message,
            )
        )

    def _validate_unique_ids(self, report: ValidationReport) -> None:
        for card_id, cards in self.repository.index.duplicates.items():
            for card in cards:
                self._add_issue(
                    report,
                    card,
                    "ERROR",
                    "DUPLICATE_ID",
                    f"Идентификатор {card_id} повторяется в нескольких карточках.",
                )

    def _validate_required_fields(self, card: KnowledgeCard, report: ValidationReport) -> None:
        for field_name in REQUIRED_FIELDS:
            if field_name not in card.metadata:
                self._add_issue(
                    report,
                    card,
                    "ERROR",
                    "MISSING_FIELD",
                    f"Отсутствует обязательное поле YAML: {field_name}.",
                )

    def _validate_basic_values(self, card: KnowledgeCard, report: ValidationReport) -> None:
        if card.domain and card.domain not in ALLOWED_DOMAINS:
            self._add_issue(report, card, "WARNING", "UNKNOWN_DOMAIN", f"Неизвестный домен: {card.domain}.")

        if card.domain == "diag" and card.category not in ALLOWED_DIAGNOSTIC_CATEGORIES:
            self._add_issue(
                report,
                card,
                "ERROR",
                "UNKNOWN_CATEGORY",
                f"Недопустимая категория диагностической карточки: {card.category}.",
            )

        if card.domain == "protocols" and card.category not in ALLOWED_PROTOCOL_CATEGORIES:
            self._add_issue(
                report,
                card,
                "ERROR",
                "UNKNOWN_CATEGORY",
                f"Недопустимая категория протокольной карточки: {card.category}.",
            )

        if card.domain in {"pharm", "therapy"} and card.category not in ALLOWED_PHARM_CATEGORIES:
            self._add_issue(
                report,
                card,
                "ERROR",
                "UNKNOWN_CATEGORY",
                f"Недопустимая категория фармакологической карточки: {card.category}.",
            )

        if card.urgency and card.urgency not in ALLOWED_URGENCY:
            self._add_issue(report, card, "ERROR", "UNKNOWN_URGENCY", f"Недопустимый уровень срочности: {card.urgency}.")

        status = str(card.metadata.get("status", "")).strip()
        if status and status not in ALLOWED_STATUS:
            self._add_issue(report, card, "WARNING", "UNKNOWN_STATUS", f"Неизвестный статус карточки: {status}.")

        if card.category in {"emergency", "emergency_p"} and card.urgency != "emergency":
            self._add_issue(
                report,
                card,
                "ERROR",
                "EMERGENCY_URGENCY",
                "Карточка emergency/emergency_p должна иметь urgency: emergency.",
            )

    def _validate_sources_and_disclaimer(self, card: KnowledgeCard, report: ValidationReport) -> None:
        sources = card.metadata.get("sources", [])
        if not isinstance(sources, list) or not sources:
            self._add_issue(report, card, "ERROR", "EMPTY_SOURCES", "Поле sources должно быть непустым списком.")

        if card.metadata.get("disclaimer") is not True:
            self._add_issue(report, card, "ERROR", "NO_DISCLAIMER", "Поле disclaimer должно иметь значение true.")

    def _validate_links(self, card: KnowledgeCard, known_ids: set[str], report: ValidationReport) -> None:
        for target_id in card.related:
            if target_id not in known_ids:
                self._add_issue(
                    report,
                    card,
                    "ERROR",
                    "BROKEN_RELATED",
                    f"Ссылка related ведёт на несуществующий документ: {target_id}.",
                )

        for relation in card.relations:
            target_id = str(relation.get("target", "")).strip()
            relation_type = str(relation.get("type", "")).strip()
            if not target_id:
                self._add_issue(report, card, "ERROR", "EMPTY_RELATION_TARGET", "В relations отсутствует target.")
            elif target_id not in known_ids:
                self._add_issue(
                    report,
                    card,
                    "ERROR",
                    "BROKEN_RELATION",
                    f"Связь relations ведёт на несуществующий документ: {target_id}.",
                )
            if not relation_type:
                self._add_issue(report, card, "WARNING", "EMPTY_RELATION_TYPE", "В relations отсутствует type.")
            elif relation_type not in ALLOWED_RELATION_TYPES:
                self._add_issue(
                    report,
                    card,
                    "WARNING",
                    "UNKNOWN_RELATION_TYPE",
                    f"Неизвестный тип связи: {relation_type}.",
                )

    def _validate_folder_category(self, card: KnowledgeCard, report: ValidationReport) -> None:
        path_parts = set(card.file_path.parts)
        for folder_name, expected_category in FOLDER_CATEGORY_RULES.items():
            if folder_name in path_parts and card.category != expected_category:
                self._add_issue(
                    report,
                    card,
                    "ERROR",
                    "FOLDER_CATEGORY_MISMATCH",
                    f"Файл находится в папке {folder_name}, но category={card.category}; ожидается {expected_category}.",
                )

    def _validate_dates(self, card: KnowledgeCard, report: ValidationReport) -> None:
        for field_name in ("date_created", "date_updated", "last_medical_review"):
            value = str(card.metadata.get(field_name, "")).strip()
            if value and not DATE_PATTERN.match(value):
                self._add_issue(
                    report,
                    card,
                    "WARNING",
                    "BAD_DATE_FORMAT",
                    f"Поле {field_name} должно иметь формат YYYY-MM-DD.",
                )
