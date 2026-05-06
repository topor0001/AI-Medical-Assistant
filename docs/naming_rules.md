# Правила именования файлов и идентификаторов

## Идентификаторы

Формат ID:

```text
DIAG-CATEGORY-NNN
```

Примеры:

- `DIAG-SYMPTOM-002` — симптом;
- `DIAG-DISEASE-003` — заболевание;
- `DIAG-EXAM-004` — метод обследования;
- `DIAG-DIFDIAG-001` — дифференциальная диагностика;
- `DIAG-REDFLAG-002` — красный флаг;
- `DIAG-EMERGENCY-001` — неотложное состояние.

## Имена файлов

Формат имени файла:

```text
diag_<category>_<short_name>.md
```

Примеры:

- `diag_symptom_chest_pain.md`;
- `diag_disease_hypertension.md`;
- `diag_exam_ecg.md`;
- `diag_redflag_thunderclap_headache.md`.

## Индексные файлы

В каждой папке диагностического контура есть `index.md`, где указаны ID, названия, срочность и связи карточек.
