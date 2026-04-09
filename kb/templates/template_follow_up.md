---
id: "PROT-FOLLOW_UP-XXX"
title: "Наблюдение пациента: [Состояние]"
domain: "protocols"
category: "follow_up"
body_system:
  - "cardiovascular | respiratory | endocrine | multisystem"
tags:
  - "follow_up"
  - "monitoring"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist | cardiologist | endocrinologist | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "PROT-PROTOCOL-XXX"
  - "PROT-ROUTING-XXX"
  - "DIAG-DISEASE-XXX"
sources:
  - "Клинические рекомендации"
clinical_guidelines:
  - "Название рекомендаций"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Наблюдение пациента: [Состояние]

> Документ описывает порядок контроля и ведения пациента после начального этапа лечения.

## Цель наблюдения
- контроль эффективности лечения
- раннее выявление осложнений
- коррекция терапии

## Кого наблюдаем
- пациенты с диагнозом [[DIAG-DISEASE-XXX]]

## Частота наблюдения
- первичный контроль: через X дней
- далее: каждые X месяцев

## Контрольные параметры
- артериальное давление
- ЧСС
- лабораторные показатели
- жалобы пациента

## Методы контроля
- [[DIAG-EXAM-XXX]]
- лабораторные исследования
- инструментальные методы

## Критерии эффективности лечения
- ...

## Критерии ухудшения
- ...

## Действия при ухудшении
- [[PROT-ROUTING-XXX]]
- [[PROT-EMERGENCY_P-XXX]]

## Коррекция терапии
- [[PHARM-REGIMEN-XXX]]
- [[PHARM-DRUG-XXX]]

## Переход на другой уровень наблюдения
- амбулаторно → стационар
- планово → срочно

## Связь с протоколом
- [[PROT-PROTOCOL-XXX]]

## Ограничения
- ...

## Источники
1. ...