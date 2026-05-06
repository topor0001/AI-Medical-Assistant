# Диагностический контур базы знаний MedAssist

Индекс содержит реализованный MVP-фрагмент предметной области «Заболевания, симптомы и диагностика».

## Состав карточек

| ID | Название | Категория | Срочность | Файл |
|---|---|---|---|---|
| `DIAG-DIFDIAG-001` | Дифференциальная диагностика боли в груди | `difdiag` | `urgent` | [differential_diagnosis/diag_difdiag_chest_pain.md](differential_diagnosis/diag_difdiag_chest_pain.md) |
| `DIAG-DIFDIAG-002` | Дифференциальная диагностика головной боли | `difdiag` | `urgent` | [differential_diagnosis/diag_difdiag_headache.md](differential_diagnosis/diag_difdiag_headache.md) |
| `DIAG-DIFDIAG-003` | Дифференциальная диагностика одышки | `difdiag` | `urgent` | [differential_diagnosis/diag_difdiag_dyspnea.md](differential_diagnosis/diag_difdiag_dyspnea.md) |
| `DIAG-DISEASE-001` | Артериальная гипертензия | `disease` | `routine` | [diseases/diag_disease_hypertension.md](diseases/diag_disease_hypertension.md) |
| `DIAG-DISEASE-002` | Ишемическая болезнь сердца | `disease` | `urgent` | [diseases/diag_disease_ihd.md](diseases/diag_disease_ihd.md) |
| `DIAG-DISEASE-003` | Пневмония | `disease` | `urgent` | [diseases/diag_disease_pneumonia.md](diseases/diag_disease_pneumonia.md) |
| `DIAG-DISEASE-004` | Бронхиальная астма | `disease` | `routine` | [diseases/diag_disease_asthma.md](diseases/diag_disease_asthma.md) |
| `DIAG-DISEASE-005` | Мигрень | `disease` | `routine` | [diseases/diag_disease_migraine.md](diseases/diag_disease_migraine.md) |
| `DIAG-EMERGENCY-001` | Острый коронарный синдром | `emergency` | `emergency` | [emergencies/diag_emergency_acs.md](emergencies/diag_emergency_acs.md) |
| `DIAG-EMERGENCY-002` | Острое нарушение мозгового кровообращения | `emergency` | `emergency` | [emergencies/diag_emergency_stroke.md](emergencies/diag_emergency_stroke.md) |
| `DIAG-EMERGENCY-003` | Острая дыхательная недостаточность | `emergency` | `emergency` | [emergencies/diag_emergency_acute_respiratory_failure.md](emergencies/diag_emergency_acute_respiratory_failure.md) |
| `DIAG-EXAM-001` | Измерение артериального давления | `exam` | `routine` | [exams/diag_exam_bp_measurement.md](exams/diag_exam_bp_measurement.md) |
| `DIAG-EXAM-002` | Электрокардиография | `exam` | `urgent` | [exams/diag_exam_ecg.md](exams/diag_exam_ecg.md) |
| `DIAG-EXAM-003` | Общий анализ крови | `exam` | `routine` | [exams/diag_exam_cbc.md](exams/diag_exam_cbc.md) |
| `DIAG-EXAM-004` | Рентгенография органов грудной клетки | `exam` | `routine` | [exams/diag_exam_chest_xray.md](exams/diag_exam_chest_xray.md) |
| `DIAG-REDFLAG-001` | Гипертонический криз осложнённый | `redflag` | `emergency` | [red_flags/diag_redflag_hypertensive_crisis.md](red_flags/diag_redflag_hypertensive_crisis.md) |
| `DIAG-REDFLAG-002` | Внезапная сильнейшая головная боль | `redflag` | `emergency` | [red_flags/diag_redflag_thunderclap_headache.md](red_flags/diag_redflag_thunderclap_headache.md) |
| `DIAG-REDFLAG-003` | Выраженная одышка и цианоз | `redflag` | `emergency` | [red_flags/diag_redflag_severe_dyspnea_cyanosis.md](red_flags/diag_redflag_severe_dyspnea_cyanosis.md) |
| `DIAG-SYMPTOM-001` | Головная боль | `symptom` | `routine` | [symptoms/diag_symptom_headache.md](symptoms/diag_symptom_headache.md) |
| `DIAG-SYMPTOM-002` | Боль в груди | `symptom` | `urgent` | [symptoms/diag_symptom_chest_pain.md](symptoms/diag_symptom_chest_pain.md) |
| `DIAG-SYMPTOM-003` | Одышка | `symptom` | `urgent` | [symptoms/diag_symptom_dyspnea.md](symptoms/diag_symptom_dyspnea.md) |
| `DIAG-SYMPTOM-004` | Лихорадка | `symptom` | `routine` | [symptoms/diag_symptom_fever.md](symptoms/diag_symptom_fever.md) |
| `DIAG-SYMPTOM-005` | Боль в животе | `symptom` | `urgent` | [symptoms/diag_symptom_abdominal_pain.md](symptoms/diag_symptom_abdominal_pain.md) |

## Проверочные признаки готовности

- Все карточки имеют YAML-метаданные.
- Используются единые ID и категории.
- Поле `related` содержит только существующие документы диагностического контура.
- Поле `relations` описывает типизированные связи.
- У всех карточек есть источники и `disclaimer: true`.
