---
id: "PROT-ROUTING-XXX"
title: "Маршрутизация пациента: [Ситуация]"
domain: "protocols"
category: "routing"
body_system:
  - "cardiovascular | respiratory | gastrointestinal | nervous | endocrine | urinary | multisystem"
tags:
  - "routing"
  - "triage"
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "therapist | cardiologist | pulmonologist | gastroenterologist | neurologist | endocrinologist | nephrologist | emergency_physician | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "PROT-PROTOCOL-XXX"
  - "DIAG-DISEASE-XXX"
  - "DIAG-RED_FLAG-XXX"
sources:
  - "Клинические рекомендации"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Маршрутизация пациента: [Ситуация]

> ⚕️ Документ предназначен для определения дальнейших действий и направления пациента.

## Входные условия
- [[DIAG-DISEASE-XXX]] [Диагноз]
- [[DIAG-SYMPTOM-XXX]] [Симптом]
- [[DIAG-RED_FLAG-XXX]] [Красный флаг]

## Общий принцип маршрутизации
[Краткое описание логики: от чего зависит маршрут]

## Категории маршрута

### 🟢 Амбулаторное ведение
- Условия:
  - ...
- Действия:
  - наблюдение
  - контроль
  - плановый визит

### 🟡 Срочное направление
- Условия:
  - ...
- Действия:
  - направление к специалисту в течение X часов/дней

### 🔴 Экстренная помощь
- Условия:
  - ...
- Действия:
  - вызов скорой помощи
  - немедленная госпитализация

### 🏥 Госпитализация
- Показания:
  - ...
- Тип:
  - плановая / экстренная

## Направление к специалистам
- терапевт → ...
- кардиолог → ...
- невролог → ...

## Связь с клиническим протоколом
- [[PROT-PROTOCOL-XXX]]

## Связь с неотложными алгоритмами
- [[PROT-EMERGENCY_P-XXX]]

## Комментарии и ограничения
- ...

## Источники
1. ...