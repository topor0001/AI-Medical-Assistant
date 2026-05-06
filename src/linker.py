"""Модуль работы со связями между карточками."""

from __future__ import annotations

from .models import RelatedCard
from .repository import KnowledgeRepository


class Linker:
    """Разрешает связи related и relations между документами."""

    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def get_related_cards(self, card_id: str) -> list[RelatedCard]:
        """Возвращает документы, на которые ссылается карточка."""

        source = self.repository.get_by_id(card_id)
        if source is None:
            return []

        related: list[RelatedCard] = []
        seen: set[tuple[str, str]] = set()

        for target_id in source.related:
            key = (target_id, "related")
            if key not in seen:
                related.append(
                    RelatedCard(
                        source_id=source.id,
                        target_id=target_id,
                        relation_type="related",
                        description="Связанный документ из поля related",
                        card=self.repository.get_by_id(target_id),
                    )
                )
                seen.add(key)

        for relation in source.relations:
            target_id = str(relation.get("target", "")).strip()
            relation_type = str(relation.get("type", "related_to")).strip() or "related_to"
            description = str(relation.get("description", "")).strip()
            if not target_id:
                continue
            key = (target_id, relation_type)
            if key not in seen:
                related.append(
                    RelatedCard(
                        source_id=source.id,
                        target_id=target_id,
                        relation_type=relation_type,
                        description=description,
                        card=self.repository.get_by_id(target_id),
                    )
                )
                seen.add(key)

        return related

    def get_backlinks(self, target_id: str) -> list[RelatedCard]:
        """Показывает, какие карточки ссылаются на заданный документ."""

        backlinks: list[RelatedCard] = []
        for card in self.repository.all_cards():
            if card.id == target_id:
                continue
            for related in self.get_related_cards(card.id):
                if related.target_id == target_id:
                    backlinks.append(related)
        return backlinks
