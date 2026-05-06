---
id: PHARM-DRUGCLASS-004
title: Тиазидные и тиазидоподобные диуретики
domain: pharm
category: drugclass
atc_code: C03A
body_system:
- cardiovascular
- urinary
tags:
- diuretic
- thiazide
- antihypertensive
- support
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
- nephrologist
age_group:
- adult
- elderly
evidence_level: Ia
related:
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
- PHARM-DOSING-001
relations:
- target: DIAG-DISEASE-001
  type: used_for
  description: Группа используется при АГ.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Группа входит в варианты схемы лечения АГ.
- target: PHARM-DOSING-001
  type: requires_dose_adjustment
  description: При ХБП требуется оценка применимости и коррекция тактики.
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

# Тиазидные и тиазидоподобные диуретики

> Служебная интеграционная карточка для связности фармакологического контура.

## Назначение
Карточка фиксирует группу препаратов, которая может применяться в антигипертензивных схемах и требует учёта функции почек.

## Связанные документы
- [[DIAG-DISEASE-001]] Артериальная гипертензия.
- [[PHARM-REGIMEN-001]] Схема лечения артериальной гипертензии.
- [[PHARM-DOSING-001]] Коррекция доз при ХБП.
