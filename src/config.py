"""Настройки MVP MedAssist.

Здесь хранятся правила, которые используются загрузчиком и валидатором.
Если структура базы знаний расширяется, большинство изменений лучше вносить сюда,
а не размазывать по разным модулям программы.
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KB_ROOT = PROJECT_ROOT / "kb"

# Файлы и папки, которые не являются карточками знаний.
EXCLUDED_FILE_NAMES = {"index.md", "README.md"}
EXCLUDED_DIR_NAMES = {"templates"}

# Обязательные поля YAML-метаданных для каждой карточки знаний.
REQUIRED_FIELDS = [
    "id",
    "title",
    "domain",
    "category",
    "body_system",
    "tags",
    "urgency",
    "access_level",
    "target_specialist",
    "age_group",
    "related",
    "sources",
    "clinical_guidelines",
    "last_medical_review",
    "author",
    "version",
    "date_created",
    "date_updated",
    "status",
    "disclaimer",
]

# Разрешённые значения. Набор можно расширять по мере добавления ПО 2 и ПО 3.
ALLOWED_DOMAINS = {"diag", "therapy", "pharm", "protocols", "protocol", "prot", "global"}
ALLOWED_DIAGNOSTIC_CATEGORIES = {
    "symptom",
    "disease",
    "exam",
    "redflag",
    "emergency",
    "difdiag",
}
ALLOWED_PROTOCOL_CATEGORIES = {
    "protocol",
    "emergency_p",
    "routing",
    "scale",
    "checklist",
    "patient_info",
    "screening",
    "follow_up",
}
ALLOWED_PHARM_CATEGORIES = {
    "regimen",
    "drug",
    "drugclass",
    "drug_class",
    "interaction",
    "adr",
    "adverse_reaction",
    "dosing",
    "nonpharm",
}
ALLOWED_URGENCY = {"routine", "urgent", "emergency", "elective"}
ALLOWED_STATUS = {"draft", "medical_review", "approved"}

# Соответствие папки и категории для диагностического контура.
FOLDER_CATEGORY_RULES = {
    "symptoms": "symptom",
    "diseases": "disease",
    "exams": "exam",
    "red_flags": "redflag",
    "emergencies": "emergency",
    "differential_diagnosis": "difdiag",
    "clinical_protocols": "protocol",
    "emergency": "emergency_p",
    "routing": "routing",
    "scales": "scale",
    "checklists": "checklist",
    "patient_info": "patient_info",
    "screening": "screening",
    "follow_up": "follow_up",
    "regimens": "regimen",
    "drugs": "drug",
    "drug_classes": "drugclass",
    "interactions": "interaction",
    "adverse_reactions": "adr",
    "dosing": "dosing",
    "nonpharm": "nonpharm",
}

# Типы связей, которые используются в relations.
ALLOWED_RELATION_TYPES = {
    "associated_with",
    "has_symptom",
    "diagnosed_by",
    "differentiates_from",
    "red_flag_for",
    "requires_attention",
    "may_indicate",
    "related_to",
    "requires_exam",
    "confirmed_by",
    "excluded_by",
    "managed_by_protocol",
    "treated_by",
    "complicates",
    "assesses",
    "protocol_for",
    "emergency_protocol_for",
    "routing_for",
    "uses_routing",
    "uses_scale",
    "used_by_protocol",
    "uses_protocol",
    "uses_checklist",
    "checklist_for",
    "uses_screening",
    "uses_follow_up",
    "follow_up_for",
    "screening_for",
    "patient_info_for",
    "has_patient_info",
    "uses_regimen",
    "uses_drug",
    "uses_exam",
    "uses_redflag",
    "influences_routing",
    "regimen_for",
    "includes_drug",
    "drug_in_regimen",
    "used_for",
    "belongs_to_class",
    "class_contains_drug",
    "uses_drugclass",
    "includes_nonpharm",
    "dose_adjustment_for",
    "requires_dose_adjustment",
    "interaction_for",
    "has_interaction",
    "adverse_reaction_for",
    "may_cause_adr",
    "nonpharm_for",
    "used_by_regimen",
}
