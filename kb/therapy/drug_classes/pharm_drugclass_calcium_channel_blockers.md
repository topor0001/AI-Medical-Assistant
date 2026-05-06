---
id: PHARM-DRUGCLASS-003
title: Блокаторы кальциевых каналов
domain: pharm
category: drugclass
atc_code: C08
body_system:
- cardiovascular
tags:
- calcium_channel_blocker
- antihypertensive
- antianginal
- support
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
- elderly
evidence_level: Ia
related:
- PHARM-DRUG-002
- DIAG-DISEASE-001
- DIAG-DISEASE-002
- PHARM-REGIMEN-001
relations:
- target: PHARM-DRUG-002
  type: class_contains_drug
  description: Амлодипин является представителем группы.
- target: DIAG-DISEASE-001
  type: used_for
  description: Группа используется при АГ.
- target: DIAG-DISEASE-002
  type: used_for
  description: Группа может использоваться при стабильной стенокардии.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Группа входит в схему лечения АГ.
sources:
- Клинические рекомендации «Артериальная гипертензия у взрослых», 2024
- 2023 ESH Guidelines
clinical_guidelines:
- АГ у взрослых, 2024
- 2023 ESH Guidelines
author: Инженер знаний №2
status: medical_review
last_medical_review: '2026-04-09'
medical_reviewer: —
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
disclaimer: true
---

# Блокаторы кальциевых каналов

> Служебная интеграционная карточка для связности фармакологического контура.

## Назначение
Карточка связывает амлодипин, антигипертензивную терапию и диагностические карточки сердечно-сосудистого профиля.

## Связанные документы
- [[PHARM-DRUG-002]] Амлодипин.
- [[DIAG-DISEASE-001]] Артериальная гипертензия.
- [[PHARM-REGIMEN-001]] Схема лечения артериальной гипертензии.
