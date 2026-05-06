# Полный листинг проекта MedAssist

## PROJECT_TREE.txt

```text
medassist_course_project_final/
    FULL_PROJECT_LISTING.md
    PROJECT_TREE.txt
    README.md
    main.py
    requirements.txt
    assets/
        diagrams/
            .gitkeep
        figures/
            .gitkeep
    bibliography/
        sources.md
    docs/
        link_types.md
        metadata_schema.md
        mvp_modules.md
        naming_rules.md
        verification_rules.md
    indices/
        diagnostics_catalog.md
        protocols_catalog.md
        therapy_catalog.md
        validation_report.md
    kb/
        diagnostics/
            index.md
            differential_diagnosis/
                diag_difdiag_chest_pain.md
                diag_difdiag_dyspnea.md
                diag_difdiag_headache.md
                index.md
            diseases/
                diag_disease_asthma.md
                diag_disease_hypertension.md
                diag_disease_ihd.md
                diag_disease_migraine.md
                diag_disease_pneumonia.md
                index.md
            emergencies/
                diag_emergency_acs.md
                diag_emergency_acute_respiratory_failure.md
                diag_emergency_stroke.md
                index.md
            exams/
                diag_exam_bp_measurement.md
                diag_exam_cbc.md
                diag_exam_chest_xray.md
                diag_exam_ecg.md
                index.md
            red_flags/
                diag_redflag_hypertensive_crisis.md
                diag_redflag_severe_dyspnea_cyanosis.md
                diag_redflag_thunderclap_headache.md
                index.md
            symptoms/
                diag_symptom_abdominal_pain.md
                diag_symptom_chest_pain.md
                diag_symptom_dyspnea.md
                diag_symptom_fever.md
                diag_symptom_headache.md
                index.md
        global/
            index.md
        protocols/
            index.md
            checklists/
                prot_checklist_hypertension_primary_visit.md
            clinical_protocols/
                prot_protocol_hypertension.md
            emergency/
                prot_emergency_hypertensive_crisis.md
            follow_up/
                prot_follow_up_hypertension.md
            patient_info/
                prot_patient_info_hypertension.md
            routing/
                prot_routing_hypertension.md
            scales/
                prot_scale_hypertension_risk.md
            screening/
                prot_screening_hypertension.md
        templates/
            template_adr.md
            template_checklist.md
            template_difdiag.md
            template_disease.md
            template_dosing.md
            template_drug.md
            template_drugclass.md
            template_emergency.md
            template_emergency_p.md
            template_exam.md
            template_follow_up.md
            template_interaction.md
            template_nonpharm.md
            template_patient_info.md
            template_protocol.md
            template_redflag.md
            template_regimen.md
            template_routing.md
            template_scale.md
            template_screening.md
            template_symptom.md
        therapy/
            index.md
            adverse_reactions/
                pharm_adr_nsaid_gi_bleeding.md
            dosing/
                pharm_dosing_ckd.md
            drug_classes/
                pharm_drugclass_ace_inhibitors.md
                pharm_drugclass_arb.md
                pharm_drugclass_calcium_channel_blockers.md
                pharm_drugclass_nsaids.md
                pharm_drugclass_thiazide_diuretics.md
            drugs/
                pharm_drug_amlodipine.md
                pharm_drug_enalapril.md
                pharm_drug_metformin.md
            interactions/
                pharm_interaction_metformin_contrast.md
            nonpharm/
                pharm_nonpharm_dash_diet.md
            regimens/
                pharm_regimen_hypertension.md
    scripts/
        .gitkeep
    src/
        __init__.py
        cli.py
        config.py
        indexer.py
        linker.py
        markdown_parser.py
        models.py
        repository.py
        scenarios.py
        search_engine.py
        validator.py
    tests/
        conftest.py
        test_linker.py
        test_log.md
        test_parser.py
        test_pharm.py
        test_protocols.py
        test_repository.py
        test_search.py
        test_validator.py
        expected_results/
            .gitkeep
        scenarios/
            .gitkeep

```

## README.md

```markdown
# MedAssist Knowledge Base MVP

MVP курсового проекта **MedAssist** — это небольшой обработчик документно-ориентированной базы знаний интеллектуального медицинского ассистента.

Проект демонстрирует не постановку диагноза, а работу с базой знаний: загрузку Markdown-карточек, чтение YAML-метаданных, поиск, навигацию по связям и проверку целостности.

## 1. Что входит в MVP

- 23 диагностические карточки в формате Markdown + YAML.
- 6 типов единиц знаний: `symptom`, `disease`, `exam`, `redflag`, `emergency`, `difdiag`.
- Шаблоны карточек для диагностического контура.
- Индексы и служебные документы.
- Python-модули для обработки базы знаний.
- Автоматические тесты.
- Консольное меню и команды для демонстрации.

## 2. Структура проекта

```text
medassist_mvp_project/
├── README.md
├── requirements.txt
├── main.py
├── docs/
│   ├── link_types.md
│   ├── metadata_schema.md
│   ├── mvp_modules.md
│   ├── naming_rules.md
│   └── verification_rules.md
├── indices/
│   ├── diagnostics_catalog.md
│   └── validation_report.md
├── kb/
│   ├── diagnostics/
│   │   ├── symptoms/
│   │   ├── diseases/
│   │   ├── exams/
│   │   ├── red_flags/
│   │   ├── emergencies/
│   │   ├── differential_diagnosis/
│   │   └── index.md
│   ├── therapy/
│   │   └── index.md
│   ├── protocols/
│   │   └── index.md
│   └── templates/
├── src/
│   ├── config.py
│   ├── models.py
│   ├── markdown_parser.py
│   ├── repository.py
│   ├── indexer.py
│   ├── search_engine.py
│   ├── linker.py
│   ├── validator.py
│   ├── scenarios.py
│   └── cli.py
└── tests/
    ├── test_parser.py
    ├── test_repository.py
    ├── test_search.py
    ├── test_linker.py
    ├── test_validator.py
    └── test_log.md
```

## 3. Установка

```bash
pip install -r requirements.txt
```

## 4. Запуск интерактивного меню

```bash
python main.py
```

## 5. Быстрые команды для демонстрации

Показать статистику базы знаний:

```bash
python main.py --stats
```

Проверить целостность базы знаний:

```bash
python main.py --validate
```

Записать отчёт проверки в `indices/validation_report.md`:

```bash
python main.py --write-validation-report
```

Найти карточки по запросу:

```bash
python main.py --search "боль в груди"
```

Показать карточку по ID:

```bash
python main.py --show DIAG-SYMPTOM-002
```

Показать связанные документы:

```bash
python main.py --related DIAG-SYMPTOM-002
```

Запустить демонстрационные сценарии:

```bash
python main.py --scenario all
```

Доступные сценарии:

```text
chest_pain
headache
dyspnea
validation
all
```

## 6. Запуск тестов

```bash
pytest -q
```

Ожидаемый результат:

```text
6 passed
```

## 7. Что проверяет валидатор

Валидатор проверяет:

- корректность чтения Markdown/YAML;
- наличие обязательных YAML-полей;
- уникальность `id`;
- существование всех `related`-ссылок;
- существование всех `relations.target`;
- наличие источников;
- наличие `disclaimer: true`;
- соответствие `category` папке хранения;
- корректность `urgency` для emergency-карточек;
- допустимость статуса и типа связи.

## 8. Роль проекта в курсовой работе

Этот MVP закрывает реализационную часть для диагностического контура MedAssist. Он показывает, что база знаний не является просто набором текстовых файлов: она читается программно, индексируется, ищется, проверяется и используется в демонстрационных сценариях.

## 9. Ограничения

MVP не ставит диагноз, не назначает лечение, не заменяет врача, не обрабатывает персональные данные пациентов и не подключается к реальным медицинским информационным системам.


## Протокольный контур и интеграция команды

В обновлённой версии проекта добавлен контур `kb/protocols/`, подготовленный для инженера знаний №3. Он включает клинический протокол артериальной гипертензии, алгоритм неотложной помощи, маршрутизацию, шкалу риска, чек-лист первичного приёма, памятку пациента, скрининг и follow-up. Также добавлены минимальные интеграционные карточки `PHARM-*`, чтобы межпредметные ссылки протоколов на фармакологический контур проходили проверку валидатором до полного наполнения ПО2.

Новые демонстрационные команды:

```bash
python main.py --search "артериальная гипертензия протокол"
python main.py --show PROT-PROTOCOL-001
python main.py --related PROT-PROTOCOL-001
python main.py --scenario hypertension_protocol
```

## Текущий интегрированный состав MVP

В данной версии интегрированы три контура базы знаний:

- инженер знаний №1: `diag` — 23 карточки диагностического контура;
- инженер знаний №2: `pharm` — 13 карточек фармакологии и терапии, включая 8 основных карточек из переданных файлов и 5 служебных карточек для замыкания связей;
- инженер знаний №3: `protocols` — 8 карточек клинических протоколов и маршрутизации.

Проверка валидатором:

```text
Проверено карточек: 44
Ошибок парсинга: 0
Структурных ошибок: 0
Предупреждений: 0
Итог: проверка пройдена
```

Основные команды:

```bash
python main.py --stats
python main.py --validate
python main.py --scenario hypertension_therapy
python main.py --scenario drug_interaction
python -m pytest -q
```


```

## bibliography/sources.md

```markdown
# Источники

Полный список источников оформляется в пояснительной записке в формате BibTeX. В карточках базы знаний источники указываются в YAML-поле `sources` и в разделе `## Источники`.

```

## docs/link_types.md

```markdown
# Типы связей между документами

| Код связи | Назначение | Пример |
|---|---|---|
| `has_symptom` | Заболевание проявляется симптомом | ИБС → Боль в груди |
| `associated_with` | Общая клиническая ассоциация | Головная боль ↔ АГ |
| `diagnosed_by` | Сущность оценивается методом обследования | ОКС → ЭКГ |
| `differentiates_from` | Используется в дифференциальной диагностике | ОКС ↔ ГЭРБ |
| `red_flag_for` | Является опасным признаком для состояния | Внезапная головная боль → ОНМК |
| `complicates` | Связано с осложнением или тяжёлым вариантом | ИБС → ОКС |
| `assesses` | Метод помогает оценить симптом/состояние | Измерение АД → головная боль |

В MVP используется два уровня связей:

1. `related` — простой список ID для валидатора и навигации.
2. `relations` — расширенное описание связи с типом и пояснением.


## Типы связей протокольного и фармакологического контуров

| Тип связи | Назначение |
|---|---|
| `protocol_for` | протокол предназначен для заболевания или состояния |
| `emergency_protocol_for` | алгоритм неотложной помощи относится к опасному состоянию |
| `routing_for` | маршрутизация применяется к заболеванию или ситуации |
| `uses_scale` | документ использует клиническую шкалу |
| `uses_routing` | документ ссылается на маршрут пациента |
| `uses_checklist` | протокол поддерживается чек-листом |
| `uses_screening` | протокол связан со скринингом |
| `uses_follow_up` | протокол связан с последующим наблюдением |
| `patient_info_for` | памятка является пациентским представлением профессионального документа |
| `uses_regimen` | протокольный документ использует фармакологическую схему |
| `uses_drug` | документ связан с конкретным лекарственным средством |
| `regimen_for` | фармакологическая схема предназначена для состояния |
| `includes_drug` | схема включает лекарственное средство |
| `drug_in_regimen` | лекарственное средство входит в схему терапии |

```

## docs/metadata_schema.md

```markdown
# Схема YAML-метаданных MedAssist

## Обязательные поля

| Поле | Назначение | Пример |
|---|---|---|
| `id` | Уникальный идентификатор единицы знаний | `DIAG-SYMPTOM-002` |
| `title` | Название карточки | `Боль в груди` |
| `domain` | Код предметной области | `diag` |
| `category` | Тип единицы знаний | `symptom`, `disease`, `exam`, `difdiag`, `redflag`, `emergency` |
| `body_system` | Система организма | `cardiovascular` |
| `tags` | Теги для поиска и индексации | `chest_pain`, `emergency` |
| `urgency` | Уровень срочности | `routine`, `urgent`, `emergency` |
| `access_level` | Уровень доступа | `professional`, `student`, `patient` |
| `related` | Список связанных ID | `DIAG-DISEASE-002` |
| `relations` | Типизированные связи | `target`, `type`, `description` |
| `sources` | Источники | клинические рекомендации, руководства |
| `clinical_guidelines` | Клинические рекомендации | название и редакция |
| `status` | Статус карточки | `draft`, `medical_review`, `approved` |
| `disclaimer` | Наличие дисклеймера | `true` |

## Допустимые категории диагностического контура

- `symptom` — симптом / синдром;
- `disease` — заболевание;
- `exam` — метод обследования;
- `difdiag` — дифференциальная диагностика;
- `redflag` — красный флаг;
- `emergency` — неотложное состояние.

## Правило для MVP

Для автоматической проверки каждая карточка должна иметь корректный YAML-блок, непустой `id`, непустой `title`, непустой `related` при наличии связей, список `sources` и `disclaimer: true`.

```

## docs/mvp_modules.md

```markdown
# Модули MVP MedAssist

## Назначение

MVP состоит из набора простых Python-модулей. Каждый модуль отвечает за отдельную операцию над базой знаний.

## Связь модулей

```text
main.py
  ↓
src/cli.py
  ├── src/repository.py ──► src/markdown_parser.py ──► src/models.py
  │         └────────────► src/indexer.py
  ├── src/search_engine.py
  ├── src/linker.py
  ├── src/validator.py
  └── src/scenarios.py
```

## Описание файлов

| Файл | Назначение |
|---|---|
| `main.py` | Точка запуска программы |
| `src/config.py` | Настройки, обязательные поля, допустимые значения |
| `src/models.py` | Модель карточки базы знаний |
| `src/markdown_parser.py` | Разбор Markdown-файла и YAML-блока |
| `src/repository.py` | Загрузка всех карточек из каталога `kb/` |
| `src/indexer.py` | Построение индексов по ID, категории, тегам и срочности |
| `src/search_engine.py` | Поиск карточек по запросу |
| `src/linker.py` | Навигация по `related` и `relations` |
| `src/validator.py` | Проверка структурной целостности базы знаний |
| `src/scenarios.py` | Демонстрационные сценарии работы БЗ |
| `src/cli.py` | Консольный интерфейс и команды запуска |

## Поток данных

```text
Markdown/YAML-карточки
        ↓
markdown_parser.py
        ↓
KnowledgeCard
        ↓
repository.py
        ↓
indexer.py
        ↓
search_engine.py / linker.py / validator.py / scenarios.py
        ↓
cli.py
```

```

## docs/naming_rules.md

```markdown
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

```

## docs/verification_rules.md

```markdown
# Правила проверки базы знаний

## Обязательные структурные проверки

1. Каждая карточка должна иметь YAML-блок в начале файла.
2. YAML-блок должен быть корректно читаемым.
3. Каждая карточка должна иметь уникальный `id`.
4. Все обязательные поля должны присутствовать.
5. Все ссылки из `related` должны вести на существующие карточки.
6. Все ссылки из `relations.target` должны вести на существующие карточки.
7. Поле `sources` должно быть непустым списком.
8. Поле `disclaimer` должно иметь значение `true`.
9. Для карточек категории `emergency` поле `urgency` должно иметь значение `emergency`.
10. Категория карточки должна соответствовать папке хранения.

## Обязательные функциональные проверки

1. Поиск по названию должен находить соответствующую карточку.
2. Поиск по тегу должен находить карточки с данным тегом.
3. Фильтр по категории должен возвращать карточки нужного типа.
4. Фильтр по срочности должен возвращать карточки нужного уровня срочности.
5. Навигация по связанным документам должна показывать существующие карточки.
6. Демонстрационные сценарии должны выполняться без ошибок.

```

## indices/diagnostics_catalog.md

```markdown
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

```

## indices/protocols_catalog.md

```markdown
# Индекс протокольного контура MedAssist

| ID | Название | Категория | Срочность | Файл |
|---|---|---|---|---|
| PROT-PROTOCOL-001 | Клинический протокол: Артериальная гипертензия | protocol | routine | clinical_protocols/prot_protocol_hypertension.md |
| PROT-EMERGENCY_P-001 | Алгоритм неотложной помощи: Гипертонический криз | emergency_p | emergency | emergency/prot_emergency_hypertensive_crisis.md |
| PROT-ROUTING-001 | Маршрутизация пациента: Артериальная гипертензия | routing | routine | routing/prot_routing_hypertension.md |
| PROT-SCALE-001 | Клиническая шкала риска при АГ | scale | routine | scales/prot_scale_hypertension_risk.md |
| PROT-CHECKLIST-001 | Чек-лист врача: первичный приём при АГ | checklist | routine | checklists/prot_checklist_hypertension_primary_visit.md |
| PROT-PATIENT_INFO-001 | Памятка для пациента: АГ | patient_info | routine | patient_info/prot_patient_info_hypertension.md |
| PROT-SCREENING-001 | Скрининг: Артериальная гипертензия | screening | routine | screening/prot_screening_hypertension.md |
| PROT-FOLLOW_UP-001 | Наблюдение пациента: АГ | follow_up | routine | follow_up/prot_follow_up_hypertension.md |

```

## indices/therapy_catalog.md

```markdown
# Индекс фармакологического контура MedAssist

Индекс содержит карточки предметной области «Фармакология и терапия»: препараты, фармакологические группы, терапевтическую схему, коррекцию доз, взаимодействие, нежелательную реакцию и немедикаментозный метод.

| ID | Название | Категория | Срочность | Файл |
|---|---|---|---|---|
| `PHARM-ADR-001` | Желудочно-кишечное кровотечение, связанное с приёмом НПВС | `adr` | `urgent` | `adverse_reactions/pharm_adr_nsaid_gi_bleeding.md` |
| `PHARM-DOSING-001` | Коррекция доз антигипертензивных препаратов при хронической болезни почек | `dosing` | `routine` | `dosing/pharm_dosing_ckd.md` |
| `PHARM-DRUG-001` | Эналаприл – Энап, Ренитек, Берлиприл | `drug` | `routine` | `drugs/pharm_drug_enalapril.md` |
| `PHARM-DRUG-002` | Амлодипин – Норваск, Амлотоп, Тенокс | `drug` | `routine` | `drugs/pharm_drug_amlodipine.md` |
| `PHARM-DRUG-020` | Метформин | `drug` | `routine` | `drugs/pharm_drug_metformin.md` |
| `PHARM-DRUGCLASS-001` | Ингибиторы ангиотензинпревращающего фермента (иАПФ) | `drugclass` | `routine` | `drug_classes/pharm_drugclass_ace_inhibitors.md` |
| `PHARM-DRUGCLASS-002` | Блокаторы рецепторов ангиотензина II (БРА) | `drugclass` | `routine` | `drug_classes/pharm_drugclass_arb.md` |
| `PHARM-DRUGCLASS-003` | Блокаторы кальциевых каналов | `drugclass` | `routine` | `drug_classes/pharm_drugclass_calcium_channel_blockers.md` |
| `PHARM-DRUGCLASS-004` | Тиазидные и тиазидоподобные диуретики | `drugclass` | `routine` | `drug_classes/pharm_drugclass_thiazide_diuretics.md` |
| `PHARM-DRUGCLASS-010` | Нестероидные противовоспалительные препараты (НПВС) | `drugclass` | `urgent` | `drug_classes/pharm_drugclass_nsaids.md` |
| `PHARM-INTERACTION-001` | Взаимодействие: Метформин + йодсодержащие контрастные вещества | `interaction` | `urgent` | `interactions/pharm_interaction_metformin_contrast.md` |
| `PHARM-NONPHARM-001` | Диета DASH – диетический подход к остановке гипертензии | `nonpharm` | `routine` | `nonpharm/pharm_nonpharm_dash_diet.md` |
| `PHARM-REGIMEN-001` | Схема лечения артериальной гипертензии | `regimen` | `routine` | `regimens/pharm_regimen_hypertension.md` |

```

## indices/validation_report.md

```markdown
# Отчёт проверки базы знаний MedAssist

Проверено карточек: **44**.
Ошибок парсинга: **0**.
Структурных ошибок: **0**.
Предупреждений: **0**.
Итог: **проверка пройдена**.


```

## kb/diagnostics/differential_diagnosis/diag_difdiag_chest_pain.md

```markdown
---
id: "DIAG-DIFDIAG-001"
title: "Дифференциальная диагностика боли в груди"
domain: "diag"
category: "difdiag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
  - "respiratory"
  - "multisystem"
tags:
  - "difdiag"
  - "chest_pain"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-002"
  - "DIAG-DISEASE-002"
  - "DIAG-EMERGENCY-001"
  - "DIAG-EXAM-001"
  - "DIAG-REDFLAG-001"
  - "DIAG-EXAM-002"
relations:
  - target: "DIAG-SYMPTOM-002"
    type: "differentiates_from"
    description: "ведущий симптом для дифференциальной диагностики"
  - target: "DIAG-DISEASE-002"
    type: "differentiates_from"
    description: "одна из ключевых кардиальных причин"
  - target: "DIAG-EMERGENCY-001"
    type: "red_flag_for"
    description: "жизнеугрожающее состояние, которое нужно исключить"
  - target: "DIAG-EXAM-002"
    type: "diagnosed_by"
    description: "ключевое первичное исследование при боли в груди"
sources:
  - "Руководства по внутренним болезням и клинической диагностике."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по острому коронарному синдрому"
  - "Клинические рекомендации по хроническому коронарному синдрому"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Дифференциальная диагностика: боль в груди

## Ведущий симптом
[[DIAG-SYMPTOM-002]] Боль в груди.

## Ключевые вопросы при сборе анамнеза
1. Когда началась боль и как быстро нарастала? — помогает отличить острое состояние от хронического.
2. Где локализована боль и есть ли иррадиация? — ориентирует на ишемический, плевральный или мышечно-скелетный характер.
3. Связана ли боль с нагрузкой, дыханием, движением, положением тела, приёмом пищи? — помогает сузить диагностический ряд.
4. Есть ли одышка, потливость, слабость, тошнота, страх, кашель, лихорадка? — уточняет системную значимость и срочность.
5. Есть ли сердечно-сосудистые факторы риска или уже известная ИБС/АГ? — повышает вероятность кардиальной причины.

## Ключевые данные объективного осмотра
- оценка общего состояния и уровня сознания;
- витальные показатели, в том числе [[DIAG-EXAM-001]] измерение АД;
- признаки дыхательной недостаточности;
- аускультация сердца и лёгких;
- поиск признаков гемодинамической нестабильности;
- оценка воспроизводимости боли при пальпации.

## Дифференциально-диагностическая таблица

| Заболевание / состояние | Ключевые признаки | Отличительные особенности | Обязательные обследования | Тактическая значимость |
|-------------------------|------------------|---------------------------|---------------------------|------------------------|
| [[DIAG-EMERGENCY-001]] Острый коронарный синдром | Интенсивная загрудинная боль, слабость, потливость, одышка | Боль в покое, системные симптомы, неотложность | ЭКГ, тропонины, оценка гемодинамики | Исключать в первую очередь |
| [[DIAG-DISEASE-002]] Ишемическая болезнь сердца | Загрудинная боль, связь с нагрузкой | Более типично хроническое, стереотипное течение | ЭКГ, функциональная оценка ишемии | Срочная, но не всегда экстренная оценка |
| [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый | Боль в груди на фоне высокого АД | Есть острое поражение органов-мишеней или угрожающий контекст | Измерение АД, ЭКГ, клиническая оценка осложнений | Экстренная оценка |
| Плеврит / пневмония | Боль при дыхании, кашель | Плевральный характер боли, дыхательная симптоматика | Аускультация, рентгенография | Срочность зависит от тяжести |
| Мышечно-скелетная боль | Локальная боль, связь с движением | Воспроизводится пальпацией, нет типичной ишемии | Осмотр, исключение опасных причин | Обычно неотложность ниже |
| ГЭРБ / эзофагеальная боль | Жжение, дискомфорт за грудиной | Связь с пищей и положением тела | Клиническая оценка, при необходимости гастроэнтерологическое обследование | После исключения опасных причин |

## 🚩 «Красные флаги»
- 🔴 Боль в груди с одышкой, холодным потом и слабостью → срочно исключать ОКС.
- 🔴 Боль в груди на фоне очень высокого АД → исключать осложнённый гипертонический криз.
- 🔴 Гемодинамическая нестабильность, синкопе, снижение сознания → немедленная экстренная помощь.
- 🔴 Внезапная крайне интенсивная боль → исключать жизнеугрожающее состояние.

## Приоритетные диагностические направления
- исключение острого коронарного синдрома;
- оценка гемодинамики и уровня артериального давления;
- разграничение кардиальной, респираторной, гастроэнтерологической и мышечно-скелетной боли;
- выявление признаков критического течения.

## Связанные документы
- [[DIAG-SYMPTOM-002]] — ведущий симптом
- [[DIAG-DISEASE-002]] — частая нозологическая причина
- [[DIAG-EMERGENCY-001]] — состояние, требующее первоочередного исключения
- [[DIAG-EXAM-001]] — обязательная часть первичной оценки
- [[DIAG-REDFLAG-001]] — опасный гипертензивный контекст боли

## Источники
1. Руководства по внутренним болезням и клинической диагностике.
2. Клинические рекомендации по соответствующему профилю, действующая редакция.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/differential_diagnosis/diag_difdiag_dyspnea.md

```markdown
---
id: "DIAG-DIFDIAG-003"
title: "Дифференциальная диагностика одышки"
domain: "diag"
category: "difdiag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
  - "cardiovascular"
  - "multisystem"
tags:
  - "difdiag"
  - "dyspnea"
  - "respiratory"
  - "cardiology"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "cardiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-DISEASE-003"
  - "DIAG-DISEASE-004"
  - "DIAG-EMERGENCY-003"
  - "DIAG-REDFLAG-003"
  - "DIAG-EXAM-002"
  - "DIAG-EXAM-004"
relations:
  - target: "DIAG-SYMPTOM-003"
    type: "differentiates_from"
    description: "ведущий симптом"
  - target: "DIAG-DISEASE-003"
    type: "differentiates_from"
    description: "инфекционно-лёгочная причина"
  - target: "DIAG-DISEASE-004"
    type: "differentiates_from"
    description: "бронхообструктивная причина"
  - target: "DIAG-EMERGENCY-003"
    type: "red_flag_for"
    description: "неотложное состояние при тяжёлой одышке"
  - target: "DIAG-EXAM-004"
    type: "diagnosed_by"
    description: "помогает оценить лёгочные причины"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых"
  - "GINA Global Strategy for Asthma Management and Prevention"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Дифференциальная диагностика: одышка

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Ведущий симптом
[[DIAG-SYMPTOM-003]] Одышка.

## Ключевые вопросы при сборе анамнеза
1. Когда возникла одышка и как быстро нарастала? — помогает отделить острое состояние от хронического.
2. Есть ли кашель, лихорадка, боль в груди? — ориентирует на инфекционную, плевральную или кардиальную причину.
3. Есть ли свистящее дыхание и приступообразность? — указывает на бронхообструкцию.
4. Возникает ли одышка в положении лёжа или ночью? — может указывать на кардиальную причину.
5. Есть ли цианоз, спутанность сознания, невозможность говорить? — признаки срочности.

## Ключевые данные объективного осмотра
- частота дыхания;
- сатурация при наличии пульсоксиметра;
- аускультация лёгких;
- частота пульса и АД;
- признаки цианоза и нарушения сознания.

## Дифференциально-диагностическая таблица
| Направление | Поддерживающие признаки | Документ БЗ |
|---|---|---|
| Пневмония | лихорадка, кашель, хрипы, изменения на рентгенографии | [[DIAG-DISEASE-003]] |
| Бронхиальная астма | приступы, свистящее дыхание, триггеры | [[DIAG-DISEASE-004]] |
| Острая дыхательная недостаточность | выраженная одышка, цианоз, нарушение сознания | [[DIAG-EMERGENCY-003]] |
| Кардиальная причина | боль в груди, отёки, одышка при нагрузке/лёжа | [[DIAG-EXAM-002]] |

## 🚩 «Красные флаги»
- [[DIAG-REDFLAG-003]] выраженная одышка и цианоз;
- одышка в покое;
- боль в груди;
- спутанность сознания;
- внезапное начало;
- быстрое ухудшение.

## Приоритетные диагностические направления
- оценка жизненных показателей;
- [[DIAG-EXAM-004]] рентгенография органов грудной клетки при лёгочной симптоматике;
- [[DIAG-EXAM-002]] ЭКГ при подозрении на кардиальную причину;
- лабораторные исследования по клинической ситуации.

## Связанные документы
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-DISEASE-003]] — пневмония.
- [[DIAG-DISEASE-004]] — бронхиальная астма.
- [[DIAG-EMERGENCY-003]] — острая дыхательная недостаточность.
- [[DIAG-REDFLAG-003]] — выраженная одышка и цианоз.

```

## kb/diagnostics/differential_diagnosis/diag_difdiag_headache.md

```markdown
---
id: "DIAG-DIFDIAG-002"
title: "Дифференциальная диагностика головной боли"
domain: "diag"
category: "difdiag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "nervous"
  - "cardiovascular"
  - "multisystem"
tags:
  - "difdiag"
  - "headache"
  - "redflag"
  - "neurology"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "neurologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-001"
  - "DIAG-DISEASE-001"
  - "DIAG-DISEASE-005"
  - "DIAG-REDFLAG-001"
  - "DIAG-REDFLAG-002"
  - "DIAG-EMERGENCY-002"
  - "DIAG-EXAM-001"
relations:
  - target: "DIAG-SYMPTOM-001"
    type: "differentiates_from"
    description: "ведущий симптом"
  - target: "DIAG-DISEASE-005"
    type: "differentiates_from"
    description: "первичная головная боль"
  - target: "DIAG-REDFLAG-002"
    type: "red_flag_for"
    description: "красный флаг опасной вторичной боли"
  - target: "DIAG-EMERGENCY-002"
    type: "red_flag_for"
    description: "сосудистая катастрофа в дифференциальном ряду"
sources:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения, действующая редакция."
  - "Клинические рекомендации по мигрени, действующая редакция."
  - "Руководства по неврологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по мигрени"
  - "Клинические рекомендации по острому нарушению мозгового кровообращения"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Дифференциальная диагностика: головная боль

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Ведущий симптом
[[DIAG-SYMPTOM-001]] Головная боль.

## Ключевые вопросы при сборе анамнеза
1. Когда началась боль и была ли она внезапной? — помогает выявить красные флаги.
2. Изменился ли характер привычной головной боли? — важно для исключения вторичной причины.
3. Есть ли неврологические симптомы? — указывает на необходимость срочной оценки.
4. Есть ли лихорадка, ригидность затылочных мышц, нарушение сознания? — помогает выявить инфекционные и опасные причины.
5. Измерялось ли артериальное давление? — важно при подозрении на гипертонический криз.

## Ключевые данные объективного осмотра
- уровень сознания;
- неврологический статус;
- артериальное давление;
- признаки менингеального синдрома;
- температура тела.

## Дифференциально-диагностическая таблица
| Направление | Поддерживающие признаки | Документ БЗ |
|---|---|---|
| Мигрень | Повторные приступы, светобоязнь, тошнота, возможная аура | [[DIAG-DISEASE-005]] |
| Гипертонический криз | Высокое АД + признаки поражения органов-мишеней | [[DIAG-REDFLAG-001]] |
| ОНМК/кровоизлияние | внезапное начало, неврологический дефицит, нарушение сознания | [[DIAG-EMERGENCY-002]] |
| Инфекционная причина | лихорадка, менингеальные признаки | требуется срочная оценка |

## 🚩 «Красные флаги»
- [[DIAG-REDFLAG-002]] внезапная сильнейшая головная боль;
- неврологический дефицит;
- нарушение сознания;
- лихорадка с менингеальными признаками;
- новый тип боли у пожилого пациента;
- головная боль после травмы.

## Приоритетные диагностические направления
- оценка срочности и жизненных показателей;
- [[DIAG-EXAM-001]] измерение артериального давления;
- неврологический осмотр;
- решение о дополнительных обследованиях врачом.

## Связанные документы
- [[DIAG-SYMPTOM-001]] — головная боль.
- [[DIAG-DISEASE-005]] — мигрень.
- [[DIAG-REDFLAG-002]] — внезапная сильнейшая головная боль.
- [[DIAG-EMERGENCY-002]] — острое нарушение мозгового кровообращения.

```

## kb/diagnostics/differential_diagnosis/index.md

```markdown
# Дифференциальная диагностика

Индекс раздела `differential_diagnosis`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-DIFDIAG-001` | Дифференциальная диагностика боли в груди | `urgent` | `DIAG-SYMPTOM-002`, `DIAG-DISEASE-002`, `DIAG-EMERGENCY-001`, `DIAG-EXAM-001`, `DIAG-REDFLAG-001`, `DIAG-EXAM-002` | [diag_difdiag_chest_pain.md](diag_difdiag_chest_pain.md) |
| `DIAG-DIFDIAG-002` | Дифференциальная диагностика головной боли | `urgent` | `DIAG-SYMPTOM-001`, `DIAG-DISEASE-001`, `DIAG-DISEASE-005`, `DIAG-REDFLAG-001`, `DIAG-REDFLAG-002`, `DIAG-EMERGENCY-002` | [diag_difdiag_headache.md](diag_difdiag_headache.md) |
| `DIAG-DIFDIAG-003` | Дифференциальная диагностика одышки | `urgent` | `DIAG-SYMPTOM-003`, `DIAG-DISEASE-003`, `DIAG-DISEASE-004`, `DIAG-EMERGENCY-003`, `DIAG-REDFLAG-003`, `DIAG-EXAM-002` | [diag_difdiag_dyspnea.md](diag_difdiag_dyspnea.md) |

```

## kb/diagnostics/diseases/diag_disease_asthma.md

```markdown
---
id: "DIAG-DISEASE-004"
title: "Бронхиальная астма"
domain: "diag"
category: "disease"
icd_10: "J45"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
tags:
  - "asthma"
  - "respiratory"
  - "dyspnea"
  - "wheezing"
  - "chronic"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "allergist"
age_group:
  - "adult"
  - "child"
  - "adolescent"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-DIFDIAG-003"
  - "DIAG-REDFLAG-003"
relations:
  - target: "DIAG-SYMPTOM-003"
    type: "has_symptom"
    description: "одышка является одним из типичных проявлений"
  - target: "DIAG-DIFDIAG-003"
    type: "differentiates_from"
    description: "требуется отличать от других причин одышки"
  - target: "DIAG-REDFLAG-003"
    type: "red_flag_for"
    description: "тяжёлый приступ может сопровождаться дыхательной недостаточностью"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "GINA Global Strategy for Asthma Management and Prevention"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Бронхиальная астма

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Бронхиальная астма — хроническое воспалительное заболевание дыхательных путей, проявляющееся вариабельными респираторными симптомами и обратимой бронхиальной обструкцией. МКБ-10: J45.

## Эпидемиология
- встречается у детей и взрослых;
- течение может быть интермиттирующим или персистирующим;
- выраженность симптомов зависит от триггеров, контроля заболевания и сопутствующих факторов.

## Этиология и патогенез
В основе лежит хроническое воспаление дыхательных путей, гиперреактивность бронхов и бронхоконстрикция. Симптомы могут провоцироваться аллергенами, физической нагрузкой, инфекциями, холодным воздухом, дымом и раздражающими веществами.

## Клиническая картина
- приступы [[DIAG-SYMPTOM-003]] одышки;
- свистящее дыхание;
- чувство стеснения в груди;
- кашель, особенно ночью или ранним утром;
- вариабельность симптомов во времени.

## 🚩 «Красные флаги»
- одышка в покое, невозможность говорить фразами;
- выраженная слабость, сонливость, спутанность сознания;
- цианоз;
- отсутствие эффекта от обычной помощи;
- признаки дыхательной недостаточности.

## Диагностика
- сбор анамнеза, выявление вариабельности симптомов и триггеров;
- оценка функции внешнего дыхания по назначению врача;
- оценка аллергологического анамнеза;
- исключение других причин одышки.

## Дифференциальная диагностика
Проводится с ХОБЛ, пневмонией, сердечной недостаточностью, тревожными расстройствами, ТЭЛА и другими причинами одышки.

## Лечение (обзор)
В базе знаний лечение описывается только как справочный контекст. Конкретные препараты, дозы и ступень терапии выбирает врач на основе клинических рекомендаций и контроля заболевания.

## Прогноз
При контролируемом течении возможно сохранение нормальной активности. Неконтролируемая астма повышает риск обострений и неотложных состояний.

## Профилактика
- контроль триггеров;
- обучение пациента правильной технике ингаляции;
- регулярная оценка контроля заболевания;
- план действий при ухудшении по назначению врача.

## Информация для пациента
При выраженной одышке, посинении губ, невозможности говорить или резком ухудшении состояния нужно срочно обращаться за медицинской помощью.

## Связанные документы
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-DIFDIAG-003]] — дифференциальная диагностика одышки.
- [[DIAG-REDFLAG-003]] — выраженная одышка и цианоз.

```

## kb/diagnostics/diseases/diag_disease_hypertension.md

```markdown
---
id: "DIAG-DISEASE-001"
title: "Артериальная гипертензия"
domain: "diag"
category: "disease"
icd_10: "I10; I11-I15"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "cardiovascular"
  - "chronic"
  - "hypertension"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
age_group:
  - "adult"
  - "elderly"
evidence_level: "Ia"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-001"
  - "DIAG-SYMPTOM-002"
  - "DIAG-EXAM-001"
  - "DIAG-REDFLAG-001"
relations:
  - target: "DIAG-SYMPTOM-001"
    type: "has_symptom"
    description: "головная боль может сопровождать повышение АД"
  - target: "DIAG-EXAM-001"
    type: "diagnosed_by"
    description: "измерение АД является базовым методом выявления"
  - target: "DIAG-REDFLAG-001"
    type: "complicates"
    description: "осложнённый гипертонический криз связан с поражением органов-мишеней"
sources:
  - "Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция."
  - "2023 ESH Guidelines for the management of arterial hypertension."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "КР Минздрава РФ по артериальной гипертензии"
  - "2023 ESH Guidelines for the management of arterial hypertension"
last_medical_review: "2025-02-15"
medical_reviewer: "Иванов И.И., д.м.н., кардиолог"
author: "Инженер знаний №1"
version: "1.0"
date_created: "2025-01-20"
date_updated: "2026-04-09"
status: "approved"
disclaimer: true
---

# Артериальная гипертензия

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
Артериальная гипертензия (АГ) — стойкое повышение артериального давления, при котором офисное систолическое АД составляет ≥ 140 мм рт. ст. и/или диастолическое АД ≥ 90 мм рт. ст.  
МКБ-10: I10; I11–I15.

## Эпидемиология
- **Распространённость**: одно из наиболее частых хронических сердечно-сосудистых состояний у взрослых.
- **Заболеваемость**: возрастает с увеличением возраста и накоплением факторов риска.
- **Возрастная группа**: чаще выявляется после 40 лет, но возможна и у молодых пациентов.
- **Гендерные различия**: до среднего возраста чаще встречается у мужчин, после менопаузы частота у женщин возрастает.
- **Факторы риска**: наследственность, ожирение, избыток соли, гиподинамия, курение, злоупотребление алкоголем, стресс, сахарный диабет, дислипидемия, хроническая болезнь почек.

## Этиология и патогенез
В большинстве случаев АГ является первичной (эссенциальной) и развивается как многофакторное заболевание. В её формировании участвуют наследственная предрасположенность, гиперактивация симпатической нервной системы, нарушения ренин-ангиотензин-альдостероновой системы, эндотелиальная дисфункция и повышение сосудистого сопротивления. Длительное существование высокого давления приводит к ремоделированию сосудистой стенки, гипертрофии миокарда левого желудочка и поражению органов-мишеней. Вторичная гипертензия развивается на фоне заболеваний почек, эндокринной патологии, сосудистых нарушений или лекарственного воздействия.

## Классификация

| Критерий | Классификация |
|----------|--------------|
| По происхождению | Первичная (эссенциальная), вторичная |
| По степени | 1 степень, 2 степень, 3 степень |
| По риску | Низкий, умеренный, высокий, очень высокий сердечно-сосудистый риск |
| По течению | Стабильная, лабильная, резистентная |

## Клиническая картина

### Основные симптомы
- **Головная боль** — чаще в затылочной области, особенно утром.
- **Головокружение** — нередко при выраженном повышении АД.
- **Шум в ушах** — возможен при нестабильном давлении.
- **Боль в груди** — требует исключения ишемии миокарда или осложнённого криза.
- **Одышка** — при длительном течении и поражении сердца.
- **Бессимптомное течение** — частый вариант, особенно на ранних стадиях.

### Данные объективного осмотра
- повышение офисного АД;
- возможная тахикардия;
- признаки гипертрофии левого желудочка;
- сосудистые изменения глазного дна;
- при осложнениях — неврологический дефицит, застойные хрипы, симптомы острого поражения органов-мишеней.

### Особенности течения
- **Хроническое**: нередко многолетнее бессимптомное течение.
- **Осложнения**: гипертонический криз, инсульт, инфаркт миокарда, сердечная недостаточность, хроническая болезнь почек, ретинопатия.

## 🚩 «Красные флаги»
- 🔴 Резкое повышение АД с неврологической симптоматикой → исключать острое поражение ЦНС.
- 🔴 Боль в груди на фоне высокого АД → исключать ОКС и осложнённый криз.
- 🔴 Одышка, отёк лёгких, выраженная слабость → срочная оценка осложнений.
- 🔴 Нарушение зрения, спутанность сознания, судороги → экстренное направление.

## Диагностика

### Обязательные исследования

| Метод | Ожидаемый результат | Цель |
|-------|-------------------|------|
| [[DIAG-EXAM-001]] Измерение артериального давления | Подтверждение стойкого повышения АД | Верификация диагноза |
| ОАК | Обычно без специфических изменений | Базовая оценка состояния |
| Биохимия крови | Оценка креатинина, глюкозы, липидов, электролитов | Выявление факторов риска и поражения органов-мишеней |
| Общий анализ мочи | Возможна протеинурия, микрогематурия | Оценка почечного поражения |
| ЭКГ | Признаки гипертрофии ЛЖ, ишемии, аритмий | Оценка сердечного поражения |

### Дополнительные исследования
- Суточное мониторирование АД — при подозрении на вариабельную, скрытую или резистентную гипертензию.
- Эхокардиография — при подозрении на гипертрофию ЛЖ и сердечную недостаточность.
- УЗИ почек и сосудов — при подозрении на вторичную гипертензию.
- Осмотр глазного дна — для оценки гипертонической ретинопатии.

### Диагностические критерии
Диагноз основывается на повторно подтверждённом повышении АД при корректном измерении, оценке факторов риска, поражения органов-мишеней и исключении вторичных причин.

## Дифференциальная диагностика

| Заболевание | Общие черты | Отличия |
|------------|------------|---------|
| Симптоматическая (вторичная) гипертензия | Повышение АД | Есть конкретная причинная патология |
| [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый | Высокое АД | Есть острое поражение органов-мишеней |
| Тревожное расстройство / паническая реакция | Сердцебиение, тревога, повышение АД | Повышение АД обычно транзиторное |

## Лечение (обзор)

### Немедикаментозное
- снижение массы тела;
- ограничение соли;
- регулярная физическая активность;
- отказ от курения;
- ограничение алкоголя;
- контроль стресса.

### Медикаментозное
- **Первая линия**: иАПФ, БРА, БКК, тиазидоподобные диуретики.
- **Вторая линия**: бета-блокаторы, комбинированная терапия по показаниям.
- **При осложнениях**: выбор схемы зависит от поражения органов-мишеней и сопутствующих состояний.

### Хирургическое (если применимо)
- **Показания**: не характерно для первичной АГ; возможно при вторичных причинах.
- **Методы**: коррекция причинного состояния.

## Прогноз
- **Благоприятный при**: раннем выявлении, достижении целевого АД и контроле факторов риска.
- **Неблагоприятные прогностические факторы**: курение, СД, ХБП, гипертрофия ЛЖ, перенесённые сосудистые события.
- **Летальность**: связана преимущественно с сердечно-сосудистыми осложнениями, а не с самой АГ как изолированным состоянием.

## Профилактика

### Первичная
- здоровое питание;
- контроль массы тела;
- физическая активность;
- ограничение соли и алкоголя.

### Вторичная
- регулярный самоконтроль АД;
- приверженность терапии;
- контроль факторов риска;
- динамическое наблюдение.

## Диспансерное наблюдение
- **Частота визитов**: зависит от степени риска и контроля давления.
- **Контролируемые показатели**: АД, ЧСС, масса тела, функция почек, липиды, глюкоза.
- **Целевые значения**: определяются индивидуально с учётом возраста и сопутствующих заболеваний.

## Особенности у отдельных групп
- **Дети**: требует отдельной возрастной оценки и поиска вторичных причин.
- **Пожилые**: выше риск ортостатических реакций и полиморбидности.
- **Беременные**: требует отдельного акушерского и терапевтического маршрута.

## Информация для пациента
Артериальная гипертензия — это стойкое повышение давления, которое может долго протекать без явных жалоб. Опасность связана не только с цифрами давления, но и с риском инсульта, инфаркта и поражения почек. Нельзя самостоятельно отменять или менять лечение. Срочно обращаться за медицинской помощью нужно при резкой головной боли, боли в груди, одышке, слабости в конечностях или нарушении зрения.

## Связанные документы
- [[DIAG-SYMPTOM-001]] — частый ассоциированный симптом
- [[DIAG-SYMPTOM-002]] — возможная жалоба и признак осложнений
- [[DIAG-EXAM-001]] — базовый метод верификации
- [[DIAG-REDFLAG-001]] — опасное осложнение

## Источники
1. Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция.
2. 2023 ESH Guidelines for the management of arterial hypertension.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/diseases/diag_disease_ihd.md

```markdown
---
id: "DIAG-DISEASE-002"
title: "Ишемическая болезнь сердца"
domain: "diag"
category: "disease"
icd_10: "I20-I25"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "cardiovascular"
  - "ihd"
  - "chest_pain"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
age_group:
  - "adult"
  - "elderly"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-002"
  - "DIAG-DIFDIAG-001"
  - "DIAG-EMERGENCY-001"
  - "DIAG-EXAM-001"
  - "DIAG-EXAM-002"
relations:
  - target: "DIAG-SYMPTOM-002"
    type: "has_symptom"
    description: "боль/дискомфорт в груди является типичным симптомом"
  - target: "DIAG-EMERGENCY-001"
    type: "complicates"
    description: "ОКС относится к острому проявлению коронарной патологии"
  - target: "DIAG-EXAM-002"
    type: "diagnosed_by"
    description: "ЭКГ используется в первичной оценке боли в груди"
  - target: "DIAG-DIFDIAG-001"
    type: "differentiates_from"
    description: "требуется исключение других причин боли в груди"
sources:
  - "Клинические рекомендации по хроническому коронарному синдрому, действующая редакция."
  - "Руководства Европейского общества кардиологов по хроническим коронарным синдромам."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по хроническому коронарному синдрому"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Ишемическая болезнь сердца

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
Ишемическая болезнь сердца (ИБС) — группа клинических состояний, обусловленных несоответствием между потребностью миокарда в кислороде и коронарным кровотоком, чаще всего вследствие атеросклеротического поражения коронарных артерий. В клиническом контуре БЗ ИБС является одной из ключевых причин боли в груди.

## Эпидемиология
- **Распространённость**: одна из ведущих причин сердечно-сосудистой заболеваемости и смертности.
- **Заболеваемость**: возрастает с увеличением возраста и накоплением факторов риска.
- **Возрастная группа**: чаще у пациентов среднего и пожилого возраста.
- **Гендерные различия**: у мужчин манифестирует раньше; у женщин риск возрастает после менопаузы.
- **Факторы риска**: АГ, дислипидемия, курение, СД, ожирение, семейный анамнез, гиподинамия.

## Этиология и патогенез
Основной причиной ИБС является атеросклероз коронарных артерий. Формирование бляшки приводит к хроническому ограничению коронарного кровотока или к острому тромбозу при её повреждении. Ишемия миокарда может проявляться стабильной стенокардией, безболевой ишемией, хроническим коронарным синдромом или острым коронарным синдромом. Клиническая выраженность зависит от степени стеноза, стабильности бляшки и сопутствующих факторов, повышающих потребность миокарда в кислороде.

## Классификация

| Критерий | Классификация |
|----------|--------------|
| По течению | Хронический коронарный синдром, острый коронарный синдром |
| По проявлениям | Стенокардия, безболевая ишемия, постинфарктные состояния |
| По функциональному классу | I–IV для стенокардии напряжения |
| По осложнениям | Нарушения ритма, сердечная недостаточность, инфаркт миокарда |

## Клиническая картина

### Основные симптомы
- **Боль в груди** — давящая, сжимающая, жгучая, часто загрудинная.
- **Иррадиация боли** — в левую руку, плечо, шею, нижнюю челюсть.
- **Одышка** — эквивалент ишемии, особенно у пожилых и пациентов с диабетом.
- **Связь с нагрузкой** — типична для стабильной ишемии.
- **Снижение толерантности к нагрузке** — частая жалоба.

### Данные объективного осмотра
- между приступами осмотр может быть малоинформативным;
- возможны признаки атеросклеротического поражения сосудов;
- при осложнениях — тахикардия, аритмия, признаки сердечной недостаточности.

### Особенности течения
- **Хроническое**: стабильные симптомы при нагрузке.
- **Острое**: при нестабильности атеросклеротической бляшки возможен переход в ОКС.
- **Осложнения**: инфаркт миокарда, аритмии, сердечная недостаточность, внезапная сердечная смерть.

## 🚩 «Красные флаги»
- 🔴 Боль в груди в покое или нарастающая по частоте/интенсивности → исключать ОКС.
- 🔴 Боль с холодным потом, слабостью, одышкой → срочная кардиологическая оценка.
- 🔴 Гемодинамическая нестабильность, синкопе, выраженная аритмия → экстренная помощь.

## Диагностика

### Обязательные исследования

| Метод | Ожидаемый результат | Цель |
|-------|-------------------|------|
| ЭКГ | Ишемические изменения, нарушения ритма | Первичная оценка ишемии |
| Тропонины | Обычно нормальны при стабильной ИБС, повышаются при некрозе | Исключение инфаркта |
| ЭхоКГ | Нарушения локальной сократимости, оценка функции ЛЖ | Оценка последствий ишемии |
| Нагрузочные тесты / визуализация ишемии | Признаки индуцируемой ишемии | Подтверждение ишемии |
| Коронарная визуализация | Стенозирующее поражение коронарных артерий | Анатомическая верификация |

### Дополнительные исследования
- липидный профиль;
- глюкоза / HbA1c;
- оценка функции почек;
- холтеровское мониторирование при подозрении на аритмии.

### Диагностические критерии
Диагноз ИБС формируется на основании клинической картины, оценки вероятности коронарного поражения, данных ЭКГ, функциональных тестов и методов визуализации коронарного русла.

## Дифференциальная диагностика

| Заболевание | Общие черты | Отличия |
|------------|------------|---------|
| [[DIAG-EMERGENCY-001]] Острый коронарный синдром | Боль в груди ишемического характера | Есть признаки острого коронарного события |
| ГЭРБ | Дискомфорт за грудиной | Связь с приёмом пищи, положением тела |
| Межрёберная невралгия / мышечно-скелетная боль | Боль в грудной клетке | Усиливается при движении и пальпации |

## Лечение (обзор)

### Немедикаментозное
- коррекция образа жизни;
- отказ от курения;
- контроль АД, липидов, массы тела;
- дозированная физическая активность.

### Медикаментозное
- **Первая линия**: антиангинальная терапия и вторичная профилактика по показаниям.
- **Вторая линия**: усиление антиангинальной терапии и коррекция факторов риска.
- **При осложнениях**: переход к тактике ведения ОКС или ХСН.

### Хирургическое (если применимо)
- **Показания**: гемодинамически значимые стенозы, рефрактерная симптоматика, высокий риск.
- **Методы**: ЧКВ, АКШ.

## Прогноз
- **Благоприятный при**: контроле факторов риска и своевременной терапии.
- **Неблагоприятные прогностические факторы**: диабет, сниженная ФВ ЛЖ, многососудистое поражение, перенесённый инфаркт.
- **Летальность**: определяется тяжестью атеросклеротического поражения и осложнениями.

## Профилактика

### Первичная
- коррекция факторов риска;
- профилактика атеросклероза;
- здоровый образ жизни.

### Вторичная
- контроль липидов, АД, гликемии;
- приверженность терапии;
- наблюдение у кардиолога.

## Диспансерное наблюдение
- **Частота визитов**: зависит от стабильности состояния.
- **Контролируемые показатели**: симптомы, АД, ЧСС, липиды, толерантность к нагрузке.
- **Целевые значения**: определяются по суммарному сердечно-сосудистому риску.

## Особенности у отдельных групп
- **Дети**: не является типичной нозологией детского возраста.
- **Пожилые**: чаще атипичные симптомы и одышка вместо типичной боли.
- **Беременные**: требует отдельной оценки и специализированного маршрута.

## Информация для пациента
ИБС связана с недостаточным кровоснабжением сердечной мышцы. Часто она проявляется болью или сдавлением в груди при нагрузке, но иногда симптомы бывают нетипичными. Самая опасная ситуация — усиление боли, появление её в покое, выраженная одышка, слабость или холодный пот. В таких случаях нужно срочно обращаться за медицинской помощью.

## Связанные документы
- [[DIAG-SYMPTOM-002]] — частое клиническое проявление
- [[DIAG-DIFDIAG-001]] — входит в дифференциальный ряд
- [[DIAG-EMERGENCY-001]] — острое осложнение / острая форма ишемического события
- [[DIAG-EXAM-001]] — базовый элемент общей оценки пациента

## Источники
1. Клинические рекомендации по хроническому коронарному синдрому, действующая редакция.
2. Руководства Европейского общества кардиологов по хроническим коронарным синдромам.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/diseases/diag_disease_migraine.md

```markdown
---
id: "DIAG-DISEASE-005"
title: "Мигрень"
domain: "diag"
category: "disease"
icd_10: "G43"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "nervous"
tags:
  - "migraine"
  - "headache"
  - "nervous"
  - "pain"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "neurologist"
age_group:
  - "adult"
  - "adolescent"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-001"
  - "DIAG-DIFDIAG-002"
  - "DIAG-REDFLAG-002"
relations:
  - target: "DIAG-SYMPTOM-001"
    type: "has_symptom"
    description: "головная боль является ведущим проявлением"
  - target: "DIAG-DIFDIAG-002"
    type: "differentiates_from"
    description: "требуется отличать от вторичных головных болей"
  - target: "DIAG-REDFLAG-002"
    type: "red_flag_for"
    description: "внезапная сильнейшая боль не типична и требует исключения опасных причин"
sources:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения, действующая редакция."
  - "Клинические рекомендации по мигрени, действующая редакция."
  - "Руководства по неврологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по мигрени"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Мигрень

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Мигрень — первичное неврологическое заболевание, проявляющееся повторными приступами головной боли и сопутствующими симптомами. МКБ-10: G43.

## Эпидемиология
- часто начинается в молодом возрасте;
- чаще встречается у женщин;
- может значительно снижать качество жизни при частых приступах.

## Этиология и патогенез
Мигрень связана с наследственной предрасположенностью, нейроваскулярными механизмами и изменением обработки болевых сигналов. Триггерами могут быть недосыпание, стресс, некоторые продукты, гормональные факторы, яркий свет и изменение режима.

## Клиническая картина
- повторные приступы [[DIAG-SYMPTOM-001]] головной боли;
- часто односторонняя пульсирующая боль;
- усиление при физической активности;
- тошнота, светобоязнь, звукобоязнь;
- у части пациентов — аура.

## 🚩 «Красные флаги»
- внезапная сильнейшая головная боль;
- новый характер боли у пациента старшего возраста;
- неврологический дефицит;
- головная боль с лихорадкой, ригидностью затылочных мышц;
- прогрессирующее ухудшение.

## Диагностика
Диагноз мигрени обычно основывается на клинических критериях, анамнезе приступов и исключении вторичных причин при наличии красных флагов.

## Дифференциальная диагностика
Проводится с головной болью напряжения, кластерной головной болью, гипертоническим кризом, внутричерепными процессами, менингитом и сосудистыми катастрофами.

## Лечение (обзор)
В БЗ MedAssist лечение не назначается. Карточка указывает, что терапия подбирается врачом с учётом частоты приступов, противопоказаний и клинических рекомендаций.

## Профилактика
- выявление индивидуальных триггеров;
- регулярный сон;
- контроль стрессовых факторов;
- обращение к врачу при частых или изменившихся приступах.

## Информация для пациента
Если головная боль стала внезапной, необычно сильной, сопровождается слабостью в конечностях, нарушением речи, температурой или нарушением сознания, требуется срочная помощь.

## Связанные документы
- [[DIAG-SYMPTOM-001]] — головная боль.
- [[DIAG-DIFDIAG-002]] — дифференциальная диагностика головной боли.
- [[DIAG-REDFLAG-002]] — внезапная сильнейшая головная боль.

```

## kb/diagnostics/diseases/diag_disease_pneumonia.md

```markdown
---
id: "DIAG-DISEASE-003"
title: "Пневмония"
domain: "diag"
category: "disease"
icd_10: "J12-J18"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
tags:
  - "pneumonia"
  - "respiratory"
  - "infection"
  - "fever"
  - "dyspnea"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-SYMPTOM-004"
  - "DIAG-EXAM-003"
  - "DIAG-EXAM-004"
  - "DIAG-DIFDIAG-003"
  - "DIAG-REDFLAG-003"
relations:
  - target: "DIAG-SYMPTOM-003"
    type: "has_symptom"
    description: "одышка может быть проявлением пневмонии"
  - target: "DIAG-SYMPTOM-004"
    type: "has_symptom"
    description: "лихорадка является частым инфекционным проявлением"
  - target: "DIAG-EXAM-003"
    type: "diagnosed_by"
    description: "ОАК помогает оценить воспалительную реакцию"
  - target: "DIAG-EXAM-004"
    type: "diagnosed_by"
    description: "рентгенография помогает выявить инфильтративные изменения"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Пневмония

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Пневмония — острое инфекционно-воспалительное заболевание лёгочной ткани, обычно сопровождающееся респираторными симптомами и признаками воспалительной реакции. МКБ-10: J12–J18.

## Эпидемиология
- **Распространённость**: частая причина обращений за медицинской помощью и госпитализаций среди инфекций нижних дыхательных путей.
- **Группы риска**: пожилые пациенты, лица с хроническими заболеваниями, иммунокомпрометированные пациенты.
- **Факторы риска**: возраст, курение, ХОБЛ, сердечно-сосудистые заболевания, нарушение глотания, иммунодефицит.

## Этиология и патогенез
Пневмония развивается при проникновении инфекционного агента в нижние дыхательные пути и формировании воспалительного процесса в альвеолярной ткани. Клиническая картина зависит от возбудителя, возраста пациента, иммунного статуса и сопутствующих заболеваний.

## Классификация
- внебольничная;
- госпитальная;
- аспирационная;
- у иммунокомпрометированных пациентов.

## Клиническая картина
### Основные проявления
- кашель;
- [[DIAG-SYMPTOM-004]] лихорадка;
- [[DIAG-SYMPTOM-003]] одышка;
- боль в груди при дыхании;
- слабость, потливость.

### Данные осмотра
- учащение дыхания;
- локальные хрипы или ослабление дыхания;
- признаки гипоксемии при тяжёлом течении.

## 🚩 «Красные флаги»
- выраженная одышка, цианоз, спутанность сознания;
- низкое артериальное давление;
- быстрое ухудшение состояния;
- пожилой возраст и выраженная коморбидность.

## Диагностика
- клиническая оценка жалоб и осмотра;
- [[DIAG-EXAM-003]] общий анализ крови;
- [[DIAG-EXAM-004]] рентгенография органов грудной клетки;
- дополнительные лабораторные и микробиологические исследования по показаниям.

## Дифференциальная диагностика
Проводится с бронхитом, бронхиальной астмой, ТЭЛА, сердечной недостаточностью, туберкулёзом и другими причинами кашля, лихорадки и одышки.

## Лечение (обзор)
В БЗ MedAssist данный раздел носит обзорный характер. Выбор терапии, необходимость антибактериального лечения, место лечения и объём обследования определяет врач с учётом тяжести состояния и клинических рекомендаций.

## Прогноз
Зависит от возраста, сопутствующих заболеваний, тяжести состояния и своевременности медицинской помощи.

## Профилактика
- вакцинация по показаниям;
- отказ от курения;
- контроль хронических заболеваний;
- своевременное обращение при ухудшении состояния.

## Информация для пациента
При высокой температуре, одышке, боли в груди, спутанности сознания или выраженной слабости необходимо обратиться за медицинской помощью.

## Связанные документы
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-SYMPTOM-004]] — лихорадка.
- [[DIAG-EXAM-003]] — общий анализ крови.
- [[DIAG-EXAM-004]] — рентгенография органов грудной клетки.

```

## kb/diagnostics/diseases/index.md

```markdown
# Заболевания

Индекс раздела `diseases`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-DISEASE-001` | Артериальная гипертензия | `routine` | `DIAG-SYMPTOM-001`, `DIAG-SYMPTOM-002`, `DIAG-EXAM-001`, `DIAG-REDFLAG-001` | [diag_disease_hypertension.md](diag_disease_hypertension.md) |
| `DIAG-DISEASE-002` | Ишемическая болезнь сердца | `urgent` | `DIAG-SYMPTOM-002`, `DIAG-DIFDIAG-001`, `DIAG-EMERGENCY-001`, `DIAG-EXAM-001`, `DIAG-EXAM-002` | [diag_disease_ihd.md](diag_disease_ihd.md) |
| `DIAG-DISEASE-003` | Пневмония | `urgent` | `DIAG-SYMPTOM-003`, `DIAG-SYMPTOM-004`, `DIAG-EXAM-003`, `DIAG-EXAM-004`, `DIAG-DIFDIAG-003`, `DIAG-REDFLAG-003` | [diag_disease_pneumonia.md](diag_disease_pneumonia.md) |
| `DIAG-DISEASE-004` | Бронхиальная астма | `routine` | `DIAG-SYMPTOM-003`, `DIAG-DIFDIAG-003`, `DIAG-REDFLAG-003` | [diag_disease_asthma.md](diag_disease_asthma.md) |
| `DIAG-DISEASE-005` | Мигрень | `routine` | `DIAG-SYMPTOM-001`, `DIAG-DIFDIAG-002`, `DIAG-REDFLAG-002` | [diag_disease_migraine.md](diag_disease_migraine.md) |

```

## kb/diagnostics/emergencies/diag_emergency_acs.md

```markdown
---
id: "DIAG-EMERGENCY-001"
title: "Острый коронарный синдром"
domain: "diag"
category: "emergency"
icd_10: "I20.0; I21; I22"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "emergency"
  - "acs"
  - "cardiology"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "cardiologist"
  - "emergency_physician"
  - "icu"
age_group:
  - "adult"
  - "elderly"
evidence_level: "Ia"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-002"
  - "DIAG-DISEASE-002"
  - "DIAG-DIFDIAG-001"
  - "DIAG-EXAM-001"
  - "DIAG-EXAM-002"
relations:
  - target: "DIAG-SYMPTOM-002"
    type: "has_symptom"
    description: "часто проявляется болью или дискомфортом в груди"
  - target: "DIAG-DISEASE-002"
    type: "complicates"
    description: "связан с ишемической болезнью сердца"
  - target: "DIAG-EXAM-002"
    type: "diagnosed_by"
    description: "ЭКГ является ключевым первичным обследованием"
  - target: "DIAG-DIFDIAG-001"
    type: "differentiates_from"
    description: "требует дифференциальной диагностики с другими причинами боли"
sources:
  - "Клинические рекомендации по острому коронарному синдрому, действующая редакция."
  - "2023 ESC Guidelines for the management of acute coronary syndromes."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "2023 ESC Guidelines for the management of acute coronary syndromes"
  - "Клинические рекомендации по ОКС"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Острый коронарный синдром

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Состояние требует немедленного распознавания и передачи управления к алгоритмам экстренной помощи.

## Определение
Острый коронарный синдром (ОКС) — клинический синдром, объединяющий состояния, вызванные острым нарушением коронарного кровотока и требующие неотложной кардиологической оценки.

## Клиническая картина

### Основные проявления
- интенсивная загрудинная боль или выраженный дискомфорт;
- иррадиация в руку, плечо, шею, спину, нижнюю челюсть;
- одышка, холодный пот, слабость;
- тошнота, тревога, чувство страха;
- возможны атипичные варианты, особенно у пожилых и пациентов с диабетом.

### Данные осмотра
- бледность, потливость;
- тахикардия или брадикардия;
- нестабильное АД;
- признаки сердечной недостаточности;
- возможные аритмии.

## Диагностические критерии
ОКС предполагается при наличии типичной клинической картины ишемии миокарда в сочетании с изменениями ЭКГ и/или повышением кардиоспецифических маркёров. Диагностический контур должен быстро отличать ОКС от стабильной ИБС и некардиальной боли в груди.

## Ключевые обследования

| Метод | Цель | Ожидаемые находки |
|-------|------|-------------------|
| ЭКГ | Быстрое выявление ишемии / инфаркта | Подъём или депрессия ST, инверсия T, новые изменения |
| Тропонины | Подтверждение повреждения миокарда | Повышение кардиоспецифических маркёров |
| ЭхоКГ | Оценка локальной сократимости и осложнений | Нарушения локальной сократимости, снижение функции ЛЖ |
| [[DIAG-EXAM-001]] Измерение артериального давления | Оценка гемодинамики | Гипертензия, гипотензия или нестабильность |

## 🚩 Признаки критического течения
- 🔴 боль в груди с гемодинамической нестабильностью;
- 🔴 выраженная одышка, отёк лёгких;
- 🔴 тяжёлые аритмии;
- 🔴 снижение сознания или признаки кардиогенного шока.

## Дифференциальная диагностика

| Состояние | Общие признаки | Отличия |
|-----------|----------------|---------|
| [[DIAG-DISEASE-002]] Ишемическая болезнь сердца | Ишемический характер боли | При хронической ИБС нет признаков острого события |
| ТЭЛА | Боль в груди, одышка | Преобладает дыхательная симптоматика, другие диагностические маркеры |
| Расслоение аорты | Интенсивная боль в груди | Боль часто разрывающая, с сосудистыми признаками |
| ГЭРБ / мышечно-скелетная боль | Боль за грудиной | Нет типичных признаков острой ишемии |

## Тактическая значимость
- **Требуется**: экстренная помощь, срочная госпитализация, специализированная кардиологическая оценка.
- **Срочность**: немедленно.
- **Передача к протоколу**: к алгоритмам неотложной помощи при ОКС.

## Информация для пациента
ОКС — это потенциально жизнеугрожающее состояние. Если у человека появляется сильная или непривычная боль в груди, особенно с одышкой, холодным потом, слабостью или страхом, требуется немедленно вызывать скорую помощь.

## Связанные документы
- [[DIAG-SYMPTOM-002]] — ведущая жалоба
- [[DIAG-DISEASE-002]] — близкая нозологическая связь
- [[DIAG-DIFDIAG-001]] — обязательный элемент диагностического сопоставления
- [[DIAG-EXAM-001]] — часть первичной оценки гемодинамики

## Источники
1. Клинические рекомендации по острому коронарному синдрому, действующая редакция.
2. 2023 ESC Guidelines for the management of acute coronary syndromes.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/emergencies/diag_emergency_acute_respiratory_failure.md

```markdown
---
id: "DIAG-EMERGENCY-003"
title: "Острая дыхательная недостаточность"
domain: "diag"
category: "emergency"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
  - "cardiovascular"
  - "multisystem"
tags:
  - "emergency"
  - "respiratory_failure"
  - "dyspnea"
  - "cyanosis"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "pulmonologist"
  - "emergency_physician"
  - "icu"
  - "therapist"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-REDFLAG-003"
  - "DIAG-DISEASE-003"
  - "DIAG-DISEASE-004"
  - "DIAG-EXAM-004"
  - "DIAG-DIFDIAG-003"
relations:
  - target: "DIAG-SYMPTOM-003"
    type: "has_symptom"
    description: "выраженная одышка является ключевым проявлением"
  - target: "DIAG-REDFLAG-003"
    type: "red_flag_for"
    description: "цианоз и тяжёлая одышка являются красным флагом"
  - target: "DIAG-EXAM-004"
    type: "diagnosed_by"
    description: "помогает искать лёгочную причину"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по неотложным состояниям в пульмонологии"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Острая дыхательная недостаточность

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Неотложные состояния требуют немедленной клинической оценки и передачи управления к утверждённым алгоритмам помощи.

## Определение
Острая дыхательная недостаточность — состояние, при котором дыхательная система не обеспечивает адекватный газообмен, что приводит к гипоксемии и/или гиперкапнии.

## Клиническая картина
### Основные проявления
- выраженная [[DIAG-SYMPTOM-003]] одышка;
- учащённое или затруднённое дыхание;
- цианоз;
- тревога, возбуждение или угнетение сознания;
- участие вспомогательной мускулатуры в дыхании.

### Данные осмотра
- изменение частоты дыхания;
- снижение сатурации при наличии пульсоксиметрии;
- патологические дыхательные шумы;
- признаки истощения дыхательных усилий.

## Диагностические критерии
Подозрение формируется при сочетании выраженной дыхательной симптоматики, признаков гипоксии и ухудшения общего состояния. Окончательная оценка требует клинического осмотра и инструментально-лабораторных данных.

## Ключевые обследования
- оценка дыхания, сознания и гемодинамики;
- пульсоксиметрия при наличии;
- [[DIAG-EXAM-004]] рентгенография органов грудной клетки по показаниям;
- [[DIAG-EXAM-002]] ЭКГ при подозрении на кардиальную причину.

## 🚩 Признаки критического течения
- цианоз;
- спутанность сознания;
- невозможность говорить;
- признаки истощения дыхания;
- быстрое ухудшение.

## Дифференциальная диагностика
Проводится с тяжёлой пневмонией, приступом бронхиальной астмы, ТЭЛА, пневмотораксом, сердечной недостаточностью и другими причинами острой одышки.

## Тактическая значимость
Состояние требует срочной оценки и маршрутизации по алгоритмам неотложной помощи.

## Информация для пациента
При выраженной одышке, посинении губ, нарушении сознания или невозможности говорить необходимо срочно вызвать скорую помощь.

## Связанные документы
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-REDFLAG-003]] — выраженная одышка и цианоз.
- [[DIAG-DISEASE-003]] — пневмония.
- [[DIAG-DISEASE-004]] — бронхиальная астма.
- [[DIAG-DIFDIAG-003]] — дифференциальная диагностика одышки.

```

## kb/diagnostics/emergencies/diag_emergency_stroke.md

```markdown
---
id: "DIAG-EMERGENCY-002"
title: "Острое нарушение мозгового кровообращения"
domain: "diag"
category: "emergency"
icd_10: "I60-I64"
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "nervous"
  - "cardiovascular"
tags:
  - "emergency"
  - "stroke"
  - "neurology"
  - "redflag"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "neurologist"
  - "emergency_physician"
  - "icu"
  - "therapist"
age_group:
  - "adult"
  - "elderly"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-001"
  - "DIAG-REDFLAG-002"
  - "DIAG-DIFDIAG-002"
  - "DIAG-EXAM-001"
relations:
  - target: "DIAG-SYMPTOM-001"
    type: "associated_with"
    description: "может сопровождаться головной болью"
  - target: "DIAG-REDFLAG-002"
    type: "red_flag_for"
    description: "внезапная сильнейшая головная боль требует исключения сосудистой причины"
  - target: "DIAG-EXAM-001"
    type: "diagnosed_by"
    description: "контроль АД входит в первичную оценку"
sources:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения, действующая редакция."
  - "Клинические рекомендации по мигрени, действующая редакция."
  - "Руководства по неврологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Острое нарушение мозгового кровообращения

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Неотложные состояния требуют немедленной клинической оценки и передачи управления к утверждённым алгоритмам помощи.

## Определение
Острое нарушение мозгового кровообращения (ОНМК) — группа неотложных состояний, связанных с внезапным нарушением кровоснабжения головного мозга или внутричерепным кровоизлиянием. МКБ-10: I60–I64.

## Клиническая картина
### Основные проявления
- внезапная слабость или онемение лица, руки или ноги, чаще с одной стороны;
- нарушение речи или понимания речи;
- нарушение зрения;
- нарушение координации, головокружение;
- внезапная сильная головная боль;
- нарушение сознания.

### Данные осмотра
- очаговый неврологический дефицит;
- асимметрия лица;
- нарушения движений и чувствительности;
- изменение уровня сознания.

## Диагностические критерии
Подозрение формируется по внезапному появлению очаговых неврологических симптомов. Дальнейшая диагностика и маршрутизация выполняются по экстренному протоколу.

## Ключевые обследования
- оценка жизненных показателей;
- [[DIAG-EXAM-001]] измерение артериального давления;
- оценка неврологического статуса;
- нейровизуализация по решению врача и протоколу.

## 🚩 Признаки критического течения
- нарушение сознания;
- судороги;
- быстрое ухудшение;
- признаки дыхательной недостаточности;
- выраженное повышение или снижение АД в клинически значимом контексте.

## Дифференциальная диагностика
Проводится с гипогликемией, мигренью с аурой, эпилептическим приступом, интоксикацией, внутричерепными образованиями и другими причинами неврологического дефицита.

## Тактическая значимость
Карточка предназначена для раннего распознавания состояния, требующего срочной медицинской помощи. Она не используется для самостоятельной постановки диагноза.

## Информация для пациента
При внезапной слабости в конечностях, нарушении речи, перекосе лица, нарушении зрения или сознания необходимо немедленно вызвать скорую помощь.

## Связанные документы
- [[DIAG-SYMPTOM-001]] — головная боль.
- [[DIAG-REDFLAG-002]] — внезапная сильнейшая головная боль.
- [[DIAG-DIFDIAG-002]] — дифференциальная диагностика головной боли.
- [[DIAG-EXAM-001]] — измерение артериального давления.

```

## kb/diagnostics/emergencies/index.md

```markdown
# Неотложные состояния

Индекс раздела `emergencies`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-EMERGENCY-001` | Острый коронарный синдром | `emergency` | `DIAG-SYMPTOM-002`, `DIAG-DISEASE-002`, `DIAG-DIFDIAG-001`, `DIAG-EXAM-001`, `DIAG-EXAM-002` | [diag_emergency_acs.md](diag_emergency_acs.md) |
| `DIAG-EMERGENCY-002` | Острое нарушение мозгового кровообращения | `emergency` | `DIAG-SYMPTOM-001`, `DIAG-REDFLAG-002`, `DIAG-DIFDIAG-002`, `DIAG-EXAM-001` | [diag_emergency_stroke.md](diag_emergency_stroke.md) |
| `DIAG-EMERGENCY-003` | Острая дыхательная недостаточность | `emergency` | `DIAG-SYMPTOM-003`, `DIAG-REDFLAG-003`, `DIAG-DISEASE-003`, `DIAG-DISEASE-004`, `DIAG-EXAM-004`, `DIAG-DIFDIAG-003` | [diag_emergency_acute_respiratory_failure.md](diag_emergency_acute_respiratory_failure.md) |

```

## kb/diagnostics/exams/diag_exam_bp_measurement.md

```markdown
---
id: "DIAG-EXAM-001"
title: "Измерение артериального давления"
domain: "diag"
category: "exam"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "exam"
  - "blood_pressure"
  - "hypertension"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
  - "nursing"
age_group:
  - "all_ages"
evidence_level: "I"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-001"
  - "DIAG-SYMPTOM-001"
  - "DIAG-SYMPTOM-002"
  - "DIAG-REDFLAG-001"
relations:
  - target: "DIAG-DISEASE-001"
    type: "diagnosed_by"
    description: "метод используется для выявления и контроля АГ"
  - target: "DIAG-REDFLAG-001"
    type: "diagnosed_by"
    description: "помогает оценить тяжесть ситуации при кризе"
  - target: "DIAG-SYMPTOM-001"
    type: "assesses"
    description: "используется при головной боли и подозрении на повышение АД"
sources:
  - "Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция."
  - "2023 ESH Guidelines for the management of arterial hypertension."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "КР Минздрава РФ по артериальной гипертензии"
  - "2023 ESH Guidelines for the management of arterial hypertension"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Измерение артериального давления

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов.

## Определение
Измерение артериального давления — базовый неинвазивный метод оценки гемодинамики, позволяющий выявлять гипертензию, гипотензию и острые нарушения кровообращения.

## Назначение метода
Метод используется для первичной оценки сердечно-сосудистого статуса, подтверждения повышения АД, контроля лечения и выявления признаков неотложных состояний.

## Показания
- подозрение на артериальную гипертензию;
- головная боль, головокружение, слабость;
- боль в груди, одышка;
- контроль антигипертензивной терапии;
- профилактический осмотр;
- оценка пациента в неотложной ситуации.

## Диагностическая роль
Измерение АД является отправной точкой при диагностике АГ и обязательным элементом любой клинической оценки пациента. Повторные измерения помогают отличать случайное повышение давления от стойкой гипертензии. В острых ситуациях метод позволяет быстро выявить тяжёлую гипертензию, гипотензию и признаки гемодинамической нестабильности.

## Интерпретация результатов

| Результат / находка | Возможное значение |
|---------------------|-------------------|
| Стойкое повышение АД | Подозрение на артериальную гипертензию |
| Очень высокое АД на фоне симптомов | Подозрение на осложнённый гипертонический криз |
| Нормальное АД | Не исключает заболевание, но снижает вероятность тяжёлой гипертензии |
| Низкое АД | Возможна гипотензия, шок, острая сердечная патология |
| Значимая разница между руками | Требует уточнения сосудистой патологии и правильности измерения |

## Ограничения
- результат зависит от правильности техники;
- разовое измерение не всегда достаточно для постановки диагноза;
- тревога, боль, физическая нагрузка и кофеин могут искажать показатели;
- неправильно подобранная манжета снижает достоверность.

## Последовательность назначения
- **Когда назначается**: при первом контакте с пациентом, при жалобах и в рамках наблюдения.
- **Приоритетность**: обязательный.
- **После каких данных**: проводится до или параллельно с дальнейшей диагностикой.

## Связанные заболевания и симптомы
- [[DIAG-DISEASE-001]] Артериальная гипертензия
- [[DIAG-SYMPTOM-001]] Головная боль
- [[DIAG-SYMPTOM-002]] Боль в груди
- [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый

## Особенности у отдельных групп
- **Дети**: необходимы возрастные нормативы и подходящая манжета.
- **Пожилые**: желательно учитывать ортостатические реакции.
- **Беременные**: требуется повышенное внимание к гипертензивным состояниям.

## Связанные документы
- [[DIAG-DISEASE-001]] — основной метод подтверждения АГ
- [[DIAG-SYMPTOM-001]] — обязательный этап оценки жалобы
- [[DIAG-SYMPTOM-002]] — часть первичной оценки боли в груди
- [[DIAG-REDFLAG-001]] — ключевой метод выявления тяжёлой гипертензии

## Источники
1. Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция.
2. 2023 ESH Guidelines for the management of arterial hypertension.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/exams/diag_exam_cbc.md

```markdown
---
id: "DIAG-EXAM-003"
title: "Общий анализ крови"
domain: "diag"
category: "exam"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "hematologic"
  - "multisystem"
tags:
  - "cbc"
  - "exam"
  - "blood_test"
  - "infection"
  - "inflammation"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "gastroenterologist"
  - "emergency_physician"
  - "nursing"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "I"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-004"
  - "DIAG-SYMPTOM-005"
  - "DIAG-DISEASE-003"
relations:
  - target: "DIAG-SYMPTOM-004"
    type: "diagnosed_by"
    description: "используется при лихорадке для оценки воспалительной реакции"
  - target: "DIAG-DISEASE-003"
    type: "diagnosed_by"
    description: "помогает оценить инфекционно-воспалительные изменения"
  - target: "DIAG-SYMPTOM-005"
    type: "diagnosed_by"
    description: "может использоваться при боли в животе для оценки воспаления"
sources:
  - "Руководства по клинической диагностике и внутренним болезням."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Руководства по лабораторной диагностике"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Общий анализ крови

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Общий анализ крови (ОАК) — базовое лабораторное исследование, оценивающее клеточный состав крови и некоторые косвенные признаки воспаления, анемии, инфекции и других состояний.

## Назначение метода
ОАК используется как скрининговое и уточняющее исследование при широком спектре симптомов: лихорадке, слабости, одышке, боли, подозрении на инфекционный или воспалительный процесс.

## Показания
- [[DIAG-SYMPTOM-004]] лихорадка;
- подозрение на [[DIAG-DISEASE-003]] пневмонию;
- боль в животе при подозрении на воспалительный процесс;
- слабость, бледность, признаки анемии;
- контроль динамики по назначению врача.

## Диагностическая роль
ОАК не устанавливает диагноз самостоятельно, но помогает оценить выраженность воспалительной реакции, наличие анемии, тромбоцитопении, лейкоцитоза или лейкопении и определить необходимость дальнейшего обследования.

## Интерпретация результатов
| Результат / находка | Возможное значение |
|---|---|
| Лейкоцитоз | Возможный инфекционный или воспалительный процесс |
| Лейкопения | Возможна вирусная инфекция, лекарственное влияние или другие причины |
| Анемия | Возможная кровопотеря, дефицитные состояния или хроническое заболевание |
| Тромбоцитопения/тромбоцитоз | Требует интерпретации в клиническом контексте |

## Ограничения
Изменения в ОАК неспецифичны и требуют сопоставления с симптомами, осмотром и другими обследованиями.

## Связанные документы
- [[DIAG-SYMPTOM-004]] — лихорадка.
- [[DIAG-DISEASE-003]] — пневмония.
- [[DIAG-SYMPTOM-005]] — боль в животе.

```

## kb/diagnostics/exams/diag_exam_chest_xray.md

```markdown
---
id: "DIAG-EXAM-004"
title: "Рентгенография органов грудной клетки"
domain: "diag"
category: "exam"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
  - "cardiovascular"
tags:
  - "xray"
  - "chest_xray"
  - "exam"
  - "pneumonia"
  - "dyspnea"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "radiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "I"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-SYMPTOM-004"
  - "DIAG-DISEASE-003"
  - "DIAG-DIFDIAG-003"
relations:
  - target: "DIAG-DISEASE-003"
    type: "diagnosed_by"
    description: "помогает выявить инфильтративные изменения при пневмонии"
  - target: "DIAG-SYMPTOM-003"
    type: "diagnosed_by"
    description: "используется при оценке лёгочных причин одышки"
  - target: "DIAG-DIFDIAG-003"
    type: "diagnosed_by"
    description: "помогает дифференцировать лёгочные причины одышки"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых"
  - "Руководства по лучевой диагностике"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Рентгенография органов грудной клетки

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Рентгенография органов грудной клетки — инструментальный метод визуализации, позволяющий оценить лёгкие, плевральные полости, средостение и косвенные признаки некоторых сердечно-сосудистых изменений.

## Назначение метода
Метод применяется при подозрении на пневмонию, плевральный выпот, пневмоторакс, некоторые причины одышки и боли в груди.

## Показания
- кашель с лихорадкой;
- [[DIAG-SYMPTOM-003]] одышка;
- подозрение на [[DIAG-DISEASE-003]] пневмонию;
- боль в груди с дыхательной симптоматикой;
- оценка осложнений по назначению врача.

## Диагностическая роль
Рентгенография помогает выявить инфильтрацию лёгочной ткани, плевральный выпот, ателектаз, пневмоторакс и другие изменения. Результат требует интерпретации врачом с учётом симптомов и осмотра.

## Интерпретация результатов
| Находка | Возможное значение |
|---|---|
| Инфильтративные изменения | Возможная пневмония |
| Плевральный выпот | Воспалительная, сердечная, опухолевая или другая причина |
| Пневмоторакс | Неотложное состояние при соответствующей клинике |
| Отсутствие изменений | Не всегда исключает раннюю патологию |

## Ограничения
Метод имеет ограниченную чувствительность на ранних стадиях некоторых заболеваний и не заменяет клиническую оценку. При необходимости врач назначает дополнительные методы.

## Связанные документы
- [[DIAG-DISEASE-003]] — пневмония.
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-DIFDIAG-003]] — дифференциальная диагностика одышки.

```

## kb/diagnostics/exams/diag_exam_ecg.md

```markdown
---
id: "DIAG-EXAM-002"
title: "Электрокардиография"
domain: "diag"
category: "exam"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "ecg"
  - "exam"
  - "cardiology"
  - "chest_pain"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
  - "emergency_physician"
  - "nursing"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "I"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-002"
  - "DIAG-DISEASE-002"
  - "DIAG-EMERGENCY-001"
  - "DIAG-DIFDIAG-001"
relations:
  - target: "DIAG-SYMPTOM-002"
    type: "diagnosed_by"
    description: "используется при боли в груди"
  - target: "DIAG-EMERGENCY-001"
    type: "diagnosed_by"
    description: "ключевое первичное исследование при подозрении на ОКС"
  - target: "DIAG-DISEASE-002"
    type: "diagnosed_by"
    description: "помогает оценить признаки ишемии и нарушения ритма"
sources:
  - "Руководства по клинической диагностике и внутренним болезням."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по острому коронарному синдрому"
  - "Руководства по электрокардиографии"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Электрокардиография

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Электрокардиография (ЭКГ) — неинвазивный метод регистрации электрической активности сердца, используемый для оценки ритма, проводимости и признаков ишемии или перегрузки отделов сердца.

## Назначение метода
ЭКГ применяется при боли в груди, сердцебиении, обмороке, одышке, подозрении на острый коронарный синдром, аритмии и другие сердечно-сосудистые состояния.

## Показания
- [[DIAG-SYMPTOM-002]] боль в груди;
- подозрение на [[DIAG-EMERGENCY-001]] острый коронарный синдром;
- нарушения ритма;
- обморок или предобморочное состояние;
- одышка при возможной кардиальной причине.

## Диагностическая роль
ЭКГ помогает выявлять признаки ишемии миокарда, инфаркта, аритмий, блокад, гипертрофии и электролитных нарушений. При подозрении на ОКС результат ЭКГ интерпретируется в клиническом контексте и не заменяет врачебную оценку.

## Интерпретация результатов
| Находка | Возможное значение |
|---|---|
| Подъём или депрессия ST | Возможная ишемия/повреждение миокарда |
| Нарушение ритма | Аритмия, требующая оценки |
| Блокады проводимости | Нарушение проведения импульса |
| Неспецифические изменения | Требуют сопоставления с клиникой |

## Ограничения
Нормальная ЭКГ не всегда полностью исключает сердечную патологию. Результат должен оцениваться с жалобами, анамнезом, осмотром и дополнительными исследованиями.

## Последовательность назначения
При острой боли в груди ЭКГ относится к первичным исследованиям. При плановой оценке выполняется по клиническим показаниям.

## Связанные документы
- [[DIAG-SYMPTOM-002]] — боль в груди.
- [[DIAG-DISEASE-002]] — ишемическая болезнь сердца.
- [[DIAG-EMERGENCY-001]] — острый коронарный синдром.
- [[DIAG-DIFDIAG-001]] — дифференциальная диагностика боли в груди.

```

## kb/diagnostics/exams/index.md

```markdown
# Методы обследования

Индекс раздела `exams`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-EXAM-001` | Измерение артериального давления | `routine` | `DIAG-DISEASE-001`, `DIAG-SYMPTOM-001`, `DIAG-SYMPTOM-002`, `DIAG-REDFLAG-001` | [diag_exam_bp_measurement.md](diag_exam_bp_measurement.md) |
| `DIAG-EXAM-002` | Электрокардиография | `urgent` | `DIAG-SYMPTOM-002`, `DIAG-DISEASE-002`, `DIAG-EMERGENCY-001`, `DIAG-DIFDIAG-001` | [diag_exam_ecg.md](diag_exam_ecg.md) |
| `DIAG-EXAM-003` | Общий анализ крови | `routine` | `DIAG-SYMPTOM-004`, `DIAG-SYMPTOM-005`, `DIAG-DISEASE-003` | [diag_exam_cbc.md](diag_exam_cbc.md) |
| `DIAG-EXAM-004` | Рентгенография органов грудной клетки | `routine` | `DIAG-SYMPTOM-003`, `DIAG-SYMPTOM-004`, `DIAG-DISEASE-003`, `DIAG-DIFDIAG-003` | [diag_exam_chest_xray.md](diag_exam_chest_xray.md) |

```

## kb/diagnostics/index.md

```markdown
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

```

## kb/diagnostics/red_flags/diag_redflag_hypertensive_crisis.md

```markdown
---
id: "DIAG-REDFLAG-001"
title: "Гипертонический криз осложнённый"
domain: "diag"
category: "redflag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
  - "multisystem"
tags:
  - "redflag"
  - "hypertensive_crisis"
  - "emergency"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-001"
  - "DIAG-SYMPTOM-001"
  - "DIAG-SYMPTOM-002"
  - "DIAG-EXAM-001"
relations:
  - target: "DIAG-DISEASE-001"
    type: "red_flag_for"
    description: "опасное состояние у пациента с АГ"
  - target: "DIAG-SYMPTOM-001"
    type: "associated_with"
    description: "может проявляться головной болью"
  - target: "DIAG-EXAM-001"
    type: "diagnosed_by"
    description: "требует контроля уровня АД"
sources:
  - "Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция."
  - "2023 ESH Guidelines for the management of arterial hypertension."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "КР Минздрава РФ по артериальной гипертензии"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Гипертонический криз осложнённый

> ⚕️ **Дисклеймер**: Информация носит справочный характер. Красный флаг указывает на необходимость срочной клинической оценки.

## Определение
Осложнённый гипертонический криз — клиническая ситуация, при которой значительное повышение артериального давления сопровождается признаками острого поражения органов-мишеней и требует неотложной медицинской помощи.

## Клиническое значение
Данный красный флаг указывает не просто на высокие цифры АД, а на риск быстрого необратимого повреждения мозга, сердца, почек, аорты или сетчатки. Ключевым является наличие симптомов или объективных признаков органного поражения.

## Когда возникает
- на фоне длительно неконтролируемой АГ;
- при резкой отмене терапии;
- при выраженном психоэмоциональном или физическом стрессе;
- при вторичной гипертензии;
- при развитии ОКС, инсульта, острой сердечной недостаточности, расслаивающей аневризмы аорты.

## Возможные ассоциированные состояния
- [[DIAG-DISEASE-001]] Артериальная гипертензия
- [[DIAG-SYMPTOM-001]] Головная боль
- [[DIAG-SYMPTOM-002]] Боль в груди

## Необходимые действия
- срочно оценить неврологический статус, наличие боли в груди, одышки, нарушения зрения;
- повторно измерить АД по корректной методике;
- выполнить ЭКГ и базовую лабораторную оценку по показаниям;
- организовать экстренное направление / госпитализацию при признаках органного поражения.

## Срочность
- **Уровень срочности**: emergency
- **К кому направлять**: скорая помощь, приёмное отделение, кардиолог/невролог/реаниматолог по ситуации
- **Что исключать в первую очередь**: инсульт, ОКС, отёк лёгких, расслаивание аорты, острую почечную дисфункцию

## Связанные обследования
- [[DIAG-EXAM-001]] Измерение артериального давления
- ЭКГ
- Биохимический анализ крови
- Оценка функции почек
- Неврологический осмотр / нейровизуализация по показаниям

## Связанные документы
- [[DIAG-DISEASE-001]] — опасное осложнение основного заболевания
- [[DIAG-SYMPTOM-001]] — частое клиническое проявление
- [[DIAG-SYMPTOM-002]] — возможный признак кардиоваскулярного осложнения
- [[DIAG-EXAM-001]] — обязательный метод первичной оценки

## Источники
1. Клинические рекомендации Минздрава РФ «Артериальная гипертензия у взрослых», действующая редакция.
2. 2023 ESH Guidelines for the management of arterial hypertension.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/red_flags/diag_redflag_severe_dyspnea_cyanosis.md

```markdown
---
id: "DIAG-REDFLAG-003"
title: "Выраженная одышка и цианоз"
domain: "diag"
category: "redflag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
  - "cardiovascular"
  - "multisystem"
tags:
  - "redflag"
  - "dyspnea"
  - "cyanosis"
  - "emergency"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "emergency_physician"
  - "icu"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-003"
  - "DIAG-DISEASE-003"
  - "DIAG-DISEASE-004"
  - "DIAG-EMERGENCY-003"
  - "DIAG-DIFDIAG-003"
relations:
  - target: "DIAG-SYMPTOM-003"
    type: "red_flag_for"
    description: "опасный вариант одышки"
  - target: "DIAG-EMERGENCY-003"
    type: "red_flag_for"
    description: "может указывать на дыхательную недостаточность"
  - target: "DIAG-DIFDIAG-003"
    type: "differentiates_from"
    description: "учитывается в дифференциальной диагностике одышки"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по неотложным состояниям в пульмонологии"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Выраженная одышка и цианоз

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Неотложные состояния требуют немедленной клинической оценки и передачи управления к утверждённым алгоритмам помощи.

## Определение
Выраженная одышка и цианоз — сочетание затруднённого дыхания с синюшной окраской губ, кожи или слизистых, указывающее на возможное нарушение оксигенации.

## Клиническое значение
Красный флаг отражает риск острой дыхательной недостаточности, тяжёлой бронхообструкции, пневмонии тяжёлого течения, ТЭЛА, пневмоторакса, сердечной недостаточности или другого опасного состояния.

## Когда возникает
- при тяжёлой пневмонии;
- при тяжёлом приступе бронхиальной астмы;
- при острой дыхательной недостаточности;
- при кардиальных и сосудистых причинах одышки.

## Возможные ассоциированные состояния
- [[DIAG-EMERGENCY-003]] Острая дыхательная недостаточность.
- [[DIAG-DISEASE-003]] Пневмония.
- [[DIAG-DISEASE-004]] Бронхиальная астма.

## Необходимые действия
- срочная оценка жизненных показателей;
- оценка дыхания, сознания, цвета кожных покровов;
- пульсоксиметрия при наличии;
- вызов экстренной помощи или срочная маршрутизация по клинической ситуации.

## Срочность
Уровень срочности: **emergency**.

## Связанные обследования
- [[DIAG-EXAM-004]] Рентгенография органов грудной клетки.
- [[DIAG-EXAM-002]] Электрокардиография при подозрении на кардиальную причину.

## Связанные документы
- [[DIAG-SYMPTOM-003]] — одышка.
- [[DIAG-EMERGENCY-003]] — острая дыхательная недостаточность.
- [[DIAG-DIFDIAG-003]] — дифференциальная диагностика одышки.

```

## kb/diagnostics/red_flags/diag_redflag_thunderclap_headache.md

```markdown
---
id: "DIAG-REDFLAG-002"
title: "Внезапная сильнейшая головная боль"
domain: "diag"
category: "redflag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "nervous"
  - "multisystem"
tags:
  - "redflag"
  - "headache"
  - "stroke"
  - "emergency"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "therapist"
  - "neurologist"
  - "emergency_physician"
  - "icu"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IIa"
recommendation_class: "I"
related:
  - "DIAG-SYMPTOM-001"
  - "DIAG-DISEASE-005"
  - "DIAG-EMERGENCY-002"
  - "DIAG-DIFDIAG-002"
relations:
  - target: "DIAG-SYMPTOM-001"
    type: "red_flag_for"
    description: "опасный вариант головной боли"
  - target: "DIAG-EMERGENCY-002"
    type: "red_flag_for"
    description: "требует исключения сосудистой катастрофы"
  - target: "DIAG-DIFDIAG-002"
    type: "differentiates_from"
    description: "учитывается в дифференциальной диагностике головной боли"
sources:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения, действующая редакция."
  - "Клинические рекомендации по мигрени, действующая редакция."
  - "Руководства по неврологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по острому нарушению мозгового кровообращения"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Внезапная сильнейшая головная боль

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Неотложные состояния требуют немедленной клинической оценки и передачи управления к утверждённым алгоритмам помощи.

## Определение
Внезапная сильнейшая головная боль — остро возникшая интенсивная головная боль, часто описываемая как «самая сильная в жизни». Такой признак рассматривается как красный флаг и требует исключения опасных причин.

## Клиническое значение
Симптом может быть связан с сосудистыми катастрофами, внутричерепным кровоизлиянием, менингитом, тромбозом венозных синусов и другими состояниями, требующими срочной диагностики.

## Когда возникает
- на фоне физического усилия или внезапно в покое;
- вместе с нарушением сознания, рвотой, судорогами;
- с неврологическим дефицитом;
- при изменении характера ранее известных головных болей.

## Возможные ассоциированные состояния
- [[DIAG-EMERGENCY-002]] Острое нарушение мозгового кровообращения.
- Субарахноидальное кровоизлияние.
- Менингит/энцефалит.
- Гипертонический криз с поражением органов-мишеней.

## Необходимые действия
- срочная клиническая оценка;
- оценка неврологического статуса;
- контроль АД и жизненных показателей;
- решение вопроса о неотложной визуализации и маршрутизации врачом.

## Срочность
Уровень срочности: **emergency**.

## Связанные документы
- [[DIAG-SYMPTOM-001]] — головная боль.
- [[DIAG-DIFDIAG-002]] — дифференциальная диагностика головной боли.
- [[DIAG-EMERGENCY-002]] — острое нарушение мозгового кровообращения.

```

## kb/diagnostics/red_flags/index.md

```markdown
# Красные флаги

Индекс раздела `red_flags`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-REDFLAG-001` | Гипертонический криз осложнённый | `emergency` | `DIAG-DISEASE-001`, `DIAG-SYMPTOM-001`, `DIAG-SYMPTOM-002`, `DIAG-EXAM-001` | [diag_redflag_hypertensive_crisis.md](diag_redflag_hypertensive_crisis.md) |
| `DIAG-REDFLAG-002` | Внезапная сильнейшая головная боль | `emergency` | `DIAG-SYMPTOM-001`, `DIAG-DISEASE-005`, `DIAG-EMERGENCY-002`, `DIAG-DIFDIAG-002` | [diag_redflag_thunderclap_headache.md](diag_redflag_thunderclap_headache.md) |
| `DIAG-REDFLAG-003` | Выраженная одышка и цианоз | `emergency` | `DIAG-SYMPTOM-003`, `DIAG-DISEASE-003`, `DIAG-DISEASE-004`, `DIAG-EMERGENCY-003`, `DIAG-DIFDIAG-003` | [diag_redflag_severe_dyspnea_cyanosis.md](diag_redflag_severe_dyspnea_cyanosis.md) |

```

## kb/diagnostics/symptoms/diag_symptom_abdominal_pain.md

```markdown
---
id: "DIAG-SYMPTOM-005"
title: "Боль в животе"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "gastrointestinal"
  - "multisystem"
tags:
  - "abdominal_pain"
  - "symptom"
  - "pain"
  - "urgent"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "gastroenterologist"
  - "surgeon"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-EXAM-003"
relations:
  - target: "DIAG-EXAM-003"
    type: "diagnosed_by"
    description: "ОАК может использоваться для оценки воспалительной реакции"
sources:
  - "Руководства по клинической диагностике и внутренним болезням."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Руководства по внутренним болезням и неотложной хирургии"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Боль в животе

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Боль в животе — симптом, связанный с патологией органов брюшной полости, забрюшинного пространства, сосудов, мочеполовой системы или отражённой болью из других областей.

## Механизм
Боль может быть висцеральной, соматической, отражённой или смешанной. Для интерпретации важны локализация, характер, связь с едой, движением, дефекацией, мочеиспусканием, температурой и общим состоянием.

## Характеристики
- **Локализация**: эпигастрий, правое/левое подреберье, околопупочная область, подвздошные области.
- **Характер**: спастическая, постоянная, кинжальная, жгучая, распирающая.
- **Динамика**: внезапная, нарастающая, рецидивирующая.
- **Сопутствующие проявления**: тошнота, рвота, диарея, задержка стула, лихорадка, желтуха, кровь в стуле.

## Клиническое значение
Боль в животе требует разделения на вероятно функциональные причины и состояния, требующие срочной хирургической или терапевтической оценки.

## 🚩 «Красные флаги»
- внезапная очень сильная боль;
- напряжение мышц передней брюшной стенки;
- повторная рвота, признаки обезвоживания;
- кровь в рвоте или стуле;
- лихорадка с выраженной болью;
- падение АД, обморок, выраженная слабость.

## Дифференциально-диагностические критерии
| Признак | Возможное направление поиска |
|---|---|
| Боль в правой подвздошной области | Острый аппендицит и другие хирургические причины |
| Боль после еды, изжога | Гастроэзофагеальные и желудочные причины |
| Опоясывающая боль | Панкреатическая причина |
| Боль + мочевые симптомы | Урологическая причина |

## Диагностические направления
- оценка локализации, перитонеальных признаков и жизненных показателей;
- [[DIAG-EXAM-003]] Общий анализ крови;
- биохимические показатели, анализ мочи, УЗИ или КТ по клиническим показаниям.

## Информация для пациента
При внезапной сильной боли, напряжении живота, крови в стуле, повторной рвоте или ухудшении общего состояния необходима срочная медицинская оценка.

## Связанные документы
- [[DIAG-EXAM-003]] — общий анализ крови как базовое лабораторное исследование.

```

## kb/diagnostics/symptoms/diag_symptom_chest_pain.md

```markdown
---
id: "DIAG-SYMPTOM-002"
title: "Боль в груди"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
  - "respiratory"
  - "multisystem"
tags:
  - "chest_pain"
  - "symptom"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "cardiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-002"
  - "DIAG-DIFDIAG-001"
  - "DIAG-EMERGENCY-001"
  - "DIAG-REDFLAG-001"
  - "DIAG-EXAM-001"
  - "DIAG-EXAM-002"
relations:
  - target: "DIAG-DISEASE-002"
    type: "associated_with"
    description: "ИБС является одной из ключевых причин боли в груди"
  - target: "DIAG-EMERGENCY-001"
    type: "red_flag_for"
    description: "боль в груди может быть проявлением ОКС"
  - target: "DIAG-DIFDIAG-001"
    type: "differentiates_from"
    description: "связанный документ по дифференциальной диагностике боли в груди"
  - target: "DIAG-EXAM-001"
    type: "diagnosed_by"
    description: "АД входит в первичную оценку пациента"
  - target: "DIAG-EXAM-002"
    type: "diagnosed_by"
    description: "ЭКГ является ключевым методом при подозрении на кардиальную причину"
sources:
  - "Руководства по внутренним болезням и клинической диагностике."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по хроническому коронарному синдрому"
  - "Клинические рекомендации по острому коронарному синдрому"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Боль в груди

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
Боль в груди — один из ведущих симптомов в диагностическом контуре MedAssist, требующий оценки характера боли, срочности ситуации и исключения жизнеугрожающих причин.

## Механизм
Боль может быть связана с ишемией миокарда, раздражением плевры, мышечно-скелетными причинами, патологией пищевода, а также сосудистыми и психогенными механизмами. Для клинической интерпретации принципиальны локализация, иррадиация, связь с нагрузкой, дыханием, движением и сопутствующими симптомами.

## Характеристики
- **Локализация**: загрудинная, слева, справа, диффузная.
- **Интенсивность**: от умеренной до крайне выраженной.
- **Динамика**: внезапная, постепенная, приступообразная, постоянная.
- **Сопутствующие проявления**: одышка, потливость, слабость, сердцебиение, кашель, тошнота, страх, повышение АД.

## Клиническое значение
Боль в груди — симптом с высокой клинической значимостью, поскольку может указывать как на относительно доброкачественные состояния, так и на ОКС, аортальную катастрофу, тромбоэмболию лёгочной артерии, пневмоторакс и другие опасные патологии.

## Ассоциированные заболевания
- [[DIAG-DISEASE-002]] Ишемическая болезнь сердца
- [[DIAG-EMERGENCY-001]] Острый коронарный синдром
- ГЭРБ
- Плеврит
- Мышечно-скелетная боль грудной клетки

## 🚩 «Красные флаги»
- 🔴 Давящая или жгучая загрудинная боль с одышкой и холодным потом → срочно исключать ОКС.
- 🔴 Внезапная интенсивная боль в груди с ухудшением состояния → срочная оценка на жизнеугрожающее состояние.
- 🔴 Боль в груди на фоне очень высокого АД → исключать осложнённый гипертонический криз.
- 🔴 Боль с синкопе, выраженной слабостью или гемодинамической нестабильностью → экстренная помощь.

## Дифференциально-диагностические критерии

| Состояние / заболевание | Общие признаки | Отличительные признаки |
|-------------------------|----------------|------------------------|
| [[DIAG-DISEASE-002]] Ишемическая болезнь сердца | Загрудинная боль, связь с нагрузкой | Стереотипность симптомов, ишемический характер |
| [[DIAG-EMERGENCY-001]] Острый коронарный синдром | Боль ишемического характера | Боль в покое, длительность, системные симптомы, неотложность |
| Плеврит | Боль в груди | Усиливается при дыхании и кашле |
| Мышечно-скелетная боль | Боль в грудной клетке | Усиливается при движении, пальпации |
| ГЭРБ | Жжение за грудиной | Связь с приёмом пищи и положением тела |

## Диагностические направления

### Обязательные обследования
- ЭКГ
- Оценка витальных функций
- [[DIAG-EXAM-001]] Измерение артериального давления

### Дополнительные обследования
- Тропонины
- Рентгенография / КТ по показаниям
- ЭхоКГ
- Лабораторные исследования в зависимости от клинической гипотезы

## Особенности у отдельных групп
- **Дети**: ишемическая природа боли встречается реже; чаще функциональные и мышечно-скелетные причины.
- **Пожилые**: выше вероятность кардиальной причины и атипичного течения.
- **Беременные**: требует осторожной оценки кардиопульмональных причин и гемодинамики.

## Информация для пациента
Боль в груди не всегда означает болезнь сердца, но именно сердечные причины нужно исключать в первую очередь, если есть одышка, слабость, холодный пот, страх, резкая слабость или очень высокое давление. При таких симптомах нельзя откладывать обращение за медицинской помощью.

## Связанные документы
- [[DIAG-DISEASE-002]] — возможная нозологическая причина
- [[DIAG-DIFDIAG-001]] — ведущий симптом для сравнения причин
- [[DIAG-EMERGENCY-001]] — опасное состояние, которое нужно исключать в первую очередь
- [[DIAG-REDFLAG-001]] — возможный контекст тяжёлой гипертензии
- [[DIAG-EXAM-001]] — часть первичной оценки

## Источники
1. Руководства по внутренним болезням и клинической диагностике.
2. Клинические рекомендации по соответствующему профилю, действующая редакция.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/symptoms/diag_symptom_dyspnea.md

```markdown
---
id: "DIAG-SYMPTOM-003"
title: "Одышка"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "respiratory"
  - "cardiovascular"
  - "multisystem"
tags:
  - "dyspnea"
  - "symptom"
  - "respiratory"
  - "cardiovascular"
  - "emergency"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "cardiologist"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-003"
  - "DIAG-DISEASE-004"
  - "DIAG-EMERGENCY-003"
  - "DIAG-EXAM-002"
  - "DIAG-EXAM-004"
  - "DIAG-DIFDIAG-003"
  - "DIAG-REDFLAG-003"
relations:
  - target: "DIAG-DISEASE-003"
    type: "associated_with"
    description: "одышка может быть проявлением пневмонии"
  - target: "DIAG-DISEASE-004"
    type: "associated_with"
    description: "одышка характерна для бронхиальной астмы"
  - target: "DIAG-EMERGENCY-003"
    type: "red_flag_for"
    description: "выраженная одышка может указывать на дыхательную недостаточность"
  - target: "DIAG-EXAM-004"
    type: "diagnosed_by"
    description: "рентгенография грудной клетки помогает оценить лёгочную причину"
  - target: "DIAG-DIFDIAG-003"
    type: "differentiates_from"
    description: "требует дифференциальной оценки причин одышки"
sources:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых, действующая редакция."
  - "GINA Global Strategy for Asthma Management and Prevention, действующая редакция."
  - "Руководства по пульмонологии и внутренним болезням."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых"
  - "GINA Global Strategy for Asthma Management and Prevention"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Одышка

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Одышка — субъективное ощущение затруднённого, учащённого или недостаточного дыхания, которое может возникать при заболеваниях дыхательной, сердечно-сосудистой, гематологической и других систем.

## Механизм
Одышка формируется при несоответствии между потребностью организма в вентиляции и возможностями дыхательной системы. Возможные механизмы включают нарушение газообмена, бронхообструкцию, снижение растяжимости лёгких, сердечную недостаточность, анемию, метаболические нарушения и тревожные реакции.

## Характеристики
- **Начало**: внезапное, постепенное, приступообразное.
- **Связь с нагрузкой**: только при физической нагрузке, в покое, ночью, в положении лёжа.
- **Сопутствующие проявления**: кашель, боль в груди, свистящее дыхание, лихорадка, цианоз, сердцебиение.
- **Динамика**: нарастающая, стабильная, рецидивирующая.

## Клиническое значение
Одышка требует оценки срочности, поскольку может отражать как хроническое заболевание, так и жизнеугрожающее состояние. В диагностическом контуре MedAssist одышка связана с пневмонией, бронхиальной астмой, острыми кардиальными состояниями и дыхательной недостаточностью.

## Ассоциированные заболевания
- [[DIAG-DISEASE-003]] Пневмония.
- [[DIAG-DISEASE-004]] Бронхиальная астма.
- Ишемическая болезнь сердца и сердечная недостаточность как возможные кардиальные причины.
- Анемия, тревожные расстройства и метаболические нарушения как внесистемные причины.

## 🚩 «Красные флаги»
- одышка в покое или невозможность говорить полными фразами;
- цианоз, спутанность сознания, выраженная слабость;
- боль в груди, кровохарканье, выраженная тахикардия;
- внезапное начало симптома;
- снижение сатурации при наличии пульсоксиметрии.

## Дифференциально-диагностические критерии
| Признак | Возможное направление поиска |
|---|---|
| Лихорадка, кашель, хрипы | Инфекционная причина, пневмония |
| Свистящее дыхание, приступы | Бронхообструкция, астма |
| Боль в груди, факторы риска | Кардиальная причина |
| Внезапное начало | ТЭЛА, пневмоторакс, острое состояние |

## Диагностические направления
- оценка частоты дыхания, пульса, АД и общего состояния;
- аускультация лёгких и сердца;
- [[DIAG-EXAM-002]] Электрокардиография при подозрении на кардиальную причину;
- [[DIAG-EXAM-004]] Рентгенография органов грудной клетки при подозрении на лёгочную причину;
- общий анализ крови и маркеры воспаления по клиническим показаниям.

## Информация для пациента
При выраженной одышке, боли в груди, посинении губ, спутанности сознания или резком ухудшении состояния необходимо срочно обратиться за медицинской помощью.

## Связанные документы
- [[DIAG-DISEASE-003]] — пневмония как возможная причина.
- [[DIAG-DISEASE-004]] — бронхиальная астма как возможная причина.
- [[DIAG-EMERGENCY-003]] — острая дыхательная недостаточность.
- [[DIAG-DIFDIAG-003]] — дифференциальная диагностика одышки.

```

## kb/diagnostics/symptoms/diag_symptom_fever.md

```markdown
---
id: "DIAG-SYMPTOM-004"
title: "Лихорадка"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "multisystem"
  - "respiratory"
  - "immune"
tags:
  - "fever"
  - "symptom"
  - "infection"
  - "inflammation"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "pulmonologist"
  - "pediatrician"
  - "emergency_physician"
age_group:
  - "adult"
  - "elderly"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-003"
  - "DIAG-EXAM-003"
  - "DIAG-EXAM-004"
relations:
  - target: "DIAG-DISEASE-003"
    type: "associated_with"
    description: "лихорадка может сопровождать пневмонию"
  - target: "DIAG-EXAM-003"
    type: "diagnosed_by"
    description: "ОАК помогает оценить признаки воспаления"
  - target: "DIAG-EXAM-004"
    type: "diagnosed_by"
    description: "при дыхательных симптомах помогает искать лёгочную причину"
sources:
  - "Руководства по клинической диагностике и внутренним болезням."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "Клинические рекомендации по внебольничной пневмонии у взрослых"
last_medical_review: "2026-04-30"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-30"
date_updated: "2026-05-03"
status: "medical_review"
disclaimer: true
---

# Лихорадка

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению и не заменяет клиническое решение врача.

## Определение
Лихорадка — повышение температуры тела выше индивидуальной нормы вследствие перестройки терморегуляции, чаще всего при инфекционном или воспалительном процессе.

## Механизм
Температурная реакция связана с действием пирогенов и медиаторов воспаления, которые изменяют установочную точку терморегуляции. Лихорадка может быть защитной реакцией, но при выраженности или сочетании с опасными признаками требует срочной оценки.

## Характеристики
- **Высота температуры**: субфебрильная, фебрильная, высокая.
- **Длительность**: острая, затяжная, рецидивирующая.
- **Сопутствующие проявления**: кашель, боль в груди, одышка, сыпь, боль в животе, менингеальные симптомы.
- **Ответ на жаропонижающие**: временное снижение или отсутствие эффекта.

## Клиническое значение
Лихорадка сама по себе не указывает на конкретное заболевание. В БЗ MedAssist она используется как симптом, направляющий к поиску инфекционного, воспалительного, аутоиммунного или опухолевого процесса.

## Ассоциированные заболевания
- [[DIAG-DISEASE-003]] Пневмония.
- Инфекции верхних дыхательных путей.
- Инфекции мочевыводящих путей.
- Воспалительные заболевания различной локализации.

## 🚩 «Красные флаги»
- лихорадка с нарушением сознания, судорогами или ригидностью затылочных мышц;
- лихорадка с выраженной одышкой, цианозом, падением АД;
- лихорадка у иммунокомпрометированного пациента;
- длительная лихорадка неясного происхождения;
- сочетание с геморрагической сыпью.

## Диагностические направления
- оценка очага инфекции по жалобам и осмотру;
- [[DIAG-EXAM-003]] Общий анализ крови;
- [[DIAG-EXAM-004]] Рентгенография грудной клетки при кашле, боли в груди или одышке;
- дополнительные обследования по клинической ситуации.

## Информация для пациента
При высокой температуре с одышкой, спутанностью сознания, сильной слабостью, сыпью или болью в груди необходимо обратиться за медицинской помощью.

## Связанные документы
- [[DIAG-DISEASE-003]] — пневмония.
- [[DIAG-EXAM-003]] — общий анализ крови.
- [[DIAG-EXAM-004]] — рентгенография органов грудной клетки.

```

## kb/diagnostics/symptoms/diag_symptom_headache.md

```markdown
---
id: "DIAG-SYMPTOM-001"
title: "Головная боль"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "nervous"
  - "multisystem"
tags:
  - "headache"
  - "symptom"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
  - "neurologist"
age_group:
  - "adult"
  - "all_ages"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-DISEASE-001"
  - "DIAG-REDFLAG-001"
  - "DIAG-EXAM-001"
  - "DIAG-DIFDIAG-002"
relations:
  - target: "DIAG-DISEASE-001"
    type: "associated_with"
    description: "головная боль может сопровождать повышение артериального давления"
  - target: "DIAG-REDFLAG-001"
    type: "red_flag_for"
    description: "головная боль при признаках поражения органов-мишеней требует срочной оценки"
  - target: "DIAG-EXAM-001"
    type: "diagnosed_by"
    description: "измерение артериального давления входит в первичную оценку"
  - target: "DIAG-DIFDIAG-002"
    type: "differentiates_from"
    description: "связанный документ по дифференциальной диагностике головной боли"
sources:
  - "Руководства по внутренним болезням и клинической диагностике."
  - "Клинические рекомендации по соответствующему профилю, действующая редакция."
  - "Техническое задание к БЗ MedAssist, раздел 3.1."
clinical_guidelines:
  - "КР по артериальной гипертензии"
last_medical_review: "2026-04-09"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "2026-04-08"
date_updated: "2026-04-09"
status: "medical_review"
disclaimer: true
---

# Головная боль

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
Головная боль — распространённый симптом, отражающий широкий спектр состояний: от функциональных и доброкачественных до жизнеугрожающих.

## Механизм
Механизм головной боли связан с раздражением болевых рецепторов сосудов, мозговых оболочек, мышц, черепных нервов и структур шеи. Для клинической оценки важны характер боли, её динамика, сопутствующие симптомы и внезапность появления.

## Характеристики
- **Локализация**: диффузная, лобная, височная, затылочная, односторонняя.
- **Интенсивность**: от умеренной до крайне выраженной.
- **Динамика**: острая, подострая, хроническая, приступообразная.
- **Сопутствующие проявления**: тошнота, рвота, фотофобия, нарушение зрения, головокружение, повышение АД, неврологический дефицит.

## Клиническое значение
Головная боль может быть самостоятельным первичным синдромом либо симптомом сосудистой, инфекционной, гипертензивной, неврологической или метаболической патологии. Особое значение имеет выделение вторичной головной боли, связанной с опасным состоянием.

## Ассоциированные заболевания
- [[DIAG-DISEASE-001]] Артериальная гипертензия
- [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый
- Мигрень
- Менингит
- Внутричерепное кровоизлияние

## 🚩 «Красные флаги»
- 🔴 Внезапная «самая сильная в жизни» головная боль → срочно исключать сосудистую катастрофу.
- 🔴 Головная боль с нарушением речи, слабостью, асимметрией лица → экстренная неврологическая помощь.
- 🔴 Головная боль на фоне очень высокого АД → оценка на осложнённый криз.
- 🔴 Лихорадка, ригидность затылочных мышц, спутанность сознания → исключать нейроинфекцию.

## Дифференциально-диагностические критерии

| Состояние / заболевание | Общие признаки | Отличительные признаки |
|-------------------------|----------------|------------------------|
| [[DIAG-DISEASE-001]] Артериальная гипертензия | Головная боль, дискомфорт | Связь с повышенным АД, сосудистыми факторами риска |
| [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый | Головная боль и высокое АД | Есть признаки острого поражения органов-мишеней |
| Мигрень | Интенсивная головная боль | Часто односторонняя, с фотофобией/тошнотой |
| Менингит | Головная боль, слабость | Лихорадка, менингеальные симптомы |
| Субарахноидальное кровоизлияние | Острая головная боль | Внезапное начало, критическая интенсивность |

## Диагностические направления

### Обязательные обследования
- [[DIAG-EXAM-001]] Измерение артериального давления
- Неврологический осмотр
- Оценка общего состояния и сознания

### Дополнительные обследования
- Нейровизуализация по показаниям
- Лабораторная диагностика при подозрении на воспалительный или метаболический процесс
- Осмотр глазного дна по показаниям

## Особенности у отдельных групп
- **Дети**: требует отдельной возрастной оценки и внимательного исключения вторичных причин.
- **Пожилые**: выше вероятность сосудистых и вторичных причин.
- **Беременные**: требует исключения гипертензивных осложнений беременности.

## Информация для пациента
Головная боль сама по себе не всегда опасна, но её нужно оценивать вместе с другими симптомами. Срочно обращаться за помощью нужно при очень резком начале боли, слабости в руке или ноге, нарушении речи, сильном повышении давления, нарушении зрения или потере сознания.

## Связанные документы
- [[DIAG-DISEASE-001]] — возможная ассоциированная причина
- [[DIAG-REDFLAG-001]] — опасный контекст симптома
- [[DIAG-EXAM-001]] — обязательный элемент первичной оценки

## Источники
1. Руководства по внутренним болезням и клинической диагностике.
2. Клинические рекомендации по соответствующему профилю, действующая редакция.
3. Техническое задание к БЗ MedAssist, раздел 3.1.

```

## kb/diagnostics/symptoms/index.md

```markdown
# Симптомы и синдромы

Индекс раздела `symptoms`.

| ID | Название | Срочность | Связанные документы | Файл |
|---|---|---|---|---|
| `DIAG-SYMPTOM-001` | Головная боль | `routine` | `DIAG-DISEASE-001`, `DIAG-REDFLAG-001`, `DIAG-EXAM-001`, `DIAG-DIFDIAG-002` | [diag_symptom_headache.md](diag_symptom_headache.md) |
| `DIAG-SYMPTOM-002` | Боль в груди | `urgent` | `DIAG-DISEASE-002`, `DIAG-DIFDIAG-001`, `DIAG-EMERGENCY-001`, `DIAG-REDFLAG-001`, `DIAG-EXAM-001`, `DIAG-EXAM-002` | [diag_symptom_chest_pain.md](diag_symptom_chest_pain.md) |
| `DIAG-SYMPTOM-003` | Одышка | `urgent` | `DIAG-DISEASE-003`, `DIAG-DISEASE-004`, `DIAG-EMERGENCY-003`, `DIAG-EXAM-002`, `DIAG-EXAM-004`, `DIAG-DIFDIAG-003` | [diag_symptom_dyspnea.md](diag_symptom_dyspnea.md) |
| `DIAG-SYMPTOM-004` | Лихорадка | `routine` | `DIAG-DISEASE-003`, `DIAG-EXAM-003`, `DIAG-EXAM-004` | [diag_symptom_fever.md](diag_symptom_fever.md) |
| `DIAG-SYMPTOM-005` | Боль в животе | `urgent` | `DIAG-EXAM-003` | [diag_symptom_abdominal_pain.md](diag_symptom_abdominal_pain.md) |

```

## kb/global/index.md

```markdown
# Глобальный уровень базы знаний

Глобальный уровень предназначен для глоссария, общих дисклеймеров, справочников и межпредметных связей. В текущем MVP основная реализация сосредоточена в диагностическом контуре `kb/diagnostics/`.

```

## kb/protocols/checklists/prot_checklist_hypertension_primary_visit.md

```markdown
---
id: PROT-CHECKLIST-001
title: 'Чек-лист врача: первичный приём при артериальной гипертензии'
domain: protocols
category: checklist
body_system:
- cardiovascular
tags:
- checklist
- hypertension
- primary_visit
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
related:
- PROT-PROTOCOL-001
- DIAG-DISEASE-001
- DIAG-EXAM-001
sources:
- Клинические рекомендации по артериальной гипертензии
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
clinical_guidelines:
- Клинические рекомендации по артериальной гипертензии, 2024
relations:
- target: PROT-PROTOCOL-001
  type: uses_protocol
  description: Чек-лист используется при первичном применении протокола.
- target: DIAG-DISEASE-001
  type: checklist_for
  description: Чек-лист относится к первичному приёму пациента с АГ.
- target: DIAG-EXAM-001
  type: uses_exam
  description: В чек-листе предусмотрено измерение артериального давления.
---

# Чек-лист врача: первичный приём при артериальной гипертензии

> Документ предназначен для стандартизации действий врача на первичном приёме.

## Жалобы и анамнез
- [ ] головная боль
- [ ] головокружение
- [ ] боль в груди
- [ ] одышка
- [ ] факторы риска (курение, ожирение, стресс)

## Объективное обследование
- [ ] [[DIAG-EXAM-001]] измерение артериального давления
- [ ] частота сердечных сокращений
- [ ] оценка общего состояния
- [ ] неврологический статус

## Оценка риска
- [ ] наличие поражения органов-мишеней
- [ ] сопутствующие заболевания
- [ ] общий сердечно-сосудистый риск

## Диагностические решения
- [ ] подтверждение диагноза [[DIAG-DISEASE-001]]
- [ ] необходимость дополнительных обследований

## Тактика ведения
- [ ] определить план лечения [[PROT-PROTOCOL-001]]
- [ ] определить маршрут пациента
- [ ] дать рекомендации пациенту

## Завершение приёма
- [ ] назначить контрольный визит
- [ ] объяснить пациенту план действий

```

## kb/protocols/clinical_protocols/prot_protocol_hypertension.md

```markdown
---
id: PROT-PROTOCOL-001
title: 'Клинический протокол: Артериальная гипертензия'
domain: protocols
category: protocol
body_system:
- cardiovascular
tags:
- protocol
- hypertension
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
related:
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
- PROT-SCALE-001
- PROT-ROUTING-001
- PROT-EMERGENCY_P-001
- PROT-PATIENT_INFO-001
- PROT-FOLLOW_UP-001
- PROT-CHECKLIST-001
- PROT-SCREENING-001
sources:
- Клинические рекомендации по артериальной гипертензии
clinical_guidelines:
- ESC/ESH Guidelines
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
relations:
- target: DIAG-DISEASE-001
  type: protocol_for
  description: Клинический протокол предназначен для ведения пациента с артериальной
    гипертензией.
- target: PHARM-REGIMEN-001
  type: uses_regimen
  description: Протокол использует терапевтическую схему из фармакологического контура.
- target: PROT-SCALE-001
  type: uses_scale
  description: Протокол использует шкалу сердечно-сосудистого риска.
- target: PROT-ROUTING-001
  type: uses_routing
  description: Протокол связан с маршрутизацией пациента.
- target: PROT-EMERGENCY_P-001
  type: emergency_protocol_for
  description: При осложнённом течении выполняется переход к алгоритму неотложной
    помощи.
- target: PROT-PATIENT_INFO-001
  type: has_patient_info
  description: К протоколу привязана пациентская памятка.
- target: PROT-FOLLOW_UP-001
  type: uses_follow_up
  description: Протокол связан с дальнейшим наблюдением пациента.
- target: PROT-CHECKLIST-001
  type: uses_checklist
  description: Протокол поддерживается чек-листом первичного приёма.
- target: PROT-SCREENING-001
  type: uses_screening
  description: Протокол связан со скринингом артериальной гипертензии.
evidence_level: IIa
recommendation_class: I
---

# Клинический протокол: Артериальная гипертензия

> ⚕️ Документ предназначен для медицинских специалистов.

## Назначение протокола
Описание алгоритма ведения пациента с артериальной гипертензией на амбулаторном этапе.  
Используется шкала оценки риска: [[PROT-SCALE-001]]

## Область применения
- Артериальная гипертензия
- Взрослые пациенты
- Амбулаторная практика

## Входные условия
- [[DIAG-DISEASE-001]]
- Повышенное артериальное давление
- Подтверждение при повторных измерениях

## Критерии начала применения
- САД ≥ 140 мм рт. ст.
- и/или ДАД ≥ 90 мм рт. ст.

## Алгоритм ведения пациента
1. Подтвердить диагноз повторными измерениями артериального давления.
2. Оценить факторы риска и наличие поражения органов-мишеней.
3. Определить степень сердечно-сосудистого риска.
4. Выбрать немедикаментозную и/или медикаментозную тактику.
5. Организовать дальнейшее наблюдение пациента.

## Ключевые решения и развилки
- Низкий риск → немедикаментозная терапия и наблюдение.
- Средний/высокий риск → медикаментозная терапия.
- Тяжёлое состояние или признаки осложнённого криза → срочная маршрутизация.

## Критерии срочности
- **Routine**: стабильное повышение давления без признаков осложнений.
- **Urgent**: выраженная симптоматика без явных признаков жизнеугрожающего состояния.
- **Emergency**: гипертонический криз.

## Связанные маршруты пациента
- [[PROT-ROUTING-001]]

## Связанные шкалы
- [[PROT-SCALE-001]]

## Неотложные состояния и действия
- [[PROT-EMERGENCY_P-001]]

## Рекомендации по терапии
- [[PHARM-REGIMEN-001]]
- [[PHARM-DRUG-001]]
- [[PHARM-DRUG-002]]

## Памятка пациенту
- [[PROT-PATIENT_INFO-001]]

## Дальнейшее наблюдение
- [[PROT-FOLLOW_UP-001]]

## Особенности у отдельных групп
- Пожилые: осторожное снижение давления.
- Коморбидные пациенты: индивидуализация терапии.

## Ограничения применения
- Не применяется при экстренных состояниях без очной оценки врача.

## Источники
1. ESC/ESH Guidelines.

```

## kb/protocols/emergency/prot_emergency_hypertensive_crisis.md

```markdown
---
id: PROT-EMERGENCY_P-001
title: 'Алгоритм неотложной помощи: Гипертонический криз'
domain: protocols
category: emergency_p
body_system:
- cardiovascular
- multisystem
tags:
- emergency
- hypertensive_crisis
- hypertension
urgency: emergency
access_level: professional
target_specialist:
- emergency_physician
- therapist
- cardiologist
age_group:
- adult
- elderly
related:
- DIAG-DISEASE-001
- DIAG-REDFLAG-001
- PROT-PROTOCOL-001
- PROT-ROUTING-001
- PHARM-REGIMEN-001
sources:
- Клинические рекомендации по артериальной гипертензии
- Руководства по неотложной кардиологии
clinical_guidelines:
- Артериальная гипертензия у взрослых, 2024
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
relations:
- target: DIAG-DISEASE-001
  type: emergency_protocol_for
  description: Алгоритм относится к опасному течению артериальной гипертензии.
- target: DIAG-REDFLAG-001
  type: uses_redflag
  description: Алгоритм активируется при наличии красных флагов осложнённого криза.
- target: PROT-PROTOCOL-001
  type: related_to
  description: После стабилизации возможен возврат к общему протоколу ведения.
- target: PROT-ROUTING-001
  type: uses_routing
  description: Алгоритм связан с дальнейшей маршрутизацией пациента.
- target: PHARM-REGIMEN-001
  type: uses_regimen
  description: Алгоритм может быть связан с фармакологической тактикой.
---

# Алгоритм неотложной помощи: Гипертонический криз

> 🚨 Экстренный протокол. Требует немедленной клинической оценки и срочных действий.

## Критерии распознавания
- значительное повышение артериального давления;
- наличие симптомов поражения органов-мишеней;
- головная боль, боль в груди, одышка, нарушение зрения;
- неврологический дефицит, спутанность сознания или другие признаки осложнённого течения.

## Красные флаги
- [[DIAG-REDFLAG-001]] Гипертонический криз осложнённый

## Первичная оценка (ABCDE)
- **A (airway)**: оценить проходимость дыхательных путей.
- **B (breathing)**: оценить дыхание, частоту дыхания, сатурацию, наличие одышки.
- **C (circulation)**: измерить артериальное давление, частоту пульса, оценить гемодинамику.
- **D (disability)**: оценить уровень сознания, наличие очаговой неврологической симптоматики.
- **E (exposure)**: провести общий осмотр, оценить признаки осложнений и сопутствующих состояний.

## Немедленные действия
1. Обеспечить покой пациента и немедленную врачебную оценку.
2. Повторно измерить артериальное давление и зафиксировать динамику.
3. Оценить наличие признаков поражения органов-мишеней.
4. При подозрении на осложнённый криз обеспечить срочную госпитализацию.
5. Передать пациента по маршруту экстренной помощи.

## Медикаментозная помощь
- антигипертензивная терапия под контролем врача;
- выбор препарата и темпа снижения давления определяется клинической ситуацией;
- дальнейшая терапевтическая коррекция: [[PHARM-REGIMEN-001]] Схема лечения артериальной гипертензии.

## Критерии стабилизации
- снижение выраженности симптомов;
- контролируемое снижение артериального давления;
- отсутствие прогрессирования признаков поражения органов-мишеней;
- стабилизация общего состояния пациента.

## Дальнейшие действия после стабилизации
- [[PROT-ROUTING-001]] Маршрутизация пациента: Артериальная гипертензия
- [[PROT-PROTOCOL-001]] Клинический протокол: Артериальная гипертензия

## Ошибки и риски
- слишком быстрое снижение артериального давления;
- недооценка признаков поражения органов-мишеней;
- задержка госпитализации при осложнённом течении;
- самостоятельный приём препаратов без врачебного контроля.

## Ограничения
- документ не заменяет очное оказание экстренной медицинской помощи;
- выбор конкретных препаратов и доз зависит от клинической ситуации и сопутствующей патологии.

## Источники
1. Клинические рекомендации по артериальной гипертензии.
2. Руководства по ведению неотложных кардиологических состояний.

```

## kb/protocols/follow_up/prot_follow_up_hypertension.md

```markdown
---
id: PROT-FOLLOW_UP-001
title: 'Наблюдение пациента: Артериальная гипертензия'
domain: protocols
category: follow_up
body_system:
- cardiovascular
tags:
- follow_up
- monitoring
- hypertension
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
- elderly
related:
- PROT-PROTOCOL-001
- PROT-ROUTING-001
- PROT-EMERGENCY_P-001
- DIAG-DISEASE-001
- DIAG-EXAM-001
- PHARM-REGIMEN-001
- PHARM-DRUG-001
- PHARM-DRUG-002
sources:
- Клинические рекомендации по артериальной гипертензии
- 2023 ESH Guidelines for the management of arterial hypertension
clinical_guidelines:
- Артериальная гипертензия у взрослых, 2024
- 2023 ESH Guidelines
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
relations:
- target: PROT-PROTOCOL-001
  type: follow_up_for
  description: Follow-up описывает наблюдение после начала ведения по протоколу.
- target: PROT-ROUTING-001
  type: uses_routing
  description: При ухудшении состояния может измениться маршрут пациента.
- target: PROT-EMERGENCY_P-001
  type: emergency_protocol_for
  description: При опасных признаках выполняется переход к emergency-алгоритму.
- target: DIAG-DISEASE-001
  type: follow_up_for
  description: Наблюдение относится к пациентам с артериальной гипертензией.
- target: DIAG-EXAM-001
  type: uses_exam
  description: Контроль включает измерение артериального давления.
- target: PHARM-REGIMEN-001
  type: uses_regimen
  description: Наблюдение связано с контролем эффективности схемы терапии.
- target: PHARM-DRUG-001
  type: uses_drug
  description: Контроль переносимости и эффективности препарата.
- target: PHARM-DRUG-002
  type: uses_drug
  description: Контроль переносимости и эффективности препарата.
---

# Наблюдение пациента: Артериальная гипертензия

> Документ описывает порядок контроля и ведения пациента после начального этапа лечения.

## Цель наблюдения
- контроль эффективности антигипертензивной терапии;
- раннее выявление осложнений и признаков ухудшения;
- коррекция маршрута и лечения при недостаточном контроле артериального давления.

## Кого наблюдаем
- пациенты с диагнозом [[DIAG-DISEASE-001]] Артериальная гипертензия;
- пациенты, получающие немедикаментозную и/или медикаментозную терапию;
- пациенты после эпизодов значимого повышения артериального давления.

## Частота наблюдения
- первичный контроль: через 2–4 недели после начала или коррекции терапии;
- повторный контроль: каждые 1–3 месяца до достижения целевого давления;
- дальнейшее наблюдение: каждые 3–6 месяцев при стабильном состоянии.

## Контрольные параметры
- артериальное давление;
- частота сердечных сокращений;
- жалобы пациента;
- приверженность терапии;
- признаки поражения органов-мишеней;
- переносимость препаратов.

## Методы контроля
- [[DIAG-EXAM-001]] Измерение артериального давления;
- оценка клинических симптомов;
- лабораторные исследования по показаниям;
- инструментальные методы по показаниям.

## Критерии эффективности лечения
- достижение целевого артериального давления;
- уменьшение выраженности симптомов;
- отсутствие прогрессирования осложнений;
- хорошая переносимость терапии и соблюдение назначений.

## Критерии ухудшения
- сохраняющееся высокое артериальное давление на фоне терапии;
- нарастание симптомов;
- плохая переносимость лечения;
- появление признаков осложнённого течения.

## Действия при ухудшении
- пересмотреть тактику по [[PROT-PROTOCOL-001]] Клинический протокол: Артериальная гипертензия;
- изменить маршрут по [[PROT-ROUTING-001]] Маршрутизация пациента: Артериальная гипертензия;
- при признаках неотложного состояния перейти к [[PROT-EMERGENCY_P-001]] Алгоритм неотложной помощи: Гипертонический криз.

## Коррекция терапии
- [[PHARM-REGIMEN-001]] Схема лечения артериальной гипертензии;
- [[PHARM-DRUG-001]] Эналаприл;
- [[PHARM-DRUG-002]] Амлодипин.

## Переход на другой уровень наблюдения
- амбулаторное плановое наблюдение → более частый контроль;
- амбулаторное наблюдение → консультация кардиолога;
- плановое наблюдение → срочное направление;
- срочное направление → экстренная помощь при признаках осложнённого криза.

## Связь с протоколом
- [[PROT-PROTOCOL-001]]

## Ограничения
- частота наблюдения и объём контроля определяются индивидуально;
- документ не заменяет очное врачебное наблюдение.

## Источники
1. Клинические рекомендации по артериальной гипертензии.
2. 2023 ESH Guidelines for the management of arterial hypertension.

```

## kb/protocols/index.md

```markdown
# Индекс протокольного контура MedAssist

| ID | Название | Категория | Срочность | Файл |
|---|---|---|---|---|
| PROT-PROTOCOL-001 | Клинический протокол: Артериальная гипертензия | protocol | routine | clinical_protocols/prot_protocol_hypertension.md |
| PROT-EMERGENCY_P-001 | Алгоритм неотложной помощи: Гипертонический криз | emergency_p | emergency | emergency/prot_emergency_hypertensive_crisis.md |
| PROT-ROUTING-001 | Маршрутизация пациента: Артериальная гипертензия | routing | routine | routing/prot_routing_hypertension.md |
| PROT-SCALE-001 | Клиническая шкала риска при АГ | scale | routine | scales/prot_scale_hypertension_risk.md |
| PROT-CHECKLIST-001 | Чек-лист врача: первичный приём при АГ | checklist | routine | checklists/prot_checklist_hypertension_primary_visit.md |
| PROT-PATIENT_INFO-001 | Памятка для пациента: АГ | patient_info | routine | patient_info/prot_patient_info_hypertension.md |
| PROT-SCREENING-001 | Скрининг: Артериальная гипертензия | screening | routine | screening/prot_screening_hypertension.md |
| PROT-FOLLOW_UP-001 | Наблюдение пациента: АГ | follow_up | routine | follow_up/prot_follow_up_hypertension.md |

```

## kb/protocols/patient_info/prot_patient_info_hypertension.md

```markdown
---
id: PROT-PATIENT_INFO-001
title: 'Памятка для пациента: Артериальная гипертензия'
domain: protocols
category: patient_info
body_system:
- cardiovascular
tags:
- patient
- hypertension
urgency: routine
access_level: patient
age_group:
- adult
- elderly
related:
- PROT-PROTOCOL-001
- DIAG-DISEASE-001
- PROT-ROUTING-001
sources:
- Клинические рекомендации по артериальной гипертензии
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
target_specialist:
- therapist
- cardiologist
clinical_guidelines:
- Клинические рекомендации по артериальной гипертензии, 2024
relations:
- target: PROT-PROTOCOL-001
  type: patient_info_for
  description: Памятка является пациентским представлением протокольной информации.
- target: DIAG-DISEASE-001
  type: patient_info_for
  description: Памятка объясняет состояние артериальной гипертензии.
- target: PROT-ROUTING-001
  type: uses_routing
  description: Памятка содержит признаки, при которых нужно изменить маршрут обращения.
---

# Памятка для пациента: Повышенное артериальное давление

> ⚠️ Эта информация носит справочный характер и не заменяет консультацию врача.

## Что это за состояние
Артериальная гипертензия — это состояние, при котором у человека постоянно повышено артериальное давление. Это может не вызывать симптомов, но со временем увеличивает риск серьёзных осложнений.

## Основные симптомы
- головная боль;
- головокружение;
- ощущение пульсации в голове;
- слабость или утомляемость;
- иногда симптомы отсутствуют.

## Что делать сейчас
- измерить артериальное давление;
- обеспечить покой;
- при необходимости принять назначенные врачом препараты;
- записаться на приём к врачу.

## Когда нужно срочно обратиться к врачу
- очень высокое давление;
- сильная головная боль;
- боль в груди;
- одышка;
- нарушение зрения или речи;
- потеря сознания.

## Что нельзя делать
- самостоятельно менять дозу препаратов;
- игнорировать высокое давление;
- принимать лекарства без назначения врача.

## Общие рекомендации
- снизить потребление соли;
- контролировать массу тела;
- отказаться от курения;
- ограничить алкоголь;
- поддерживать умеренную физическую активность.

## Контроль и наблюдение
- регулярно измерять давление;
- посещать врача;
- сдавать назначенные анализы.

## Связанные медицинские документы
- [[PROT-PROTOCOL-001]]
- [[PROT-ROUTING-001]]

## Источники
1. Клинические рекомендации по артериальной гипертензии

```

## kb/protocols/routing/prot_routing_hypertension.md

```markdown
---
id: PROT-ROUTING-001
title: 'Маршрутизация пациента: Артериальная гипертензия'
domain: protocols
category: routing
body_system:
- cardiovascular
tags:
- routing
- hypertension
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
related:
- DIAG-DISEASE-001
- DIAG-REDFLAG-001
- PROT-PROTOCOL-001
- PROT-EMERGENCY_P-001
- PROT-SCALE-001
sources:
- Клинические рекомендации по артериальной гипертензии
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
clinical_guidelines:
- Клинические рекомендации по артериальной гипертензии, 2024
relations:
- target: DIAG-DISEASE-001
  type: routing_for
  description: Маршрутизация применяется к пациентам с артериальной гипертензией.
- target: DIAG-REDFLAG-001
  type: uses_redflag
  description: Красные флаги определяют экстренный маршрут.
- target: PROT-PROTOCOL-001
  type: related_to
  description: Маршрутизация является частью общего протокола.
- target: PROT-EMERGENCY_P-001
  type: emergency_protocol_for
  description: При экстренных признаках выполняется переход к emergency-алгоритму.
- target: PROT-SCALE-001
  type: uses_scale
  description: Оценка риска влияет на выбор маршрута.
---

# Маршрутизация пациента: Артериальная гипертензия

> ⚕️ Документ определяет дальнейшие действия и направление пациента.

## Входные условия
- [[DIAG-DISEASE-001]]
- Повышенное артериальное давление
- [[DIAG-REDFLAG-001]]

## Общий принцип маршрутизации
Маршрут пациента определяется уровнем артериального давления, наличием симптомов и признаков поражения органов-мишеней.

## Категории маршрута

### 🟢 Амбулаторное ведение
**Условия:**
- стабильное повышение АД;
- отсутствие симптомов поражения органов-мишеней.

**Действия:**
- наблюдение у терапевта;
- коррекция образа жизни;
- плановое назначение терапии.

### 🟡 Срочное направление
**Условия:**
- выраженное повышение АД;
- наличие симптомов, таких как головная боль и головокружение.

**Действия:**
- консультация врача в ближайшие 24–72 часа;
- дообследование;
- пересмотр тактики лечения.

### 🔴 Экстренная помощь
**Условия:**
- [[DIAG-REDFLAG-001]]

**Действия:**
- немедленный вызов скорой помощи;
- переход к [[PROT-EMERGENCY_P-001]].

### 🏥 Госпитализация
**Показания:**
- неэффективность терапии;
- осложнения;
- тяжёлое течение.

**Тип:**
- экстренная или плановая.

## Направление к специалистам
- терапевт → первичное ведение;
- кардиолог → осложнённые случаи.

## Связь с клиническим протоколом
- [[PROT-PROTOCOL-001]]

## Связь с неотложными алгоритмами
- [[PROT-EMERGENCY_P-001]]

## Комментарии и ограничения
- решение принимается индивидуально;
- учитываются сопутствующие заболевания.

## Источники
1. ESC/ESH Guidelines.

```

## kb/protocols/scales/prot_scale_hypertension_risk.md

```markdown
---
id: PROT-SCALE-001
title: 'Клиническая шкала: Оценка сердечно-сосудистого риска при артериальной гипертензии'
domain: protocols
category: scale
body_system:
- cardiovascular
tags:
- scale
- risk_assessment
- hypertension
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
related:
- PROT-PROTOCOL-001
- PROT-ROUTING-001
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
sources:
- Клинические рекомендации по артериальной гипертензии
clinical_guidelines:
- ESC/ESH Guidelines
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
relations:
- target: PROT-PROTOCOL-001
  type: used_by_protocol
  description: Шкала используется в общем протоколе ведения.
- target: PROT-ROUTING-001
  type: influences_routing
  description: Результат шкалы влияет на маршрут пациента.
- target: DIAG-DISEASE-001
  type: assesses
  description: Шкала оценивает риск при артериальной гипертензии.
- target: PHARM-REGIMEN-001
  type: uses_regimen
  description: Категория риска может влиять на выбор режима терапии.
evidence_level: IIa
recommendation_class: I
---

# Клиническая шкала: Оценка сердечно-сосудистого риска при артериальной гипертензии

> ⚕️ Шкала используется для формализованной оценки риска осложнений и выбора тактики ведения пациента.

## Назначение шкалы
Оценка сердечно-сосудистого риска у пациентов с артериальной гипертензией для определения дальнейшей тактики лечения и наблюдения.

## Область применения
- артериальная гипертензия;
- амбулаторная практика;
- первичный приём и последующее наблюдение.

## Параметры оценки

| Параметр | Значения | Баллы |
|----------|----------|-------|
| Систолическое АД | < 140 мм рт. ст. | 0 |
| Систолическое АД | 140–159 мм рт. ст. | 1 |
| Систолическое АД | ≥ 160 мм рт. ст. | 2 |
| Курение | нет | 0 |
| Курение | да | 1 |
| Сахарный диабет | нет | 0 |
| Сахарный диабет | да | 1 |
| Возраст | < 60 лет | 0 |
| Возраст | ≥ 60 лет | 1 |

## Правила расчёта
1. Суммируются баллы по всем параметрам.
2. Оцениваются все доступные факторы риска.
3. При отсутствии данных параметр не учитывается.

## Интерпретация результата

| Сумма баллов | Категория риска | Клиническое значение |
|--------------|------------------|----------------------|
| 0–1 | низкий | возможно немедикаментозное ведение |
| 2–3 | умеренный | требуется медикаментозная терапия |
| ≥ 4 | высокий | высокий риск осложнений, требуется активная тактика |

## Тактическая значимость
- низкий риск → амбулаторное наблюдение;
- умеренный риск → [[PROT-PROTOCOL-001]];
- высокий риск → [[PROT-ROUTING-001]] или усиленная терапия.

## Ограничения
- шкала является упрощённой моделью;
- не заменяет клиническое решение врача;
- требует учёта сопутствующих заболеваний.

## Особенности применения
- **Пожилые**: учитывать коморбидность.
- **Пациенты с сахарным диабетом**: риск может быть выше, чем по шкале.
- **Коморбидные пациенты**: требуется индивидуализация.

## Связанные документы
- [[PROT-PROTOCOL-001]] — клинический протокол;
- [[PROT-ROUTING-001]] — маршрутизация пациента;
- [[PHARM-REGIMEN-001]] — терапия.

## Источники
1. ESC/ESH Guidelines.
2. Клинические рекомендации по артериальной гипертензии.

```

## kb/protocols/screening/prot_screening_hypertension.md

```markdown
---
id: PROT-SCREENING-001
title: 'Скрининг: Артериальная гипертензия'
domain: protocols
category: screening
body_system:
- cardiovascular
tags:
- screening
- prevention
- hypertension
urgency: routine
access_level: professional
target_specialist:
- therapist
age_group:
- adult
related:
- DIAG-DISEASE-001
- DIAG-EXAM-001
- PROT-PROTOCOL-001
- PROT-ROUTING-001
sources:
- Клинические рекомендации по артериальной гипертензии
clinical_guidelines:
- Артериальная гипертензия у взрослых, 2024
last_medical_review: '2026-04-09'
medical_reviewer: —
author: Инженер знаний №3
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
status: draft
disclaimer: true
relations:
- target: DIAG-DISEASE-001
  type: screening_for
  description: Скрининг направлен на раннее выявление артериальной гипертензии.
- target: DIAG-EXAM-001
  type: uses_exam
  description: Основным методом скрининга является измерение артериального давления.
- target: PROT-PROTOCOL-001
  type: related_to
  description: При подтверждении состояния выполняется переход к протоколу.
- target: PROT-ROUTING-001
  type: uses_routing
  description: Результаты скрининга определяют дальнейший маршрут.
---

# Скрининг: Артериальная гипертензия

> Документ описывает алгоритм раннего выявления артериальной гипертензии у взрослых пациентов.

## Целевая группа
- взрослые старше 18 лет;
- пациенты с факторами сердечно-сосудистого риска;
- пациенты, ранее не проходившие регулярный контроль артериального давления.

## Показания к скринингу
- профилактический осмотр;
- наличие факторов риска;
- жалобы, потенциально связанные с повышенным артериальным давлением.

## Методы скрининга
- [[DIAG-EXAM-001]] Измерение артериального давления;
- повторные измерения по показаниям;
- дополнительные обследования по решению врача.

## Частота проведения
- не реже 1 раза в год;
- чаще при наличии факторов риска или ранее выявленных пограничных значений давления.

## Интерпретация результатов
- нормальные показатели → плановое наблюдение;
- повышенные показатели → [[PROT-ROUTING-001]];
- повторно подтверждённое повышение давления → переход к клиническому протоколу.

## Дальнейшие действия
- [[PROT-PROTOCOL-001]]

## Ограничения
- единичное измерение не всегда достаточно для подтверждения диагноза;
- решение о дальнейшем ведении принимает врач с учётом клинического контекста.

## Источники
1. Клинические рекомендации по артериальной гипертензии.

```

## kb/templates/template_adr.md

```markdown
---
id: "PHARM-ADR-XXX"
title: "Нежелательная лекарственная реакция: [Название]"
domain: "pharm"
category: "adr"
body_system:
  - "system"
tags:
  - "adr"
  - "safety"
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "all_specialties"
age_group:
  - "adult"
evidence_level: "Ia | Ib | IIa | IIb | III | IV"
related:
  - "PHARM-DRUG-XXX"
  - "PHARM-DRUGCLASS-XXX"
relations:
  - target: "PHARM-DRUGCLASS-XXX"
    type: "adverse_reaction_for"
sources:
  - "источник"
clinical_guidelines:
  - "название рекомендаций, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Нежелательная лекарственная реакция: [Название]

## Описание
[Описание реакции]

## Механизм
[Механизм развития]

## Факторы риска
- ...

## Тактика ведения
- ...

## Связанные документы
- [[PHARM-DRUG-XXX]]

```

## kb/templates/template_checklist.md

```markdown
---
id: "PROT-CHECKLIST-XXX"
title: "Чек-лист врача: [Название ситуации]"
domain: "protocols"
category: "checklist"
body_system:
  - "cardiovascular | respiratory | gastrointestinal | nervous | endocrine | multisystem"
tags:
  - "checklist"
  - "clinical_workflow"
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "therapist | cardiologist | pulmonologist | neurologist | endocrinologist | emergency_physician | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "PROT-PROTOCOL-XXX"
  - "DIAG-DISEASE-XXX"
  - "DIAG-EXAM-XXX"
sources:
  - "Клинические рекомендации"
clinical_guidelines:
  - "Название рекомендаций, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО, специальность"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Чек-лист врача: [Название ситуации]

> ⚕️ Документ предназначен для стандартизации действий медицинского работника.

## Цель чек-листа
[Для какого этапа помощи используется чек-лист]

## Контекст применения
- [Первичный приём]
- [Повторный визит]
- [Неотложная помощь]
- [Подготовка к госпитализации]

## Жалобы и анамнез
- [ ] ...
- [ ] ...
- [ ] ...

## Объективное обследование
- [ ] [[DIAG-EXAM-XXX]] [Ключевое обследование]
- [ ] ...
- [ ] ...

## Оценка риска и тяжести
- [ ] ...
- [ ] ...
- [ ] ...

## Диагностические решения
- [ ] [[DIAG-DISEASE-XXX]] [Проверка диагноза]
- [ ] необходимость дополнительных обследований
- [ ] необходимость консультации специалиста

## Тактика ведения
- [ ] [[PROT-PROTOCOL-XXX]] [Выбор клинического протокола]
- [ ] определить маршрут пациента
- [ ] оценить необходимость неотложных действий

## Информирование пациента
- [ ] дать рекомендации
- [ ] объяснить дальнейшие действия
- [ ] назначить контроль

## Завершение этапа
- [ ] оформить назначения
- [ ] назначить повторный визит
- [ ] зафиксировать план ведения

## Критерии завершения
- [Все обязательные действия выполнены]
- [Пациент информирован]
- [Маршрут определён]

## Источники
1. [Клинические рекомендации]
2. [Профессиональное руководство]
```

## kb/templates/template_difdiag.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "difdiag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "urgent"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# Дифференциальная диагностика: [Ведущий симптом/синдром]

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не заменяет клиническое решение врача.

## Ведущий симптом
[[DIAG-SYMPTOM-NNN]] [Название симптома].

## Ключевые вопросы при сборе анамнеза
1. [Вопрос 1] — [что уточняет]
2. [Вопрос 2] — [что уточняет]

## Ключевые данные объективного осмотра
- [Признак 1]
- [Признак 2]

## Дифференциально-диагностическая таблица
| Направление | Поддерживающие признаки | Документ БЗ |
|---|---|---|
| [Состояние] | [Признаки] | [[DIAG-DISEASE-NNN]] |

## 🚩 «Красные флаги»
- [[DIAG-REDFLAG-NNN]] [Название]

## Приоритетные диагностические направления
- [Обследование/оценка 1]
- [[DIAG-EXAM-NNN]] [Метод]

## Связанные документы
- [[DIAG-SYMPTOM-NNN]] — ведущий симптом

## Источники
1. [Источник]

```

## kb/templates/template_disease.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "disease"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# [Название заболевания]

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
[Краткое клиническое определение. Код МКБ-10, если применимо.]

## Эпидемиология
- **Распространённость**: [данные]
- **Возрастная группа**: [данные]
- **Факторы риска**: [перечень]

## Этиология и патогенез
[Причины и механизм развития.]

## Классификация
- [Тип/форма 1]
- [Тип/форма 2]

## Клиническая картина
### Основные проявления
- [Симптом 1]
- [Симптом 2]

### Данные осмотра
- [Признак 1]

## 🚩 «Красные флаги»
- [Опасный признак 1]

## Диагностика
- [[DIAG-EXAM-NNN]] [Метод]

## Дифференциальная диагностика
[С какими состояниями дифференцировать.]

## Лечение (обзор)
[Только справочный обзор. Конкретные решения принимает врач.]

## Прогноз
[Кратко.]

## Профилактика
[Кратко.]

## Особенности у отдельных групп
[Если применимо.]

## Информация для пациента
[Безопасная информация без назначения лечения.]

## Связанные документы
- [[DIAG-SYMPTOM-NNN]] — [тип связи]

## Источники
1. [Источник]

```

## kb/templates/template_dosing.md

```markdown
---
id: "PHARM-DOSING-XXX"
title: "Коррекция доз: [Ситуация]"
domain: "pharm"
category: "dosing"
body_system:
  - "system"
tags:
  - "dosing"
  - "safety"
urgency: "routine | urgent"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "Ia | IIa"
related:
  - "PHARM-DRUG-XXX"
relations:
  - target: "PHARM-DRUG-XXX"
    type: "dose_adjustment_for"
sources:
  - "источник"
clinical_guidelines:
  - "название рекомендаций, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Коррекция доз: [Ситуация]

## Общий принцип
[Описание]

## Таблица коррекции
| Параметр | Рекомендация |
|---|---|
| ... | ... |

## Связанные документы
- [[PHARM-DRUG-XXX]]

```

## kb/templates/template_drug.md

```markdown
---
id: "PHARM-DRUG-XXX"
title: "МНН – торговое название"
domain: "pharm"
category: "drug"
atc_code: "код"
inn: "международное непатентованное название"
body_system:
  - "система органов"
tags:
  - тег1
  - тег2
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "специалист"
age_group:
  - "all_ages"
evidence_level: "Ia | Ib | IIa | IIb | III | IV"
recommendation_class: "I | IIa | IIb | III"
related:
  - "ID_связанного_документа"
sources:
  - "источник"
clinical_guidelines:
  - "название КР, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО, степень"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# МНН (INN) – торговые названия

> **Дисклеймер**: Назначение, изменение дозы и отмена препарата выполняются только врачом.

## Общие сведения
- **МНН**: 
- **АТС-код**: 
- **Фармакологическая группа**: [[ID]] название
- **Рецептурный статус**: рецептурный / безрецептурный
- **Формы выпуска**: таблетки, капсулы, раствор и т.д.

## Механизм действия
[Как работает препарат на молекулярном / рецепторном уровне – 3–7 предложений]

## Фармакокинетика
| Параметр | Значение |
|----------|----------|
| Биодоступность | ...% |
| Связь с белками плазмы | ...% |
| Метаболизм | печёночный / CYP... |
| Период полувыведения (T½) | ... часов |
| Элиминация | почечная / печёночная / смешанная |
| Начало действия | ... |
| Пик действия | ... |

## Показания
1. [Показание 1] – уровень доказательности, класс рекомендации
2. [Показание 2] – уровень, класс

## Дозирование
### Стандартное дозирование (взрослые)
| Показание | Доза | Кратность | Путь введения | Длительность |
|-----------|------|-----------|----------------|---------------|
| ... | ... | ... | перорально | ... |

### Коррекция дозы
| Группа | Рекомендация |
|--------|---------------|
| Почечная недостаточность (СКФ < 30) | ... |
| Печёночная недостаточность (Child-Pugh C) | ... |
| Пожилые (≥ 65 лет) | ... |
| Дети | ... |

## Противопоказания
### Абсолютные
- ...

### Относительные
- ...

## Побочные эффекты
### Частые (> 10%)
- ...

### Нечастые (1–10%)
- ...

### Редкие, но серьёзные (< 1%)
- ... – требует ...

## Лекарственные взаимодействия
### Клинически значимые
| Препарат / группа | Тип взаимодействия | Эффект | Рекомендация |
|------------------|--------------------|--------|---------------|
| ... | ... | ... | ... |

## Взаимодействие с пищей / алкоголем
- ...

## Беременность и лактация
- **Категория FDA**: A / B / C / D / X
- **Беременность**: рекомендация
- **Лактация**: рекомендация

## Мониторинг терапии
| Параметр | Частота контроля | Целевое значение |
|----------|------------------|------------------|
| ... | ... | ... |

## Передозировка
- **Симптомы**: ...
- **Антидот**: ...
- **Тактика**: ...

## Сравнение с аналогами в группе
| Критерий | Этот препарат | Аналог 1 | Аналог 2 |
|----------|---------------|----------|----------|
| Эффективность | ... | ... | ... |
| Безопасность | ... | ... | ... |
| Стоимость | ... | ... | ... |
| Удобство приёма | ... | ... | ... |

## Информация для пациента
[Адаптированный текст: зачем назначен препарат, как принимать, чего избегать, когда обратиться к врачу – 5–10 предложений понятным языком]

## Связанные документы
- [[ID]] – связь

## Источники
1. Инструкция по медицинскому применению
2. Клинические рекомендации
3. Справочник лекарственных средств

```

## kb/templates/template_drugclass.md

```markdown
---
id: "PHARM-DRUGCLASS-XXX"
title: "Название фармакологической группы"
domain: "pharm"
category: "drugclass"
atc_code: "код (если применимо)"
body_system:
  - "система"
tags:
  - тег
access_level: "professional"
target_specialist:
  - "специалист"
age_group:
  - "all_ages"
evidence_level: "Ia"
related:
  - "ID"
sources:
  - "источник"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "approved"
disclaimer: true
---

# [Название группы]

> **Дисклеймер**: Информация предназначена для медицинских специалистов.

## Общая характеристика
[Описание группы, место в терапии, общие свойства]

## Механизм действия (общий для группы)
[Общий фармакологический механизм]

## Представители группы
| МНН | Торговые названия | Особенности |
|-----|------------------|-------------|
| ... | ... | ... |

## Сравнительная характеристика
| Параметр | Препарат А | Препарат Б | Препарат В |
|----------|------------|------------|------------|
| ... | ... | ... | ... |

## Общие показания
- ...

## Общие противопоказания
- ...

## Общие побочные эффекты
- ...

## Клинически значимые взаимодействия
- ...

## Особенности выбора
[Алгоритм выбора препарата внутри группы]

## Связанные документы
- [[ID]] – связь

## Источники
1. ...

```

## kb/templates/template_emergency.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "emergency"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# [Название неотложного состояния]

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Состояние требует немедленного распознавания и передачи управления к алгоритмам экстренной помощи.

## Определение
[Краткое определение экстренного состояния.]

## Клиническая картина
### Основные проявления
- [Признак 1]

### Данные осмотра
- [Данные 1]

## Диагностические критерии
[Критерии подозрения/распознавания.]

## Ключевые обследования
- [[DIAG-EXAM-NNN]] [Метод]

## 🚩 Признаки критического течения
- [Признак]

## Дифференциальная диагностика
[С какими состояниями дифференцировать.]

## Тактическая значимость
[Почему важно быстро распознать.]

## Информация для пациента
[Коротко и безопасно: когда срочно обращаться за помощью.]

## Связанные документы
- [[DIAG-SYMPTOM-NNN]] — [тип связи]

## Источники
1. [Источник]

```

## kb/templates/template_emergency_p.md

```markdown
---
id: "PROT-EMERGENCY_P-XXX"
title: "Алгоритм неотложной помощи: [Состояние]"
domain: "protocols"
category: "emergency_p"
body_system:
  - "cardiovascular | respiratory | nervous | endocrine | multisystem"
tags:
  - "emergency"
  - "critical"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "emergency_physician | therapist | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "DIAG-DISEASE-XXX"
  - "DIAG-REDFLAG-XXX"
  - "PROT-PROTOCOL-XXX"
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

# Алгоритм неотложной помощи: [Состояние]

> 🚨 Экстренный протокол. Требует немедленных действий.

## Критерии распознавания
- [Признак 1]
- [Признак 2]
- [Признак 3]

## Красные флаги
- [[DIAG-REDFLAG-XXX]]

## Первичная оценка (ABCDE)
- A (airway): ...
- B (breathing): ...
- C (circulation): ...
- D (disability): ...
- E (exposure): ...

## Немедленные действия
1. [Шаг 1]
2. [Шаг 2]
3. [Шаг 3]

## Медикаментозная помощь
- [[PHARM-DRUG-XXX]]
- [[PHARM-REGIMEN-XXX]]

## Критерии стабилизации
- ...

## Дальнейшие действия после стабилизации
- [[PROT-ROUTING-XXX]]

## Ошибки и риски
- [Частая ошибка]
- [Опасное действие]

## Ограничения
- ...

## Источники
1. ...
```

## kb/templates/template_exam.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "exam"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# [Название метода обследования]

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов.

## Определение
[Что представляет собой метод.]

## Назначение метода
[Для чего применяется.]

## Показания
- [Показание 1]

## Диагностическая роль
[Что помогает подтвердить/исключить/уточнить.]

## Интерпретация результатов
| Результат / находка | Возможное значение |
|---|---|
| [Находка] | [Интерпретация] |

## Ограничения
[Ограничения метода.]

## Последовательность назначения
[Когда применяется в диагностическом маршруте.]

## Связанные заболевания и симптомы
- [[DIAG-SYMPTOM-NNN]] [Название]

## Особенности у отдельных групп
[Если применимо.]

## Связанные документы
- [[DIAG-DISEASE-NNN]] — [тип связи]

## Источники
1. [Источник]

```

## kb/templates/template_follow_up.md

```markdown
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
```

## kb/templates/template_interaction.md

```markdown
---
id: "PHARM-INTERACTION-XXX"
title: "Взаимодействие: Препарат A + Препарат B"
domain: "pharm"
category: "interaction"
atc_code: "коды через +"
body_system:
  - "система"
tags:
  - interaction
  - bleeding_risk (и т.д.)
urgency: "urgent | routine"
access_level: "professional"
target_specialist:
  - "all_specialties"
age_group:
  - "all_ages"
evidence_level: "Ia | Ib | IIa | IIb | III | IV"
related:
  - "ID"
sources:
  - "источник"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "approved"
disclaimer: true
---

# Взаимодействие: [Препарат A] + [Препарат B]

> ⚠️ **Уровень значимости**: [критическое / значимое / умеренное / незначительное]

## Участники взаимодействия
- **Препарат A**: [[ID]] МНН
- **Препарат B**: [[ID]] МНН

## Тип взаимодействия
[Фармакокинетическое / Фармакодинамическое / Оба]

## Механизм
[Подробное описание механизма: ферменты, рецепторы и т.д. – 3–7 предложений]

## Клинический эффект
[Что произойдёт при совместном назначении]

## Клинические проявления
- ...

## Рекомендации
### Если комбинация необходима
1. ...
2. ...

### Альтернативы
- Вместо A → [[ID]] альтернатива
- Вместо B → [[ID]] альтернатива

## Доказательная база
- **Уровень доказательности**: 
- **Источник данных**: 

## Связанные взаимодействия
- [[ID]] – связь

## Источники
1. DrugBank / Lexicomp / Vidal
2. Клинические исследования

```

## kb/templates/template_nonpharm.md

```markdown
---
id: "PHARM-NONPHARM-XXX"
title: "[Название метода] – нефармакологическое лечение"
domain: "pharm"
category: "nonpharm"
body_system:
  - "система"
tags:
  - lifestyle
  - diet
  - physiotherapy
access_level: "professional | patient"
target_specialist:
  - "therapist"
  - "специалист"
age_group:
  - "all_ages"
evidence_level: "Ia | IIa"
recommendation_class: "I | IIa"
related:
  - "ID"
sources:
  - "источник"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "approved"
disclaimer: true
---

# [Название метода]

> **Дисклеймер**: Метод не заменяет медикаментозную терапию при наличии показаний.

## Суть метода
[Описание]

## Показания
- ...

## Противопоказания
- ...

## Эффективность (доказательная база)
[Уровень доказательности, ключевые исследования]

## Практическая реализация
[Пошаговое описание для врача / пациента]

## Ожидаемые результаты
- ...

## Побочные эффекты / риски (если есть)
- ...

## Сочетание с медикаментозной терапией
- ...

## Информация для пациента
[Упрощённая версия]

## Связанные документы
- [[ID]] – заболевание

## Источники
1. ...

```

## kb/templates/template_patient_info.md

```markdown
---
id: "PROT-PATIENT_INFO-XXX"
title: "Памятка для пациента: [Состояние]"
domain: "protocols"
category: "patient_info"
body_system:
  - "cardiovascular | respiratory | gastrointestinal | nervous | endocrine | multisystem"
tags:
  - "patient"
  - "education"
urgency: "routine | urgent | emergency"
access_level: "patient"
age_group:
  - "adult | elderly | all_ages"
related:
  - "PROT-PROTOCOL-XXX"
  - "DIAG-DISEASE-XXX"
sources:
  - "Клинические рекомендации"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО врача"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Памятка для пациента: [Состояние]

> ⚠️ Эта информация носит справочный характер и не заменяет консультацию врача.

## Что это за состояние
[Простое объяснение без сложных терминов]

## Основные симптомы
- ...
- ...
- ...

## Что делать сейчас
- ...
- ...
- ...

## Когда нужно срочно обратиться к врачу
- [Тревожный признак 1]
- [Тревожный признак 2]
- [Тревожный признак 3]

## Что нельзя делать
- ...
- ...
- ...

## Общие рекомендации
- режим
- питание
- физическая активность

## Контроль и наблюдение
- когда идти к врачу
- какие анализы сдавать

## Связанные медицинские документы
- [[PROT-PROTOCOL-XXX]]
- [[PROT-ROUTING-XXX]]

## Источники
1. ...
```

## kb/templates/template_protocol.md

```markdown
---
id: "PROT-PROTOCOL-XXX"
title: "Клинический протокол: [Название]"
domain: "protocols"
category: "protocol"
body_system:
  - "cardiovascular | respiratory | gastrointestinal | nervous | endocrine | urinary | multisystem"
tags:
  - "protocol"
  - "clinical"
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "therapist | cardiologist | pulmonologist | gastroenterologist | neurologist | endocrinologist | nephrologist | emergency_physician | all_specialties"
age_group:
  - "adult | elderly | all_ages"
evidence_level: "Ia | Ib | IIa | IIb | III | IV"
recommendation_class: "I | IIa | IIb | III"
related:
  - "DIAG-DISEASE-XXX"
  - "PHARM-REGIMEN-XXX"
sources:
  - "Ссылка или библиографическое описание"
clinical_guidelines:
  - "Название клинических рекомендаций, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО рецензента, специальность"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Клинический протокол: [Название]

> ⚕️ **Дисклеймер**: Документ предназначен для медицинских специалистов.
> Используется как элемент клинической поддержки принятия решений и не заменяет врача.

## Назначение протокола
[Для какой клинической ситуации предназначен данный протокол]

## Область применения
- [Заболевание / синдром / клиническая ситуация]
- [Целевая категория пациентов]
- [Условия использования]

## Входные условия
- [[DIAG-DISEASE-XXX]] [Связанное заболевание]
- [[DIAG-SYMPTOM-XXX]] [Связанный симптом]
- [[DIAG-EXAM-XXX]] [Ключевое обследование]

## Критерии начала применения
- [Критерий 1]
- [Критерий 2]
- [Критерий 3]

## Алгоритм ведения пациента
1. [Шаг 1]
2. [Шаг 2]
3. [Шаг 3]

## Ключевые решения и развилки
- [Условие] → [Решение]
- [Условие] → [Решение]

## Критерии срочности
- **Routine**: [описание]
- **Urgent**: [описание]
- **Emergency**: [описание]

## Связанные маршруты пациента
- [[PROT-ROUTING-XXX]] [Маршрут пациента]

## Связанные шкалы
- [[PROT-SCALE-XXX]] [Шкала оценки]

## Неотложные состояния и действия
- [[PROT-EMERGENCY_P-XXX]] [Алгоритм неотложной помощи]

## Рекомендации по терапии
- [[PHARM-REGIMEN-XXX]] [Схема лечения]
- [[PHARM-DRUG-XXX]] [Препарат]
- [[PHARM-NONPHARM-XXX]] [Немедикаментозный метод]

## Памятка пациенту
- [[PROT-PATIENT_INFO-XXX]] [Памятка пациенту]

## Дальнейшее наблюдение
- [[PROT-FOLLOW_UP-XXX]] [Документ наблюдения]

## Особенности у отдельных групп
- **Пожилые**: [особенности]
- **Беременные**: [особенности]
- **Пациенты с коморбидностью**: [особенности]

## Ограничения применения
- [Ограничение 1]
- [Ограничение 2]

## Связанные документы
- [[ID]] — [тип связи]

## Источники
1. [Клинические рекомендации]
2. [Профессиональное руководство]
3. [Международный гайдлайн]
```

## kb/templates/template_redflag.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "redflag"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "emergency"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# [Название красного флага]

> ⚕️ **Дисклеймер**: Информация носит справочный характер. Красный флаг указывает на необходимость срочной клинической оценки.

## Определение
[Описание опасного симптома или сочетания признаков.]

## Клиническое значение
[Почему признак опасен.]

## Когда возникает
- [Ситуация 1]

## Возможные ассоциированные состояния
- [[DIAG-EMERGENCY-NNN]] [Название]

## Необходимые действия
- [Срочная оценка]
- [Маршрутизация]

## Срочность
Уровень срочности: **emergency / urgent**.

## Связанные обследования
- [[DIAG-EXAM-NNN]] [Метод]

## Связанные документы
- [[DIAG-SYMPTOM-NNN]] — [тип связи]

## Источники
1. [Источник]

```

## kb/templates/template_regimen.md

```markdown
---
id: "PHARM-REGIMEN-XXX"
title: "Схема лечения: [Заболевание/состояние]"
domain: "pharm"
category: "regimen"
body_system:
  - "система"
tags:
  - regimen
  - treatment
urgency: "routine | urgent"
access_level: "professional"
target_specialist:
  - "специалист"
age_group:
  - "adult"
evidence_level: "Ia"
recommendation_class: "I"
related:
  - "ID"
sources:
  - "источник"
clinical_guidelines:
  - "КР, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО"
author: "Инженер знаний №2"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "approved"
disclaimer: true
---

# Схема лечения: [Название заболевания/состояния]

> **Дисклеймер**: Схема приведена для медицинских специалистов. Окончательное решение о терапии принимает лечащий врач.

## Целевая популяция
[Для каких пациентов / стадий заболевания]

## Основные принципы
- ...

## Схема 1-й линии
| Препарат | Дозировка | Путь введения | Длительность | Примечание |
|----------|-----------|----------------|---------------|-------------|
| [[ID]] МНН | ... | ... | ... | ... |

## Альтернативные схемы (2-я линия)
| Препарат | Дозировка | Примечание |
|----------|-----------|-------------|
| ... | ... | ... |

## Комбинированные режимы (если применимо)
- ...

## Мониторинг эффективности
| Параметр | Цель | Частота |
|----------|------|---------|
| ... | ... | ... |

## Критерии перехода на следующую линию
- ...

## Особенности у особых групп
- **Почечная недостаточность**: ...
- **Печёночная недостаточность**: ...
- **Пожилые**: ...

## Связанные документы
- [[ID]] – заболевание
- [[ID]] – протокол

## Источники
1. Клинические рекомендации ...

```

## kb/templates/template_routing.md

```markdown
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
```

## kb/templates/template_scale.md

```markdown
---
id: "PROT-SCALE-XXX"
title: "Клиническая шкала: [Название]"
domain: "protocols"
category: "scale"
body_system:
  - "cardiovascular | respiratory | nervous | endocrine | multisystem"
tags:
  - "scale"
  - "risk_assessment"
urgency: "routine | urgent | emergency"
access_level: "professional"
target_specialist:
  - "therapist | cardiologist | pulmonologist | neurologist | endocrinologist | emergency_physician | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "PROT-PROTOCOL-XXX"
  - "PROT-ROUTING-XXX"
  - "DIAG-DISEASE-XXX"
sources:
  - "Клинические рекомендации"
clinical_guidelines:
  - "Название руководства, год"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: "ФИО рецензента, специальность"
author: "Инженер знаний №3"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft | medical_review | approved"
disclaimer: true
---

# Клиническая шкала: [Название]

> ⚕️ Документ предназначен для формализованной оценки тяжести состояния, риска или прогноза.

## Назначение шкалы
[Для чего используется данная шкала]

## Область применения
- [Клиническая ситуация 1]
- [Клиническая ситуация 2]

## Параметры оценки
| Параметр | Значения | Баллы |
|----------|----------|-------|
| [Параметр 1] | ... | ... |
| [Параметр 2] | ... | ... |
| [Параметр 3] | ... | ... |

## Правила расчёта
1. [Как суммируются баллы]
2. [Какие условия учитывать]
3. [Когда шкала неприменима]

## Интерпретация результата
| Сумма баллов | Категория риска / тяжести | Клиническое значение |
|--------------|----------------------------|----------------------|
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |

## Тактическая значимость
- [Результат 1] → [[PROT-ROUTING-XXX]]
- [Результат 2] → [[PROT-EMERGENCY_P-XXX]]
- [Результат 3] → [[PROT-PROTOCOL-XXX]]

## Ограничения
- [Ограничение 1]
- [Ограничение 2]

## Особенности применения
- **Пожилые**: [особенности]
- **Беременные**: [особенности]
- **Пациенты с коморбидностью**: [особенности]

## Связанные документы
- [[ID]] — [тип связи]

## Источники
1. [Клинические рекомендации]
2. [Руководство / гайдлайн]
3. [Оригинальная публикация шкалы]
```

## kb/templates/template_screening.md

```markdown
---
id: "PROT-SCREENING-XXX"
title: "Скрининг: [Заболевание / состояние]"
domain: "protocols"
category: "screening"
body_system:
  - "cardiovascular | endocrine | oncological | multisystem"
tags:
  - "screening"
  - "prevention"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist | endocrinologist | oncologist | all_specialties"
age_group:
  - "adult | elderly | all_ages"
related:
  - "DIAG-DISEASE-XXX"
  - "PROT-PROTOCOL-XXX"
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

# Скрининг: [Заболевание]

> Документ описывает алгоритм раннего выявления заболевания.

## Целевая группа
- возраст
- факторы риска
- группы пациентов

## Показания к скринингу
- ...

## Методы скрининга
- [[DIAG-EXAM-XXX]]
- лабораторные тесты
- инструментальные методы

## Частота проведения
- ежегодно / раз в X лет

## Интерпретация результатов
- норма → наблюдение
- отклонение → [[PROT-ROUTING-XXX]]

## Дальнейшие действия
- [[PROT-PROTOCOL-XXX]]

## Ограничения
- ...

## Источники
1. ...
```

## kb/templates/template_symptom.md

```markdown
---
id: "DOMAIN-CATEGORY-NNN"
title: "Название единицы знаний"
domain: "diag"
category: "symptom"
icd_10: ""
icd_11: ""
atc_code: ""
inn: ""
body_system:
  - "cardiovascular"
tags:
  - "tag_1"
  - "tag_2"
urgency: "routine"
access_level: "professional"
target_specialist:
  - "therapist"
age_group:
  - "adult"
evidence_level: "IV"
recommendation_class: "I"
related:
  - "DIAG-..."
relations:
  - target: "DIAG-..."
    type: "associated_with"
    description: "Краткое объяснение связи"
sources:
  - "Источник 1: точное название, организация, год/редакция"
clinical_guidelines:
  - "Название клинических рекомендаций, год/редакция"
last_medical_review: "YYYY-MM-DD"
medical_reviewer: ""
author: "Инженер знаний №1"
version: "1.0"
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
status: "draft"
disclaimer: true
---

# [Название симптома / синдрома]

> ⚕️ **Дисклеймер**: Информация носит справочный характер и предназначена для медицинских специалистов. Не является руководством по самолечению.

## Определение
[Клиническое определение симптома / синдрома.]

## Механизм
[Краткое описание механизма возникновения симптома.]

## Характеристики
- **Локализация**: [описание]
- **Интенсивность**: [описание]
- **Динамика**: [описание]
- **Сопутствующие проявления**: [описание]

## Клиническое значение
[Почему симптом важен для диагностики.]

## Ассоциированные заболевания
- [[DIAG-DISEASE-NNN]] [Название]

## 🚩 «Красные флаги»
- [Красный флаг 1]
- [Красный флаг 2]

## Дифференциально-диагностические критерии
| Признак | Возможное направление поиска |
|---|---|
| [Признак] | [Интерпретация] |

## Диагностические направления
- [Осмотр/обследование 1]
- [[DIAG-EXAM-NNN]] [Метод обследования]

## Особенности у отдельных групп
[Дети, пожилые, беременные, коморбидные пациенты — если применимо.]

## Информация для пациента
[Короткое безопасное объяснение без самолечения.]

## Связанные документы
- [[DIAG-DISEASE-NNN]] — [тип связи]

## Источники
1. [Источник]

```

## kb/therapy/adverse_reactions/pharm_adr_nsaid_gi_bleeding.md

```markdown
---
id: PHARM-ADR-001
title: Желудочно-кишечное кровотечение, связанное с приёмом НПВС
domain: pharm
category: adr
body_system:
- gastrointestinal
- hematologic
tags:
- nsaid
- gi_bleeding
- serious
- core
urgency: urgent
access_level: professional
target_specialist:
- therapist
- gastroenterologist
- emergency_physician
- all_specialties
age_group:
- adult
- elderly
evidence_level: Ia
related:
- PHARM-DRUGCLASS-010
sources:
- FDA Adverse Event Reporting System
- Клинические рекомендации по НПВС-гастропатии
last_medical_review: '2025-03-20'
medical_reviewer: Петрова А.А., к.м.н.
author: Инженер знаний №2
version: '1.0'
date_created: '2025-03-15'
date_updated: '2025-03-20'
status: approved
disclaimer: true
clinical_guidelines:
- FDA Adverse Event Reporting System
relations:
- target: PHARM-DRUGCLASS-010
  type: adverse_reaction_for
  description: ЖКТ-кровотечение является серьёзной НЛР для НПВС.
---

# Желудочно-кишечное кровотечение, связанное с приёмом НПВС

> ⚠️ **Серьёзная нежелательная реакция**. Требует немедленной отмены и госпитализации.

## Описание
Кровотечение из верхних или нижних отделов ЖКТ, возникающее на фоне приёма нестероидных противовоспалительных препаратов (НПВС). Наиболее частые источники: эрозии/язвы желудка или двенадцатиперстной кишки, реже – тонкая или толстая кишка. Может проявляться от скрытой кровопотери до массивного геморрагического шока.

## Частота встречаемости
- Госпитализация по поводу НПВС-ассоциированного ЖКТ-кровотечения: 1–2% в год у хронических пользователей НПВС
- Смертность: 5–10% при тяжёлом кровотечении
- Частота выше у пожилых, принимающих НПВС + антикоагулянты/антиагреганты

## Механизм развития
Тип A (augmented – фармакологическое расширение эффекта): ингибирование ЦОГ-1 → снижение синтеза простагландинов (PGE2, PGI2), которые защищают слизистую ЖКТ (уменьшают секрецию кислоты, стимулируют секрецию бикарбонатов и слизи, поддерживают кровоток). В результате – повреждение слизистой, эрозии, язвы, кровотечение.

## Наиболее часто вызывающие препараты (классы)
- [[PHARM-DRUGCLASS-010]] Неселективные НПВС: кеторолак (наибольший риск), индометацин, диклофенак, ибупрофен, напроксен
- Селективные ингибиторы ЦОГ-2 (целекоксиб, эторикоксиб) – риск ниже, но не нулевой
- Аспирин (даже в низких дозах 75–100 мг) – повышает риск ЖКТ-кровотечения в 2–3 раза

## Факторы риска
- Возраст ≥ 65 лет
- Язвенный анамнез или предыдущее ЖКТ-кровотечение
- Одновременный приём антикоагулянтов (варфарин, апиксабан), антиагрегантов (клопидогрел), ГКС
- Длительный приём НПВС (> 30 дней)
- Высокие дозы НПВС
- Инфекция H. pylori
- Тяжёлые сопутствующие заболевания (ХСН, цирроз, ХБП)

## Диагностика
- Клиника: мелена (чёрный дёгтеобразный стул), гематемезис (рвота кровью), геморрагический шок (слабость, бледность, тахикардия, гипотензия)
- Лабораторно: снижение гемоглобина, гематокрита; положительный тест кала на скрытую кровь
- Инструментально: экстренная эзофагогастродуоденоскопия (ЭГДС) – источник кровотечения

## Тактика ведения
1. **Немедленно отменить НПВС** (всегда)
2. Оценить гемодинамику: пульс, АД, диурез
3. При признаках шока – инфузионная терапия (кристаллоиды), при тяжёлой кровопотере – трансфузия эритроцитарной массы
4. **Экстренная ЭГДС** (в течение 24 часов, лучше до 12 часов) – для диагностики и эндоскопического гемостаза (клипирование, коагуляция, инъекция адреналина)
5. **Внутривенное введение ИПП** (омепразол 80 мг болюс, затем 8 мг/ч инфузия 72 ч) для снижения риска рецидива
6. При неэффективности эндоскопического гемостаза – ангиография с эмболизацией или хирургия (прошивание, резекция)

## Профилактика у пациентов, вынужденных принимать НПВС
- Выбор наименее опасного НПВС (ибупрофен ≤ 1200 мг/сут, целекоксиб)
- Назначение гастропротекции: ИПП (омепразол 20 мг/сут) или мизопростол
- Эрадикация H. pylori (если обнаружена) до начала длительной терапии НПВС
- Избегать комбинации НПВС + антикоагулянты + антиагреганты

## Связанные документы
- [[PHARM-DRUGCLASS-010]] – Нестероидные противовоспалительные препараты
- [[PHARM-INTERACTION-001]] – Варфарин + НПВС
- [[PROT-EMERGENCY_P-010]] – Алгоритм при ЖКТ-кровотечении
- [[PHARM-DRUG-045]] – Ибупрофен

## Источники
1. Lanas A. et al. Time trends and impact of upper and lower gastrointestinal bleeding and perforation in clinical practice. Am J Gastroenterol. 2021.
2. Клин рекомендации «НПВС-гастропатия: диагностика и лечение», РГА, 2022.
3. FDA Drug Safety Communication: NSAIDs and GI bleeding.

```

## kb/therapy/dosing/pharm_dosing_ckd.md

```markdown
---
id: PHARM-DOSING-001
title: Коррекция доз антигипертензивных препаратов при хронической болезни почек
domain: pharm
category: dosing
body_system:
- cardiovascular
- urinary
tags:
- ckd
- dosing
- renal
- core
access_level: professional
target_specialist:
- therapist
- nephrologist
- cardiologist
age_group:
- adult
- elderly
evidence_level: IIa
related:
- PHARM-DRUG-001
- PHARM-DRUG-002
- PHARM-REGIMEN-001
sources:
- KDIGO 2024 CKD Guidelines
- Инструкции к препаратам
last_medical_review: '2025-03-25'
medical_reviewer: Сидорова Е.А., д.м.н., нефролог
author: Инженер знаний №2
version: '1.0'
date_created: '2025-03-20'
date_updated: '2025-03-25'
status: approved
disclaimer: true
urgency: routine
clinical_guidelines:
- KDIGO 2024 CKD Guidelines
relations:
- target: PHARM-DRUG-001
  type: dose_adjustment_for
  description: Документ содержит правила коррекции дозы для эналаприла.
- target: PHARM-DRUG-002
  type: dose_adjustment_for
  description: Документ содержит правила коррекции дозы для амлодипина.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Дозирование учитывается при выборе схемы лечения АГ.
---

# Коррекция доз антигипертензивных препаратов при хронической болезни почек

> **Дисклеймер**: Рекомендации основаны на инструкциях и КР. Требуется индивидуальный подход с учётом динамики СКФ и калия.

## Почечная недостаточность
| СКФ (мл/мин/1.73 м²) | Эналаприл (иАПФ) | Амлодипин (БКК) | Индапамид (тиазид) | Спиронолактон (АМКР) |
|----------------------|------------------|-----------------|---------------------|----------------------|
| > 60 | стандартно 5–20 мг/сут | 5–10 мг/сут | 1.5–2.5 мг/сут | 12.5–25 мг/сут |
| 30–60 | 5 мг/сут, титровать | без коррекции | 1.5 мг/сут | 12.5 мг/сут (контроль калия) |
| 15–30 | 2.5–5 мг/сут | без коррекции | противопоказан (петлевой диуретик) | противопоказан (риск гиперкалиемии) |
| < 15 | 2.5 мг/сут или избегать | без коррекции | петлевой (фуросемид) | противопоказан |

**Примечания:**
- **иАПФ** – снижение дозы обязательно при СКФ < 30; при СКФ 15–30 – риск ухудшения функции, контролировать креатинин и калий.
- **БКК (дигидропиридиновые)** – не требуют коррекции, но при СКФ < 15 накапливаются активные метаболиты (теоретический риск).
- **Тиазидные диуретики** – неэффективны при СКФ < 30; замена на петлевые (фуросемид, торасемид).
- **Антагонисты минералокортикоидных рецепторов (спиронолактон, эплеренон)** – противопоказаны при СКФ < 30 или калии > 5.0 ммоль/л.

## Печёночная недостаточность (для препаратов с печёночным метаболизмом)
| Класс Child-Pugh | Амлодипин | Эналаприл | Спиронолактон |
|------------------|-----------|-----------|----------------|
| A (лёгкая) | без коррекции | без коррекции | 12.5–25 мг/сут |
| B (средняя) | начальная 2.5 мг/сут, макс 5 мг/сут | начальная 2.5 мг/сут | 12.5 мг/сут (осторожно) |
| C (тяжёлая) | 2.5 мг/сут (или избегать) | 2.5 мг/сут (избегать) | противопоказан |

## Пожилой возраст (≥ 65 лет)
- Начинать с **половинных** начальных доз:
  - Эналаприл: 2.5 мг/сут
  - Амлодипин: 2.5 мг/сут
  - Индапамид: 1.5 мг/сут (при СКФ > 45)
- Титровать дозу медленно (каждые 4–6 недель)
- Контролировать ортостатическую гипотензию (особенно на диуретиках)

## Дети (для АГ у детей, off-label)
- Эналаприл: начальная 0.08 мг/кг 1 раз/сут, макс 0.6 мг/кг (но не более 20 мг/сут)
- Амлодипин: начальная 0.1–0.2 мг/кг/сут, макс 5 мг/сут (для детей < 6 лет), 10 мг/сут (6–17 лет)

## Беременность и лактация
- иАПФ, БРА, спиронолактон – **противопоказаны** (тератогенность, фетотоксичность)
- БКК (амлодипин) – только при отсутствии альтернативы, данные ограничены
- β-блокаторы (метопролол, лабеталол) – допустимы

## Связанные документы
- [[DIAG-DISEASE-008]] – Хроническая болезнь почек
- [[PHARM-DRUG-001]] – Эналаприл
- [[PHARM-DRUG-002]] – Амлодипин
- [[GLB-PROFILE-004]] – Профиль: пациент с ХБП

## Источники
1. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease.
2. Инструкции по медицинскому применению препаратов (ГРЛС, 2025).
3. Clinical Pharmacokinetics and Pharmacodynamics of Antihypertensive Drugs in CKD. Clin J Am Soc Nephrol. 2022.

```

## kb/therapy/drug_classes/pharm_drugclass_ace_inhibitors.md

```markdown
---
id: PHARM-DRUGCLASS-001
title: Ингибиторы ангиотензинпревращающего фермента (иАПФ)
domain: pharm
category: drugclass
atc_code: C09AA
body_system:
- cardiovascular
tags:
- ace_inhibitor
- antihypertensive
- cardiology
- core
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
- PHARM-DRUG-001
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
sources:
- Клинические рекомендации по АГ, 2024
- 2023 ESH Guidelines
last_medical_review: '2025-03-01'
medical_reviewer: Иванов И.И., д.м.н.
author: Инженер знаний №2
version: '1.0'
date_created: '2025-02-20'
date_updated: '2025-03-01'
status: approved
disclaimer: true
urgency: routine
clinical_guidelines:
- Клинические рекомендации по АГ, 2024
relations:
- target: PHARM-DRUG-001
  type: class_contains_drug
  description: Эналаприл является представителем группы иАПФ.
- target: DIAG-DISEASE-001
  type: used_for
  description: Группа применяется при артериальной гипертензии.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Группа используется в схеме лечения АГ.
---

# Ингибиторы ангиотензинпревращающего фермента (иАПФ)

> **Дисклеймер**: Информация предназначена для медицинских специалистов.

## Общая характеристика
иАПФ – одна из основных групп антигипертензивных препаратов. Обладают также органопротективным действием (кардио-, нефро-, вазопротекция). Являются препаратами первой линии при АГ, ХСН, хронической болезни почек с протеинурией, после инфаркта миокарда.

## Механизм действия (общий для группы)
Ингибирование АПФ → снижение образования ангиотензина II → уменьшение вазоконстрикции и секреции альдостерона → снижение ОПСС, уменьшение задержки натрия и воды, снижение преднагрузки. Также иАПФ увеличивают уровень брадикинина, что способствует дополнительной вазодилатации, но вызывает сухой кашель.

## Представители группы
| МНН | Торговые названия | Особенности |
|-----|------------------|-------------|
| Эналаприл | Энап, Ренитек | пролекарство, активный метаболит эналаприлат |
| Лизиноприл | Диротон, Лизинотон | не пролекарство, гидрофильный |
| Периндоприл | Престариум | пролекарство, длительное действие |
| Рамиприл | Тритаце, Амприлан | пролекарство, доказана эффективность при ХСН |
| Фозиноприл | Моноприл | двойной путь элиминации (печень+почки) |

## Сравнительная характеристика
| Параметр | Эналаприл | Лизиноприл | Периндоприл | Рамиприл |
|----------|-----------|------------|-------------|----------|
| Длительность действия | 12–24 ч | 24 ч | 24 ч | 24 ч |
| Путь элиминации | почки | почки | почки | почки |
| Необходимость коррекции при ХБП | да | да | да | да |
| Частота кашля | ~10% | ~10% | ~5-8% | ~10% |
| Доказанная польза при ХСН | да | да | да | да |

## Общие показания
- Артериальная гипертензия (I класс, уровень Ia)
- Хроническая сердечная недостаточность (I класс)
- Постинфарктный период (снижение ремоделирования ЛЖ)
- Хроническая болезнь почек с протеинурией (нефропротекция)
- Профилактика повторного инсульта

## Общие противопоказания
- Ангионевротический отёк в анамнезе (на любые иАПФ)
- Беременность (категория D)
- Двусторонний стеноз почечных артерий
- Гиперкалиемия >5.5 ммоль/л

## Общие побочные эффекты
- Сухой кашель (наиболее частый, до 20%)
- Гипотензия (особенно первый приём)
- Гиперкалиемия (особенно при ХБП + калийсберегающие диуретики)
- Повышение креатинина (обратимое)
- Ангионевротический отёк (редко, но опасно)

## Клинически значимые взаимодействия
- Калийсберегающие диуретики → риск гиперкалиемии
- НПВС → снижение антигипертензивного эффекта, риск ОПП
- Литий → повышение уровня лития (токсичность)
- Алискирен → удвоение риска гиперкалиемии и гипотензии

## Особенности выбора
- При ХБП с протеинурией: иАПФ с преимущественно почечной элиминацией (лизиноприл) или с двойным путём (фозиноприл)
- При ХСН: эналаприл, рамиприл, периндоприл (доказанная база)
- При кашле: замена на БРА (лозартан и др.)
- У пожилых: начинать с малых доз (2.5 мг эналаприла)

## Связанные документы
- [[PHARM-DRUG-001]] – Эналаприл
- [[DIAG-DISEASE-001]] – Артериальная гипертензия
- [[DIAG-DISEASE-003]] – Хроническая сердечная недостаточность
- [[PHARM-INTERACTION-001]] – иАПФ + НПВС

## Источники
1. Клинические рекомендации «Артериальная гипертензия у взрослых», 2024
2. 2023 ESH Guidelines for the management of arterial hypertension
3. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure

```

## kb/therapy/drug_classes/pharm_drugclass_arb.md

```markdown
---
id: PHARM-DRUGCLASS-002
title: Блокаторы рецепторов ангиотензина II (БРА)
domain: pharm
category: drugclass
atc_code: C09CA
body_system:
- cardiovascular
tags:
- arb
- antihypertensive
- cardiology
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
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
relations:
- target: DIAG-DISEASE-001
  type: used_for
  description: Группа используется при АГ.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Группа входит в варианты схемы лечения АГ.
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

# Блокаторы рецепторов ангиотензина II (БРА)

> Служебная интеграционная карточка для связности фармакологического контура.

## Назначение
Карточка фиксирует фармакологическую группу, которая используется в схеме терапии артериальной гипертензии как альтернатива ингибиторам АПФ.

## Связанные документы
- [[DIAG-DISEASE-001]] Артериальная гипертензия.
- [[PHARM-REGIMEN-001]] Схема лечения артериальной гипертензии.

```

## kb/therapy/drug_classes/pharm_drugclass_calcium_channel_blockers.md

```markdown
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

```

## kb/therapy/drug_classes/pharm_drugclass_nsaids.md

```markdown
---
id: PHARM-DRUGCLASS-010
title: Нестероидные противовоспалительные препараты (НПВС)
domain: pharm
category: drugclass
atc_code: M01A
body_system:
- musculoskeletal
- gastrointestinal
tags:
- nsaid
- pain
- gi_bleeding
- support
urgency: urgent
access_level: professional
target_specialist:
- therapist
- gastroenterologist
- all_specialties
age_group:
- adult
- elderly
evidence_level: Ia
related:
- PHARM-ADR-001
relations:
- target: PHARM-ADR-001
  type: may_cause_adr
  description: НПВС могут повышать риск желудочно-кишечного кровотечения.
sources:
- Клинические рекомендации по НПВС-гастропатии
clinical_guidelines:
- Клинические рекомендации по НПВС-гастропатии
author: Инженер знаний №2
status: medical_review
last_medical_review: '2026-04-09'
medical_reviewer: —
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
disclaimer: true
---

# Нестероидные противовоспалительные препараты (НПВС)

> Служебная интеграционная карточка для связи с нежелательной лекарственной реакцией.

## Назначение
Карточка используется для демонстрации связи фармакологической группы с серьёзной нежелательной реакцией.

## Связанные документы
- [[PHARM-ADR-001]] Желудочно-кишечное кровотечение, связанное с приёмом НПВС.

```

## kb/therapy/drug_classes/pharm_drugclass_thiazide_diuretics.md

```markdown
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

```

## kb/therapy/drugs/pharm_drug_amlodipine.md

```markdown
---
id: PHARM-DRUG-002
title: Амлодипин – Норваск, Амлотоп, Тенокс
domain: pharm
category: drug
atc_code: C08CA01
inn: Amlodipine
body_system:
- cardiovascular
tags:
- calcium_channel_blocker
- antihypertensive
- antianginal
- core
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
- elderly
evidence_level: Ia
recommendation_class: I
related:
- PHARM-DRUGCLASS-003
- DIAG-DISEASE-001
- DIAG-DISEASE-002
- PHARM-REGIMEN-001
sources:
- Инструкция по медицинскому применению амлодипина
- Клинические рекомендации «Артериальная гипертензия», 2024
clinical_guidelines:
- АГ, 2024
last_medical_review: '2025-03-15'
medical_reviewer: Иванов И.И., д.м.н., кардиолог
author: Инженер знаний №2
version: '1.0'
date_created: '2025-03-10'
date_updated: '2025-03-15'
status: approved
disclaimer: true
relations:
- target: PHARM-DRUGCLASS-003
  type: belongs_to_class
  description: Амлодипин относится к блокаторам кальциевых каналов.
- target: DIAG-DISEASE-001
  type: used_for
  description: Применяется при артериальной гипертензии по назначению врача.
- target: DIAG-DISEASE-002
  type: used_for
  description: Может применяться при хронической ишемической болезни сердца по назначению врача.
- target: PHARM-REGIMEN-001
  type: drug_in_regimen
  description: Может входить в антигипертензивную схему.
---

# Амлодипин – Норваск, Амлотоп, Тенокс

> **Дисклеймер**: Назначение, изменение дозы и отмена препарата выполняются только врачом.

## Общие сведения
- **МНН**: Амлодипин
- **АТС-код**: C08CA01
- **Фармакологическая группа**: [[PHARM-DRUGCLASS-003]] Блокаторы кальциевых каналов (дигидропиридиновые)
- **Рецептурный статус**: рецептурный
- **Формы выпуска**: таблетки 2.5 мг, 5 мг, 10 мг

## Механизм действия
Амлодипин – дигидропиридиновый блокатор L-типа кальциевых каналов. Снижает трансмембранный поток ионов кальция в гладкомышечные клетки сосудов и кардиомиоциты. В сосудах вызывает выраженную вазодилатацию (артериолы > вены), снижает ОПСС, что приводит к снижению АД. В терапевтических дозах не влияет на проводимость и сократимость миокарда, не вызывает рефлекторную тахикардию благодаря медленному развитию эффекта.

## Фармакокинетика
| Параметр | Значение |
|----------|----------|
| Биодоступность | 64–90% |
| Связь с белками плазмы | 97–98% |
| Метаболизм | печёночный (CYP3A4) |
| Период полувыведения (T½) | 30–50 часов |
| Элиминация | почечная (60% метаболитов) |
| Начало действия | 6–12 часов |
| Пик действия | 6–12 часов (плато) |

## Показания
1. Артериальная гипертензия (моно- или комбинированная терапия) – Ia, I
2. Стабильная стенокардия (хроническая) – Ib, I
3. Вазоспастическая стенокардия (Принцметала) – Ib, I

## Дозирование
### Стандартное дозирование (взрослые)
| Показание | Доза | Кратность | Путь введения | Длительность |
|-----------|------|-----------|----------------|---------------|
| АГ | 5–10 мг | 1 раз/сут | перорально | постоянно |
| Стенокардия | 5–10 мг | 1 раз/сут | перорально | постоянно |

### Коррекция дозы
| Группа | Рекомендация |
|--------|---------------|
| Почечная недостаточность (любая СКФ) | коррекция не требуется (не выводится почками) |
| Печёночная недостаточность (Child-Pugh B/C) | начальная 2.5 мг/сут, титровать медленно |
| Пожилые (≥ 65 лет) | начальная 2.5 мг/сут |
| Дети | 2.5–5 мг 1 раз/сут (только для АГ, off-label) |

## Противопоказания
### Абсолютные
- Гиперчувствительность к дигидропиридинам
- Тяжёлая гипотензия (САД < 90 мм рт. ст.)
- Шок (в т.ч. кардиогенный)
- Гемодинамически нестабильная сердечная недостаточность (декомпенсация)

### Относительные
- Стеноз аорты (тяжёлый)
- Печёночная недостаточность (риск кумуляции)

## Побочные эффекты
### Частые (> 10%)
- Отёки лодыжек (периферические отёки) – 10–15%
- Головная боль, головокружение

### Нечастые (1–10%)
- Приливы жара, покраснение лица
- Сердцебиение (незначительная тахикардия)
- Утомляемость, сонливость

### Редкие, но серьёзные (< 1%)
- Гиперплазия дёсен (при длительном приёме)
- Повышение уровня печёночных ферментов
- Эксфолиативный дерматит (очень редко)

## Лекарственные взаимодействия
### Клинически значимые
| Препарат / группа | Тип взаимодействия | Эффект | Рекомендация |
|------------------|--------------------|--------|---------------|
| Ингибиторы CYP3A4 (кетоконазол, кларитромицин) | фармакокинетическое | повышение концентрации амлодипина, гипотензия | уменьшить дозу амлодипина |
| Индукторы CYP3A4 (рифампицин, карбамазепин) | фармакокинетическое | снижение эффективности | увеличить дозу (под контролем АД) |
| Грейпфрутовый сок | фармакокинетическое | повышение концентрации до 2 раз | избегать приёма сока |

## Взаимодействие с пищей / алкоголем
- Грейпфрутовый сок противопоказан
- Алкоголь потенцирует гипотензивный эффект

## Беременность и лактация
- **Категория FDA**: C
- **Беременность**: назначают только по строгим показаниям (недостаточно исследований)
- **Лактация**: выделяется с молоком – при необходимости приёма прекратить грудное вскармливание

## Мониторинг терапии
| Параметр | Частота контроля | Целевое значение |
|----------|------------------|------------------|
| АД | ежемесячно до цели, затем 1 раз в 3–6 мес | <130/80 |
| Отёки | при каждом визите | отсутствие или лёгкие |
| Функция печени | 1 раз в 6 мес (АЛТ, АСТ) | норма |

## Передозировка
- **Симптомы**: выраженная гипотензия, рефлекторная тахикардия, шок
- **Антидот**: нет (глюконат кальция в/в может частично антагонизировать)
- **Тактика**: промывание желудка, активированный уголь, вазопрессоры (допамин)

## Сравнение с аналогами в группе
| Критерий | Амлодипин | Нифедипин (ретард) | Лацидипин |
|----------|-----------|---------------------|------------|
| Эффективность | высокая | высокая | средняя |
| Безопасность | отёки (дозозависимо) | отёки + тахикардия | меньше отёков |
| Стоимость | средняя | низкая | высокая |
| Удобство приёма | 1 раз/сут | 1–2 раза/сут | 1 раз/сут |

## Информация для пациента
Амлодипин снижает давление и предотвращает приступы стенокардии. Принимайте его один раз в день, в одно и то же время, независимо от еды. Не жуйте таблетку. Эффект развивается постепенно в течение 6–12 часов. Не прекращайте приём резко. Если появились отёки на ногах, сообщите врачу – возможно, потребуется снизить дозу или добавить иАПФ. Избегайте грейпфрутового сока – он усиливает действие и риск побочных эффектов.

## Связанные документы
- [[PHARM-DRUGCLASS-003]] – Блокаторы кальциевых каналов
- [[DIAG-DISEASE-001]] – Артериальная гипертензия
- [[DIAG-DISEASE-002]] – ИБС, стенокардия

## Источники
1. Инструкция по медицинскому применению амлодипина (РЛС, 2024)
2. Клинические рекомендации «Артериальная гипертензия у взрослых», 2024
3. 2023 ESH Guidelines for the management of arterial hypertension

```

## kb/therapy/drugs/pharm_drug_enalapril.md

```markdown
---
id: PHARM-DRUG-001
title: Эналаприл – Энап, Ренитек, Берлиприл
domain: pharm
category: drug
atc_code: C09AA02
inn: Enalapril
body_system:
- cardiovascular
tags:
- ace_inhibitor
- antihypertensive
- cardiology
- core
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
recommendation_class: I
related:
- PHARM-DRUGCLASS-001
- DIAG-DISEASE-001
- PHARM-REGIMEN-001
sources:
- Инструкция по медицинскому применению эналаприла
- Клинические рекомендации «Артериальная гипертензия у взрослых», 2024
clinical_guidelines:
- Артериальная гипертензия у взрослых, 2024
last_medical_review: '2025-03-15'
medical_reviewer: Иванов И.И., д.м.н., кардиолог
author: Инженер знаний №2
version: '1.0'
date_created: '2025-03-10'
date_updated: '2025-03-15'
status: approved
disclaimer: true
relations:
- target: PHARM-DRUGCLASS-001
  type: belongs_to_class
  description: Эналаприл относится к ингибиторам АПФ.
- target: DIAG-DISEASE-001
  type: used_for
  description: Применяется в терапии артериальной гипертензии по назначению врача.
- target: PHARM-REGIMEN-001
  type: drug_in_regimen
  description: Может входить в антигипертензивную схему.
---

# Эналаприл – Энап, Ренитек, Берлиприл

> **Дисклеймер**: Назначение, изменение дозы и отмена препарата выполняются только врачом.

## Общие сведения
- **МНН**: Эналаприл
- **АТС-код**: C09AA02
- **Фармакологическая группа**: [[PHARM-DRUGCLASS-001]] Ингибиторы АПФ
- **Рецептурный статус**: рецептурный
- **Формы выпуска**: таблетки 2.5 мг, 5 мг, 10 мг, 20 мг; раствор для инъекций (в/в)

## Механизм действия
Эналаприл – пролекарство, в печени гидролизуется до активного метаболита эналаприлата. Ингибирует ангиотензинпревращающий фермент (АПФ), что приводит к снижению образования ангиотензина II, уменьшению секреции альдостерона, расширению артериол и снижению общего периферического сосудистого сопротивления (ОПСС). Также снижает преднагрузку за счёт венодилатации. Не влияет на ЧСС.

## Фармакокинетика
| Параметр | Значение |
|----------|----------|
| Биодоступность | ~60% (всасывается 60–70%) |
| Связь с белками плазмы | 50–60% |
| Метаболизм | печёночный (гидролиз до эналаприлата) |
| Период полувыведения (T½) | 11 часов (эналаприлат) |
| Элиминация | почечная (94%) |
| Начало действия | 1 час |
| Пик действия | 4–6 часов |

## Показания
1. Артериальная гипертензия – уровень Ia, класс I
2. Хроническая сердечная недостаточность (в составе комбинированной терапии) – Ia, I
3. Бессимптомная дисфункция левого желудочка – Ia, I
4. Профилактика сердечной недостаточности у пациентов с дисфункцией ЛЖ – Ib, I

## Дозирование
### Стандартное дозирование (взрослые)
| Показание | Доза | Кратность | Путь введения | Длительность |
|-----------|------|-----------|----------------|---------------|
| АГ | 5–20 мг | 1–2 раза/сут | перорально | постоянно |
| ХСН | 2.5 мг (начальная) → 10–20 мг | 2 раза/сут | перорально | постоянно |

### Коррекция дозы
| Группа | Рекомендация |
|--------|---------------|
| Почечная недостаточность (СКФ < 30) | начальная 2.5 мг/сут, титровать медленно |
| Печёночная недостаточность (Child-Pugh C) | начальная 2.5 мг/сут, контроль |
| Пожилые (≥ 65 лет) | начинать с 2.5–5 мг/сут |
| Дети | не рекомендуется (безопасность не установлена) |

## Противопоказания
### Абсолютные
- Ангионевротический отёк в анамнезе (на фоне приёма иАПФ)
- Беременность (тератогенность)
- Двусторонний стеноз почечных артерий
- Гиперкалиемия (>5.5 ммоль/л)

### Относительные
- Стеноз аорты/митрального клапана
- Гипертрофическая кардиомиопатия
- Системные заболевания соединительной ткани (повышенный риск нейтропении)

## Побочные эффекты
### Частые (> 10%)
- Сухой кашель (10–20%)
- Гипотензия (особенно при первом приёме)

### Нечастые (1–10%)
- Головокружение, головная боль
- Гиперкалиемия
- Обратимое повышение креатинина

### Редкие, но серьёзные (< 1%)
- Ангионевротический отёк (язык, гортань) – требует немедленной отмены и введения адреналина
- Нейтропения / агранулоцитоз
- Острая почечная недостаточность (при двустороннем стенозе почечных артерий)

## Лекарственные взаимодействия
### Клинически значимые
| Препарат / группа | Тип взаимодействия | Эффект | Рекомендация |
|------------------|--------------------|--------|---------------|
| Калийсберегающие диуретики (спиронолактон) | фармакодинамическое | тяжёлая гиперкалиемия | избегать комбинации |
| НПВС | фармакодинамическое | снижение антигипертензивного эффекта, риск ОПП | контроль АД и креатинина |
| Литий | фармакокинетическое | повышение уровня лития (токсичность) | контролировать уровень лития |

## Взаимодействие с пищей / алкоголем
- Пища умеренно снижает всасывание (не клинически значимо)
- Алкоголь потенцирует гипотензивный эффект – избегать

## Беременность и лактация
- **Категория FDA**: D (противопоказан)
- **Беременность**: тератогенен (нарушение развития почек плода, олигогидрамнион)
- **Лактация**: проникает в грудное молоко – при необходимости отменить грудное вскармливание

## Мониторинг терапии
| Параметр | Частота контроля | Целевое значение |
|----------|------------------|------------------|
| АД | еженедельно до цели, затем 1 раз в 3–6 мес | <130/80 |
| Креатинин, калий | через 2–4 недели после начала/титрования, затем 1 раз в 6–12 мес | креатинин – стабильно, калий <5.0 |

## Передозировка
- **Симптомы**: выраженная гипотензия, брадикардия, шок
- **Антидот**: нет (гемодиализ эффективен)
- **Тактика**: промывание желудка, в/в введение жидкости, атропин при брадикардии

## Сравнение с аналогами в группе
| Критерий | Эналаприл | Лизиноприл | Периндоприл |
|----------|-----------|------------|--------------|
| Эффективность | хорошая | хорошая | хорошая |
| Безопасность | кашель + | кашель + | кашель + (реже) |
| Стоимость | низкая | средняя | высокая |
| Удобство приёма | 1–2 раза/сут | 1 раз/сут | 1 раз/сут |

## Информация для пациента
Эналаприл назначают для снижения давления и лечения сердечной недостаточности. Принимайте его каждый день в одно и то же время, независимо от еды. Не прекращайте приём резко – это может вызвать скачок давления. Если появился сухой кашель, отёк губ или лица – немедленно обратитесь к врачу. Избегайте алкоголя. Регулярно измеряйте давление и сдавайте анализ крови (калий, креатинин).

## Связанные документы
- [[PHARM-DRUGCLASS-001]] – Ингибиторы АПФ
- [[DIAG-DISEASE-001]] – Артериальная гипертензия
- [[PHARM-REGIMEN-001]] – Схема лечения АГ
- [[PROT-PATIENT_INFO-001]] – Памятка по АГ

## Источники
1. Инструкция по медицинскому применению эналаприла (РЛС, 2024)
2. Клинические рекомендации «Артериальная гипертензия у взрослых», Минздрав РФ, 2024
3. Harrison's Principles of Internal Medicine, 21st ed., 2022

```

## kb/therapy/drugs/pharm_drug_metformin.md

```markdown
---
id: PHARM-DRUG-020
title: Метформин
domain: pharm
category: drug
atc_code: A10BA02
inn: Metformin
body_system:
- endocrine
tags:
- metformin
- diabetes
- interaction
- support
urgency: routine
access_level: professional
target_specialist:
- therapist
- endocrinologist
- nephrologist
age_group:
- adult
- elderly
evidence_level: Ia
recommendation_class: I
related:
- PHARM-INTERACTION-001
relations:
- target: PHARM-INTERACTION-001
  type: has_interaction
  description: Метформин имеет клинически значимое взаимодействие с йодсодержащими контрастными веществами.
sources:
- Инструкция по медицинскому применению метформина
- ESUR Guidelines on Contrast Media, 2018
clinical_guidelines:
- ESUR Guidelines on Contrast Media, 2018
author: Инженер знаний №2
status: medical_review
last_medical_review: '2026-04-09'
medical_reviewer: —
version: '1.0'
date_created: '2026-04-09'
date_updated: '2026-04-09'
disclaimer: true
---

# Метформин

> Служебная интеграционная карточка для связи с карточкой лекарственного взаимодействия.

## Назначение
Карточка используется для демонстрации проверки фармакологических связей в MVP.

## Связанные документы
- [[PHARM-INTERACTION-001]] Метформин + йодсодержащие контрастные вещества.

```

## kb/therapy/index.md

```markdown
# Индекс фармакологического контура MedAssist

Индекс содержит карточки предметной области «Фармакология и терапия»: препараты, фармакологические группы, терапевтическую схему, коррекцию доз, взаимодействие, нежелательную реакцию и немедикаментозный метод.

| ID | Название | Категория | Срочность | Файл |
|---|---|---|---|---|
| `PHARM-ADR-001` | Желудочно-кишечное кровотечение, связанное с приёмом НПВС | `adr` | `urgent` | `adverse_reactions/pharm_adr_nsaid_gi_bleeding.md` |
| `PHARM-DOSING-001` | Коррекция доз антигипертензивных препаратов при хронической болезни почек | `dosing` | `routine` | `dosing/pharm_dosing_ckd.md` |
| `PHARM-DRUG-001` | Эналаприл – Энап, Ренитек, Берлиприл | `drug` | `routine` | `drugs/pharm_drug_enalapril.md` |
| `PHARM-DRUG-002` | Амлодипин – Норваск, Амлотоп, Тенокс | `drug` | `routine` | `drugs/pharm_drug_amlodipine.md` |
| `PHARM-DRUG-020` | Метформин | `drug` | `routine` | `drugs/pharm_drug_metformin.md` |
| `PHARM-DRUGCLASS-001` | Ингибиторы ангиотензинпревращающего фермента (иАПФ) | `drugclass` | `routine` | `drug_classes/pharm_drugclass_ace_inhibitors.md` |
| `PHARM-DRUGCLASS-002` | Блокаторы рецепторов ангиотензина II (БРА) | `drugclass` | `routine` | `drug_classes/pharm_drugclass_arb.md` |
| `PHARM-DRUGCLASS-003` | Блокаторы кальциевых каналов | `drugclass` | `routine` | `drug_classes/pharm_drugclass_calcium_channel_blockers.md` |
| `PHARM-DRUGCLASS-004` | Тиазидные и тиазидоподобные диуретики | `drugclass` | `routine` | `drug_classes/pharm_drugclass_thiazide_diuretics.md` |
| `PHARM-DRUGCLASS-010` | Нестероидные противовоспалительные препараты (НПВС) | `drugclass` | `urgent` | `drug_classes/pharm_drugclass_nsaids.md` |
| `PHARM-INTERACTION-001` | Взаимодействие: Метформин + йодсодержащие контрастные вещества | `interaction` | `urgent` | `interactions/pharm_interaction_metformin_contrast.md` |
| `PHARM-NONPHARM-001` | Диета DASH – диетический подход к остановке гипертензии | `nonpharm` | `routine` | `nonpharm/pharm_nonpharm_dash_diet.md` |
| `PHARM-REGIMEN-001` | Схема лечения артериальной гипертензии | `regimen` | `routine` | `regimens/pharm_regimen_hypertension.md` |

```

## kb/therapy/interactions/pharm_interaction_metformin_contrast.md

```markdown
---
id: PHARM-INTERACTION-001
title: 'Взаимодействие: Метформин + йодсодержащие контрастные вещества'
domain: pharm
category: interaction
atc_code: A10BA02 + V08A
body_system:
- endocrine
- urinary
tags:
- metformin
- contrast_media
- lactic_acidosis
- core
urgency: urgent
access_level: professional
target_specialist:
- endocrinologist
- radiologist
- therapist
- nephrologist
age_group:
- adult
- elderly
evidence_level: IIa
related:
- PHARM-DRUG-020
sources:
- Инструкция к метформину
- ESUR Guidelines on Contrast Media, 2018
last_medical_review: '2025-02-10'
medical_reviewer: Петрова А.А., к.м.н., клинический фармаколог
author: Инженер знаний №2
version: '1.0'
date_created: '2025-02-05'
date_updated: '2025-02-10'
status: approved
disclaimer: true
clinical_guidelines:
- Инструкция к метформину
relations:
- target: PHARM-DRUG-020
  type: interaction_for
  description: Взаимодействие описывает риск при применении метформина с йодсодержащим контрастом.
---

# Взаимодействие: Метформин + йодсодержащие контрастные вещества

> ⚠️ **Уровень значимости**: КРИТИЧЕСКОЕ

## Участники взаимодействия
- **Препарат A**: [[PHARM-DRUG-020]] Метформин
- **Препарат B**: Йодсодержащие рентгеноконтрастные вещества (йогексол, йопромид, йодиксанол и др.)

## Тип взаимодействия
Фармакокинетическое (почечное) + фармакодинамическое (метаболическое)

## Механизм
Йодсодержащие контрастные вещества могут вызывать контраст-индуцированную нефропатию (КИН) – острое снижение СКФ за счёт вазоконстрикции и прямого тубулярного повреждения. Метформин выводится почками в неизменённом виде. При снижении СКФ происходит кумуляция метформина, что на фоне тканевой гипоксии (характерной для пациентов с диабетом и ССЗ) повышает риск развития лактат-ацидоза – жизнеугрожающего осложнения (летальность до 50%).

## Клинический эффект
Повышение риска лактат-ацидоза (тошнота, рвота, боль в животе, мышечные судороги, гипервентиляция, спутанность сознания, снижение pH крови, повышение лактата >5 ммоль/л).

## Клинические проявления
- Слабость, тошнота, рвота, диарея
- Боли в животе, мышечные судороги
- Тахипноэ (дыхание Куссмауля)
- Гипотензия, аритмии
- Спутанность сознания → кома

## Рекомендации
### Если комбинация необходима (т.е. требуется введение йодсодержащего контраста у пациента, принимающего метформин)

**Для пациентов с нормальной функцией почек (СКФ ≥ 60 мл/мин/1.73 м²):**
1. Отменить метформин за 48 часов до введения контраста (или в день процедуры, если СКФ нормальная, по некоторым протоколам – за 24 ч)
2. После введения контраста – не возобновлять метформин в течение 48 часов
3. Через 48 часов после введения контраста – оценить СКФ
4. Если СКФ осталась ≥ 60 – возобновить метформин

**Для пациентов с ХБП (СКФ < 60 мл/мин/1.73 м²) или с факторами риска КИН (возраст > 75, СД, дегидратация, ССЗ):**
1. Отменить метформин за 48 часов до введения контраста
2. Обеспечить гидратацию (в/в физиологический раствор до и после процедуры)
3. Использовать низкоосмолярные или изоосмолярные контрасты в минимальной дозе
4. После введения контраста – не возобновлять метформин в течение 48–72 часов
5. Оценить СКФ – возобновить только при стабильной или исходной функции

### Альтернативы
- Вместо йодсодержащего контраста (при возможности) – МРТ с гадолинием (но при СКФ < 30 гадолиний также противопоказан из-за риска нефрогенного системного фиброза)
- Вместо метформина (временно) – инсулин короткого действия (на время процедуры и восстановления функции почек)

## Доказательная база
- **Уровень доказательности**: IIa (консенсус экспертов, клинические руководства)
- **Источник данных**: ESUR Guidelines on Contrast Media (v10.0, 2018), рекомендации FDA, KDIGO

## Связанные взаимодействия
- [[PHARM-INTERACTION-002]] – Метформин + алкоголь (лактат-ацидоз)

## Источники
1. Инструкция по медицинскому применению метформина
2. ESUR Guidelines on Contrast Media, 2018 (Version 10.0)
3. KDIGO 2020 Clinical Practice Guideline for Diabetes Management in CKD

```

## kb/therapy/nonpharm/pharm_nonpharm_dash_diet.md

```markdown
---
id: PHARM-NONPHARM-001
title: Диета DASH – диетический подход к остановке гипертензии
domain: pharm
category: nonpharm
body_system:
- cardiovascular
tags:
- diet
- lifestyle
- hypertension
- core
access_level: professional
target_specialist:
- therapist
- cardiologist
- dietitian
age_group:
- adult
- elderly
evidence_level: Ia
recommendation_class: I
related:
- DIAG-DISEASE-001
- PROT-PATIENT_INFO-001
- PHARM-REGIMEN-001
sources:
- DASH Collaborative Research Group, NEJM 1997
- 2023 ESH Guidelines
last_medical_review: '2025-03-10'
medical_reviewer: Иванов И.И., д.м.н., кардиолог
author: Инженер знаний №2
version: '1.0'
date_created: '2025-03-05'
date_updated: '2025-03-10'
status: approved
disclaimer: true
urgency: routine
clinical_guidelines:
- DASH Collaborative Research Group, NEJM 1997
relations:
- target: DIAG-DISEASE-001
  type: nonpharm_for
  description: Диета DASH применяется как немедикаментозный подход при АГ.
- target: PROT-PATIENT_INFO-001
  type: patient_info_for
  description: Памятка пациента может ссылаться на рекомендации по образу жизни.
- target: PHARM-REGIMEN-001
  type: used_by_regimen
  description: Немедикаментозные меры дополняют антигипертензивную схему.
---

# Диета DASH – диетический подход к остановке гипертензии

> **Дисклеймер**: Метод не заменяет медикаментозную терапию при наличии показаний. Является обязательной частью немедикаментозного лечения АГ.

## Суть метода
DASH (Dietary Approaches to Stop Hypertension) – диета, богатая овощами, фруктами, цельнозерновыми продуктами, нежирными молочными продуктами, с низким содержанием насыщенных жиров, холестерина, рафинированных углеводов и соли. Основной механизм – снижение потребления натрия и увеличение калия, кальция, магния.

## Показания
- Артериальная гипертензия (I класс рекомендаций, уровень доказательности Ia)
- Высокое нормальное АД (130–139/85–89) – для профилактики АГ
- Метаболический синдром, ожирение
- Хроническая сердечная недостаточность (в составе комплексной терапии)

## Противопоказания
- Хроническая болезнь почек с гиперкалиемией (из-за высокого содержания калия)
- Тяжёлая почечная недостаточность (СКФ < 30)
- Приём калийсберегающих диуретиков (риск гиперкалиемии)

## Эффективность (доказательная база)
- Снижение систолического АД на 8–14 мм рт. ст. у пациентов с АГ (данные DASH-исследования, NEJM 1997)
- Эффект сравним с монотерапией антигипертензивным препаратом
- Комбинация DASH + ограничение натрия до 1500 мг/сут даёт дополнительное снижение АД на 4–5 мм рт. ст.

## Практическая реализация

**Рекомендуемое потребление (на 2000 ккал/сут):**
| Группа продуктов | Порции | Примеры |
|------------------|--------|---------|
| Овощи | 4–5 порций | листовые, брокколи, морковь, помидоры |
| Фрукты | 4–5 порций | яблоки, груши, цитрусовые, бананы |
| Цельнозерновые | 6–8 порций | хлеб из муки грубого помола, овсянка, коричневый рис |
| Нежирные молочные продукты | 2–3 порции | обезжиренное молоко, йогурт |
| Постное мясо, птица, рыба | ≤ 2 порций | курица без кожи, индейка, лосось |
| Орехи, бобовые, семена | 4–5 порций в неделю | грецкие орехи, фасоль, льняное семя |
| Жиры и масла | 2–3 порции | оливковое масло, авокадо |

**Ограничения:**
- Натрий: < 2300 мг/сут (оптимально < 1500 мг/сут) – что соответствует < 5 г соли/сут
- Насыщенные жиры: < 6% от калорийности
- Сладости и добавленный сахар: ≤ 5 порций в неделю
- Алкоголь: не более 1 напитка/сут для женщин, 2 – для мужчин

## Ожидаемые результаты
- Снижение АД через 2–4 недели
- Улучшение липидного профиля (снижение ЛПНП)
- Снижение массы тела (при соблюдении калоража)
- Снижение риска сердечно-сосудистых событий на 15–20% (долгосрочные исследования)

## Побочные эффекты / риски
- Гиперкалиемия (риск при ХБП или приёме калийсберегающих диуретиков)
- Дефицит витамина B12, кальция (при строгом соблюдении без контроля) – редко

## Сочетание с медикаментозной терапией
- DASH диета усиливает эффект антигипертензивных препаратов, позволяя снизить их дозы
- При добавлении диеты к терапии – контролировать АД и калий (особенно у пациентов на иАПФ/БРА и спиронолактоне)

## Информация для пациента
Диета DASH – это способ питания, который помогает снизить давление без лекарств или вместе с ними. Ешьте больше овощей, фруктов, цельнозерновых, обезжиренных молочных продуктов. Ограничьте соль (не досаливайте готовую еду, уберите соленья, колбасы, фастфуд). Замените сладости на орехи и фрукты. Через 2–4 недели вы заметите улучшение. Подробную памятку с меню можно взять у врача.

## Связанные документы
- [[DIAG-DISEASE-001]] – Артериальная гипертензия
- [[PROT-PATIENT_INFO-001]] – Памятка для пациента по АГ
- [[PHARM-NONPHARM-002]] – Физическая активность при АГ

## Источники
1. Appel LJ, Moore TJ, Obarzanek E, et al. A clinical trial of the effects of dietary patterns on blood pressure. DASH Collaborative Research Group. N Engl J Med. 1997;336(16):1117-24.
2. 2023 ESH Guidelines for the management of arterial hypertension. Journal of Hypertension. 2023;41(12):1874–2071.
3. Сайт Национального института сердца, лёгких и крови (NHLBI): DASH diet.

```

## kb/therapy/regimens/pharm_regimen_hypertension.md

```markdown
---
id: PHARM-REGIMEN-001
title: Схема лечения артериальной гипертензии
domain: pharm
category: regimen
body_system:
- cardiovascular
tags:
- hypertension
- treatment
- core
- antihypertensive
urgency: routine
access_level: professional
target_specialist:
- therapist
- cardiologist
age_group:
- adult
- elderly
evidence_level: Ia
recommendation_class: I
related:
- DIAG-DISEASE-001
- PROT-PROTOCOL-001
- PHARM-DRUGCLASS-001
- PHARM-DRUGCLASS-002
- PHARM-DRUGCLASS-003
- PHARM-DRUGCLASS-004
- PHARM-DRUG-001
- PHARM-DRUG-002
- PHARM-NONPHARM-001
sources:
- Клинические рекомендации «АГ у взрослых», 2024
- 2023 ESH Guidelines
clinical_guidelines:
- АГ у взрослых, 2024
last_medical_review: '2025-03-01'
medical_reviewer: Иванов И.И., д.м.н.
author: Инженер знаний №2
version: '1.0'
date_created: '2025-02-25'
date_updated: '2025-03-01'
status: approved
disclaimer: true
relations:
- target: DIAG-DISEASE-001
  type: regimen_for
  description: Схема предназначена для терапии артериальной гипертензии.
- target: PROT-PROTOCOL-001
  type: used_by_protocol
  description: Схема используется клиническим протоколом ведения АГ.
- target: PHARM-DRUGCLASS-001
  type: uses_drugclass
  description: В схеме используется группа иАПФ.
- target: PHARM-DRUGCLASS-002
  type: uses_drugclass
  description: В схеме может использоваться группа БРА.
- target: PHARM-DRUGCLASS-003
  type: uses_drugclass
  description: В схеме может использоваться группа БКК.
- target: PHARM-DRUGCLASS-004
  type: uses_drugclass
  description: В схеме может использоваться группа тиазидных диуретиков.
- target: PHARM-DRUG-001
  type: includes_drug
  description: Эналаприл приведён как пример препарата.
- target: PHARM-DRUG-002
  type: includes_drug
  description: Амлодипин приведён как пример препарата.
- target: PHARM-NONPHARM-001
  type: includes_nonpharm
  description: Немедикаментозные меры дополняют терапевтическую схему.
---

# Схема лечения артериальной гипертензии

> **Дисклеймер**: Схема приведена для медицинских специалистов. Окончательное решение о терапии принимает лечащий врач с учётом индивидуальных особенностей пациента.

## Целевая популяция
Взрослые пациенты с эссенциальной артериальной гипертензией (АГ) с целевым АД < 130/80 мм рт. ст. (для большинства, по ESH 2023). Для пожилых ≥ 80 лет – целевое АД < 140/90.

## Основные принципы
- Начинать терапию с **монотерапии** (у пациентов с АД 140–159/90–99 мм рт. ст. и низким/средним риском) или с **двойной комбинации** (у пациентов с АД ≥ 160/100 или высоким/очень высоким риском).
- Предпочтительны **фиксированные комбинации** для повышения приверженности.
- Титровать дозу каждые 2–4 недели до достижения цели.
- При неэффективности двойной комбинации – переход на тройную.

## Схема 1-й линии
**Монотерапия** (стартовая при АД 1-й степени):
- [[PHARM-DRUGCLASS-001]] иАПФ (эналаприл 5–10 мг/сут) или
- [[PHARM-DRUGCLASS-002]] БРА (лозартан 50 мг/сут) или
- [[PHARM-DRUGCLASS-003]] БКК (амлодипин 5 мг/сут) или
- [[PHARM-DRUGCLASS-004]] Тиазидный диуретик (индапамид 1.5–2.5 мг/сут)

**Двойная комбинация** (стартовая при АД ≥ 160/100 или высоком риске, а также при неэффективности монотерапии):
| Препарат 1 | Препарат 2 | Пример доз |
|------------|------------|-------------|
| иАПФ / БРА | БКК (амлодипин) | периндоприл 5 мг + амлодипин 5 мг |
| иАПФ / БРА | тиазидный диуретик | лозартан 50 мг + индапамид 1.5 мг |
| БКК | тиазидный диуретик | амлодипин 5 мг + индапамид 1.5 мг |

*Примечание: комбинация иАПФ + БРА противопоказана (удвоение риска гиперкалиемии и ОПП).*

## Альтернативные схемы (2-я линия)
При непереносимости или противопоказаниях к первой линии:
- [[PHARM-DRUGCLASS-005]] β-блокаторы (метопролол, бисопролол) – особенно при ИБС, ХСН, ЧСС > 80
- α-блокаторы (доксазозин) – только при доброкачественной гиперплазии предстательной железы
- Антагонисты минералокортикоидных рецепторов (спиронолактон) – при резистентной АГ

## Комбинированные режимы (тройная терапия)
При неэффективности двойной комбинации (после титрования до полных доз):
- **иАПФ/БРА + БКК + тиазидный диуретик** – золотой стандарт тройной терапии
- Пример: периндоприл 10 мг + амлодипин 10 мг + индапамид 2.5 мг (фиксированная комбинация)

**Резистентная АГ** (АД не достигнуто на трёх препаратах, включая диуретик):
- Добавить спиронолактон 12.5–25 мг/сут (при СКФ > 45 и нормальном калии)
- При непереносимости – эплеренон, клонидин, доксазозин

## Мониторинг эффективности
| Параметр | Цель | Частота |
|----------|------|---------|
| Офисное АД | <130/80 | ежемесячно до цели, затем 1 раз в 3–6 мес |
| СМАД (суточное) | <125/75 | при подозрении на «маскированную» или «белый халат» |
| Креатинин, калий | стабильность | через 2–4 недели после начала/титрования |
| Приверженность | высокая | каждый визит |

## Критерии перехода на следующую линию
- Недостижение целевого АД через 4 недели терапии (при хорошей приверженности) → усиление (добавление второго препарата)
- Недостижение цели на двойной комбинации в полных дозах через 4–8 недель → переход на тройную
- Недостижение цели на тройной комбинации (включая диуретик) → резистентная АГ → добавить спиронолактон и/или направить к специалисту

## Особенности у особых групп
- **ХБП с протеинурией**: иАПФ или БРА в максимально переносимых дозах (нефропротекция). Целевое АД < 130/80.
- **Сахарный диабет**: иАПФ/БРА предпочтительны. Целевое АД < 130/80.
- **Пожилые ≥ 65 лет**: начинать с половинных доз, медленное титрование. Целевое АД < 140/90 (для 65–79), < 140/90 (≥80, но с осторожностью).
- **Беременность**: метилдопа, лабеталол, нифедипин (иАПФ/БРА противопоказаны).

## Связанные документы
- [[DIAG-DISEASE-001]] – Артериальная гипертензия
- [[PHARM-DRUGCLASS-001]] – иАПФ
- [[PHARM-DRUGCLASS-002]] – БРА
- [[PHARM-DRUGCLASS-003]] – БКК
- [[PROT-PROTOCOL-001]] – Протокол ведения АГ

## Источники
1. Клинические рекомендации «Артериальная гипертензия у взрослых», Минздрав РФ, 2024.
2. 2023 ESH Guidelines for the management of arterial hypertension. Journal of Hypertension. 2023;41(12):1874–2071.

```

## main.py

```python
"""Точка запуска MVP MedAssist."""

from src.cli import run_cli


if __name__ == "__main__":
    run_cli()

```

## requirements.txt

```text
PyYAML>=6.0
pytest>=8.0

```

## src/__init__.py

```python
"""MedAssist MVP: обработка Markdown/YAML базы знаний."""

```

## src/cli.py

```python
"""Консольный интерфейс MVP MedAssist."""

from __future__ import annotations

import argparse
from pathlib import Path

from .config import KB_ROOT, PROJECT_ROOT
from .linker import Linker
from .repository import KnowledgeRepository
from .scenarios import ScenarioRunner
from .search_engine import SearchEngine
from .validator import KnowledgeBaseValidator


def build_repository(kb_root: Path | str = KB_ROOT) -> KnowledgeRepository:
    repository = KnowledgeRepository(kb_root)
    repository.load()
    return repository


def print_card(card) -> None:
    print(f"\n{card.id} — {card.title}")
    print(f"Категория: {card.category}")
    print(f"Домен: {card.domain}")
    print(f"Срочность: {card.urgency}")
    print(f"Теги: {', '.join(card.tags)}")
    print(f"Файл: {card.file_path}")


def print_statistics(repository: KnowledgeRepository) -> None:
    print("\nСтатистика базы знаний")
    print(f"Всего карточек: {len(repository.cards)}")
    print("\nПо доменам:")
    for domain, count in repository.summary_by_domain().items():
        print(f"  {domain}: {count}")
    print("\nПо категориям:")
    for category, count in repository.summary_by_category().items():
        print(f"  {category}: {count}")
    if repository.parse_errors:
        print("\nОшибки парсинга:")
        for error in repository.parse_errors:
            print(f"  - {error}")


def run_interactive(repository: KnowledgeRepository) -> None:
    search_engine = SearchEngine(repository)
    linker = Linker(repository)
    validator = KnowledgeBaseValidator(repository)
    scenarios = ScenarioRunner(repository)

    while True:
        print("\nMedAssist Knowledge Base MVP")
        print("1. Показать статистику базы знаний")
        print("2. Найти карточку")
        print("3. Показать карточку по ID")
        print("4. Показать связанные документы")
        print("5. Фильтр по категории")
        print("6. Фильтр по срочности")
        print("7. Проверить целостность базы знаний")
        print("8. Запустить демонстрационный сценарий")
        print("0. Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "0":
            print("Выход из MVP MedAssist.")
            return
        if choice == "1":
            print_statistics(repository)
        elif choice == "2":
            query = input("Введите запрос: ").strip()
            results = search_engine.search(query)
            if not results:
                print("Ничего не найдено.")
            for result in results:
                print(f"{result.card.short_description}; score={result.score}; найдено по: {', '.join(result.matched_by)}")
        elif choice == "3":
            card_id = input("Введите ID карточки: ").strip()
            card = repository.get_by_id(card_id)
            if card is None:
                print("Карточка не найдена.")
            else:
                print_card(card)
        elif choice == "4":
            card_id = input("Введите ID исходной карточки: ").strip()
            related = linker.get_related_cards(card_id)
            if not related:
                print("Связанные документы не найдены или карточка отсутствует.")
            for item in related:
                if item.card is None:
                    print(f"{item.target_id} — отсутствует; тип связи: {item.relation_type}")
                else:
                    print(f"{item.card.short_description}; тип связи: {item.relation_type}")
        elif choice == "5":
            category = input("Введите категорию: ").strip()
            for card in search_engine.filter_by_category(category):
                print(card.short_description)
        elif choice == "6":
            urgency = input("Введите срочность: ").strip()
            for card in search_engine.filter_by_urgency(urgency):
                print(card.short_description)
        elif choice == "7":
            report = validator.validate()
            print(report.to_markdown())
        elif choice == "8":
            print("Доступные сценарии: chest_pain, headache, dyspnea, hypertension_protocol, hypertension_therapy, pharm_drug, drug_interaction, validation, all")
            name = input("Введите имя сценария: ").strip() or "all"
            print(scenarios.run(name))
        else:
            print("Неизвестный пункт меню.")


def run_cli(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="MedAssist Knowledge Base MVP")
    parser.add_argument("--kb-root", default=str(KB_ROOT), help="Путь к каталогу kb")
    parser.add_argument("--stats", action="store_true", help="Показать статистику и выйти")
    parser.add_argument("--validate", action="store_true", help="Проверить базу знаний и выйти")
    parser.add_argument("--write-validation-report", action="store_true", help="Записать отчёт в indices/validation_report.md")
    parser.add_argument("--search", help="Найти карточки по запросу")
    parser.add_argument("--show", help="Показать карточку по ID")
    parser.add_argument("--related", help="Показать связанные документы по ID")
    parser.add_argument("--scenario", choices=["chest_pain", "headache", "dyspnea", "hypertension_protocol", "hypertension_therapy", "pharm_drug", "drug_interaction", "validation", "all"], help="Запустить сценарий")

    args = parser.parse_args(argv)
    repository = build_repository(Path(args.kb_root))
    search_engine = SearchEngine(repository)
    linker = Linker(repository)
    validator = KnowledgeBaseValidator(repository)
    scenarios = ScenarioRunner(repository)

    if args.stats:
        print_statistics(repository)
        return

    if args.validate:
        print(validator.validate().to_markdown())
        return

    if args.write_validation_report:
        output_path = PROJECT_ROOT / "indices" / "validation_report.md"
        report = validator.save_report(output_path)
        print(report.to_markdown())
        print(f"\nОтчёт записан: {output_path}")
        return

    if args.search:
        for result in search_engine.search(args.search):
            print(f"{result.card.short_description}; score={result.score}; найдено по: {', '.join(result.matched_by)}")
        return

    if args.show:
        card = repository.get_by_id(args.show)
        if card is None:
            print("Карточка не найдена.")
        else:
            print_card(card)
        return

    if args.related:
        related = linker.get_related_cards(args.related)
        for item in related:
            if item.card is None:
                print(f"{item.target_id} — отсутствует; тип связи: {item.relation_type}")
            else:
                print(f"{item.card.short_description}; тип связи: {item.relation_type}")
        return

    if args.scenario:
        print(scenarios.run(args.scenario))
        return

    run_interactive(repository)

```

## src/config.py

```python
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

```

## src/indexer.py

```python
"""Построение индексов по карточкам базы знаний."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .models import KnowledgeCard, normalize_text


@dataclass
class KnowledgeIndex:
    """Набор быстрых индексов для поиска и навигации."""

    by_id: dict[str, KnowledgeCard] = field(default_factory=dict)
    by_domain: dict[str, list[KnowledgeCard]] = field(default_factory=lambda: defaultdict(list))
    by_category: dict[str, list[KnowledgeCard]] = field(default_factory=lambda: defaultdict(list))
    by_tag: dict[str, list[KnowledgeCard]] = field(default_factory=lambda: defaultdict(list))
    by_urgency: dict[str, list[KnowledgeCard]] = field(default_factory=lambda: defaultdict(list))
    duplicates: dict[str, list[KnowledgeCard]] = field(default_factory=dict)


def build_index(cards: list[KnowledgeCard]) -> KnowledgeIndex:
    """Строит индексы по id, домену, категории, тегам и срочности."""

    index = KnowledgeIndex()
    id_occurrences: dict[str, list[KnowledgeCard]] = defaultdict(list)

    for card in cards:
        if card.id:
            id_occurrences[card.id].append(card)
            # Для удобства работы сохраняем первый встретившийся документ.
            index.by_id.setdefault(card.id, card)

        if card.domain:
            index.by_domain[normalize_text(card.domain)].append(card)
        if card.category:
            index.by_category[normalize_text(card.category)].append(card)
        if card.urgency:
            index.by_urgency[normalize_text(card.urgency)].append(card)

        for tag in card.tags:
            index.by_tag[normalize_text(tag)].append(card)

    index.duplicates = {
        card_id: repeated_cards
        for card_id, repeated_cards in id_occurrences.items()
        if len(repeated_cards) > 1
    }
    return index

```

## src/linker.py

```python
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

```

## src/markdown_parser.py

```python
"""Парсер Markdown-файлов с YAML-метаданными."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import KnowledgeCard


class MarkdownParseError(Exception):
    """Ошибка разбора Markdown-карточки базы знаний."""


def split_front_matter(raw_text: str, file_path: Path) -> tuple[str, str]:
    """Отделяет YAML-блок от основного Markdown-текста.

    Ожидаемый формат файла:
    ---
    id: "..."
    title: "..."
    ---

    # Заголовок карточки
    ...
    """

    normalized = raw_text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise MarkdownParseError(f"В файле нет начального YAML-блока: {file_path}")

    parts = normalized.split("\n---\n", 1)
    if len(parts) != 2:
        raise MarkdownParseError(f"В файле не найден закрывающий разделитель YAML: {file_path}")

    yaml_text = parts[0].removeprefix("---\n")
    markdown_body = parts[1]
    return yaml_text, markdown_body


def parse_markdown_file(file_path: Path) -> KnowledgeCard:
    """Читает Markdown-файл и возвращает объект KnowledgeCard."""

    try:
        raw_text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise MarkdownParseError(f"Файл должен быть в UTF-8: {file_path}") from exc

    yaml_text, markdown_body = split_front_matter(raw_text, file_path)

    try:
        metadata = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        raise MarkdownParseError(f"Ошибка YAML в файле {file_path}: {exc}") from exc

    if not isinstance(metadata, dict):
        raise MarkdownParseError(f"YAML-блок должен быть словарём: {file_path}")

    return KnowledgeCard(metadata=metadata, content=markdown_body.strip(), file_path=file_path)

```

## src/models.py

```python
"""Модели данных MVP MedAssist."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


def normalize_text(value: str) -> str:
    """Нормализует строку для простого поиска.

    Учитывается русская буква ё, регистр и лишние пробелы.
    Это не полнотекстовый поисковый движок, а простой механизм для MVP.
    """

    return " ".join(value.lower().replace("ё", "е").split())


@dataclass(frozen=True)
class KnowledgeCard:
    """Одна единица знаний из Markdown-файла.

    Карточка содержит служебные YAML-метаданные, основной Markdown-текст
    и путь к исходному файлу. Остальные свойства являются удобными
    обёртками над metadata.
    """

    metadata: dict[str, Any]
    content: str
    file_path: Path

    @property
    def id(self) -> str:
        return str(self.metadata.get("id", "")).strip()

    @property
    def title(self) -> str:
        return str(self.metadata.get("title", "")).strip()

    @property
    def domain(self) -> str:
        return str(self.metadata.get("domain", "")).strip()

    @property
    def category(self) -> str:
        return str(self.metadata.get("category", "")).strip()

    @property
    def urgency(self) -> str:
        return str(self.metadata.get("urgency", "")).strip()

    @property
    def tags(self) -> list[str]:
        tags = self.metadata.get("tags", [])
        if isinstance(tags, list):
            return [str(tag).strip() for tag in tags]
        return []

    @property
    def related(self) -> list[str]:
        related = self.metadata.get("related", [])
        if isinstance(related, list):
            return [str(item).strip() for item in related if str(item).strip()]
        return []

    @property
    def relations(self) -> list[dict[str, Any]]:
        relations = self.metadata.get("relations", [])
        if isinstance(relations, list):
            return [item for item in relations if isinstance(item, dict)]
        return []

    @property
    def short_description(self) -> str:
        return f"{self.id} — {self.title} [{self.category}, {self.urgency}]"

    def full_text_for_search(self) -> str:
        """Возвращает текст, по которому выполняется простой поиск."""

        parts = [
            self.id,
            self.title,
            self.domain,
            self.category,
            self.urgency,
            " ".join(self.tags),
            self.content,
        ]
        return normalize_text(" ".join(parts))


@dataclass(frozen=True)
class SearchResult:
    """Результат поиска с числовой оценкой релевантности."""

    card: KnowledgeCard
    score: int
    matched_by: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RelatedCard:
    """Результат разрешения связи между карточками."""

    source_id: str
    target_id: str
    relation_type: str
    description: str
    card: KnowledgeCard | None

    @property
    def is_missing(self) -> bool:
        return self.card is None

```

## src/repository.py

```python
"""Репозиторий базы знаний: загрузка карточек из файловой системы."""

from __future__ import annotations

from pathlib import Path

from .config import EXCLUDED_DIR_NAMES, EXCLUDED_FILE_NAMES, KB_ROOT
from .indexer import KnowledgeIndex, build_index
from .markdown_parser import MarkdownParseError, parse_markdown_file
from .models import KnowledgeCard


class KnowledgeRepository:
    """Загружает карточки базы знаний и предоставляет доступ к индексам."""

    def __init__(self, kb_root: Path | str = KB_ROOT) -> None:
        self.kb_root = Path(kb_root)
        self.cards: list[KnowledgeCard] = []
        self.parse_errors: list[str] = []
        self.index: KnowledgeIndex = KnowledgeIndex()

    def load(self) -> "KnowledgeRepository":
        """Загружает все Markdown-карточки из kb_root."""

        self.cards = []
        self.parse_errors = []

        if not self.kb_root.exists():
            raise FileNotFoundError(f"Каталог базы знаний не найден: {self.kb_root}")

        for file_path in sorted(self.kb_root.rglob("*.md")):
            if self._should_skip(file_path):
                continue

            try:
                card = parse_markdown_file(file_path)
            except MarkdownParseError as exc:
                self.parse_errors.append(str(exc))
                continue

            self.cards.append(card)

        self.index = build_index(self.cards)
        return self

    def _should_skip(self, file_path: Path) -> bool:
        """Определяет, является ли Markdown-файл служебным."""

        if file_path.name in EXCLUDED_FILE_NAMES:
            return True
        return any(part in EXCLUDED_DIR_NAMES for part in file_path.parts)

    def get_by_id(self, card_id: str) -> KnowledgeCard | None:
        return self.index.by_id.get(card_id)

    def all_cards(self) -> list[KnowledgeCard]:
        return list(self.cards)

    def summary_by_domain(self) -> dict[str, int]:
        return {domain: len(cards) for domain, cards in sorted(self.index.by_domain.items())}

    def summary_by_category(self) -> dict[str, int]:
        return {category: len(cards) for category, cards in sorted(self.index.by_category.items())}

```

## src/scenarios.py

```python
"""Демонстрационные сценарии MVP MedAssist."""

from __future__ import annotations

from .linker import Linker
from .repository import KnowledgeRepository
from .search_engine import SearchEngine
from .validator import KnowledgeBaseValidator


class ScenarioRunner:
    """Формирует текстовые демонстрации работы базы знаний."""

    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository
        self.search_engine = SearchEngine(repository)
        self.linker = Linker(repository)
        self.validator = KnowledgeBaseValidator(repository)

    def run(self, name: str) -> str:
        scenarios = {
            "chest_pain": self.chest_pain,
            "headache": self.headache_hypertension,
            "dyspnea": self.dyspnea,
            "validation": self.validation,
            "hypertension_protocol": self.hypertension_protocol,
            "hypertension_therapy": self.hypertension_therapy,
            "pharm_drug": self.pharm_drug,
            "drug_interaction": self.drug_interaction,
            "all": self.all_scenarios,
        }
        scenario = scenarios.get(name)
        if scenario is None:
            return f"Неизвестный сценарий: {name}. Доступно: {', '.join(scenarios)}"
        return scenario()

    def chest_pain(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: боль в груди",
            query="боль в груди",
            focus_id="DIAG-SYMPTOM-002",
        )

    def headache_hypertension(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: головная боль и высокое АД",
            query="головная боль",
            focus_id="DIAG-SYMPTOM-001",
        )

    def dyspnea(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: одышка",
            query="одышка",
            focus_id="DIAG-SYMPTOM-003",
        )

    def hypertension_protocol(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: протокол ведения артериальной гипертензии",
            query="артериальная гипертензия протокол",
            focus_id="PROT-PROTOCOL-001",
        )

    def hypertension_therapy(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: фармакотерапия артериальной гипертензии",
            query="схема лечения артериальной гипертензии",
            focus_id="PHARM-REGIMEN-001",
        )

    def pharm_drug(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: просмотр лекарственного средства",
            query="эналаприл",
            focus_id="PHARM-DRUG-001",
        )

    def drug_interaction(self) -> str:
        return self._scenario_by_query(
            title="Сценарий: лекарственное взаимодействие",
            query="метформин контраст",
            focus_id="PHARM-INTERACTION-001",
        )

    def validation(self) -> str:
        report = self.validator.validate()
        return report.to_markdown()

    def all_scenarios(self) -> str:
        return "\n\n---\n\n".join([
            self.chest_pain(),
            self.headache_hypertension(),
            self.dyspnea(),
            self.hypertension_protocol(),
            self.hypertension_therapy(),
            self.pharm_drug(),
            self.drug_interaction(),
            self.validation(),
        ])

    def _scenario_by_query(self, title: str, query: str, focus_id: str) -> str:
        lines = [f"# {title}", ""]
        lines.append(f"Запрос пользователя: **{query}**")
        lines.append("")

        results = self.search_engine.search(query, limit=5)
        lines.append("## Результаты поиска")
        if not results:
            lines.append("Документы не найдены.")
            return "\n".join(lines)

        for result in results:
            lines.append(f"- {result.card.short_description}; score={result.score}; найдено по: {', '.join(result.matched_by)}")

        focus_card = self.repository.get_by_id(focus_id) or results[0].card
        lines.append("")
        lines.append("## Основная найденная карточка")
        lines.append(f"{focus_card.short_description}")
        lines.append("")
        lines.append("## Связанные документы")
        related = self.linker.get_related_cards(focus_card.id)
        if not related:
            lines.append("Связанные документы не указаны.")
        else:
            for item in related:
                if item.card is None:
                    lines.append(f"- {item.target_id} — связь битая ({item.relation_type})")
                else:
                    lines.append(f"- {item.card.short_description}; тип связи: {item.relation_type}")
        return "\n".join(lines)

```

## src/search_engine.py

```python
"""Простой поисковый модуль базы знаний."""

from __future__ import annotations

from .models import KnowledgeCard, SearchResult, normalize_text
from .repository import KnowledgeRepository


class SearchEngine:
    """Выполняет поиск по карточкам базы знаний.

    Поиск специально сделан простым и прозрачным: он не использует ML и внешние
    сервисы, поэтому его легко объяснить на защите.
    """

    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def search(self, query: str, limit: int = 20) -> list[SearchResult]:
        """Ищет карточки по id, названию, тегам, категории, срочности и тексту."""

        normalized_query = normalize_text(query)
        if not normalized_query:
            return []

        results: list[SearchResult] = []
        for card in self.repository.all_cards():
            score, matched_by = self._score_card(card, normalized_query)
            if score > 0:
                results.append(SearchResult(card=card, score=score, matched_by=matched_by))

        results.sort(key=lambda item: (-item.score, item.card.id))
        return results[:limit]

    def filter_by_category(self, category: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_category.get(normalize_text(category), []))

    def filter_by_tag(self, tag: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_tag.get(normalize_text(tag), []))

    def filter_by_urgency(self, urgency: str) -> list[KnowledgeCard]:
        return list(self.repository.index.by_urgency.get(normalize_text(urgency), []))

    @staticmethod
    def _score_card(card: KnowledgeCard, query: str) -> tuple[int, list[str]]:
        score = 0
        matched_by: list[str] = []

        card_id = normalize_text(card.id)
        title = normalize_text(card.title)
        category = normalize_text(card.category)
        urgency = normalize_text(card.urgency)
        tags = [normalize_text(tag) for tag in card.tags]
        full_text = card.full_text_for_search()

        if query == card_id:
            score += 100
            matched_by.append("id")
        elif query in card_id:
            score += 70
            matched_by.append("id_part")

        if query == title:
            score += 90
            matched_by.append("title_exact")
        elif query in title:
            score += 60
            matched_by.append("title")

        if query == category:
            score += 50
            matched_by.append("category")

        if query == urgency:
            score += 40
            matched_by.append("urgency")

        if query in tags:
            score += 55
            matched_by.append("tag_exact")
        elif any(query in tag for tag in tags):
            score += 35
            matched_by.append("tag")

        if query in full_text:
            score += 15
            matched_by.append("content")

        # Поиск по отдельным словам запроса.
        words = [word for word in query.split() if len(word) >= 3]
        if words and all(word in full_text for word in words):
            score += 20
            matched_by.append("all_words")

        return score, matched_by

```

## src/validator.py

```python
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

```

## tests/conftest.py

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

```

## tests/test_linker.py

```python
from src.linker import Linker
from src.repository import KnowledgeRepository


def test_related_cards_for_chest_pain():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("DIAG-SYMPTOM-002")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-002" in target_ids
    assert "DIAG-EMERGENCY-001" in target_ids
    assert "DIAG-DIFDIAG-001" in target_ids
    assert all(not item.is_missing for item in related)

```

## tests/test_log.md

```markdown
# Журнал тестирования MVP MedAssist

## Команда

```bash
python -m pytest -q
```

## Результат

```text
............                                                             [100%]
12 passed in 4.41s
```

## Проверка валидатором

```bash
python main.py --validate
```

```text
# Отчёт проверки базы знаний MedAssist

Проверено карточек: **44**.
Ошибок парсинга: **0**.
Структурных ошибок: **0**.
Предупреждений: **0**.
Итог: **проверка пройдена**.
```

```

## tests/test_parser.py

```python
from pathlib import Path

from src.markdown_parser import parse_markdown_file


def test_parse_markdown_card():
    path = Path("kb/diagnostics/symptoms/diag_symptom_chest_pain.md")
    card = parse_markdown_file(path)

    assert card.id == "DIAG-SYMPTOM-002"
    assert card.title == "Боль в груди"
    assert card.category == "symptom"
    assert "chest_pain" in card.tags
    assert "Боль в груди" in card.content

```

## tests/test_pharm.py

```python
from src.linker import Linker
from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine


def test_pharm_cards_are_loaded():
    repo = KnowledgeRepository("kb").load()

    assert repo.get_by_id("PHARM-DRUG-001") is not None
    assert repo.get_by_id("PHARM-DRUG-002") is not None
    assert repo.get_by_id("PHARM-DRUGCLASS-001") is not None
    assert repo.get_by_id("PHARM-REGIMEN-001") is not None
    assert repo.get_by_id("PHARM-INTERACTION-001") is not None
    assert repo.get_by_id("PHARM-ADR-001") is not None
    assert repo.get_by_id("PHARM-DOSING-001") is not None
    assert repo.get_by_id("PHARM-NONPHARM-001") is not None


def test_pharm_regimen_links_are_resolved():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("PHARM-REGIMEN-001")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-001" in target_ids
    assert "PROT-PROTOCOL-001" in target_ids
    assert "PHARM-DRUG-001" in target_ids
    assert "PHARM-DRUG-002" in target_ids
    assert all(not item.is_missing for item in related)


def test_search_pharm_drug_and_interaction():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    enalapril_ids = [result.card.id for result in search.search("эналаприл")]
    interaction_ids = [result.card.id for result in search.search("метформин контраст")]

    assert "PHARM-DRUG-001" in enalapril_ids
    assert "PHARM-INTERACTION-001" in interaction_ids

```

## tests/test_protocols.py

```python
from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine
from src.linker import Linker


def test_protocol_cards_are_loaded():
    repo = KnowledgeRepository("kb").load()

    assert repo.get_by_id("PROT-PROTOCOL-001") is not None
    assert repo.get_by_id("PROT-EMERGENCY_P-001") is not None
    assert repo.get_by_id("PROT-FOLLOW_UP-001") is not None


def test_protocol_related_cards_are_resolved():
    repo = KnowledgeRepository("kb").load()
    linker = Linker(repo)

    related = linker.get_related_cards("PROT-PROTOCOL-001")
    target_ids = {item.target_id for item in related}

    assert "DIAG-DISEASE-001" in target_ids
    assert "PROT-ROUTING-001" in target_ids
    assert "PHARM-REGIMEN-001" in target_ids
    assert all(not item.is_missing for item in related)


def test_search_hypertension_protocol():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    results = search.search("артериальная гипертензия протокол")
    ids = [result.card.id for result in results]

    assert "PROT-PROTOCOL-001" in ids

```

## tests/test_repository.py

```python
from src.repository import KnowledgeRepository


def test_repository_loads_diagnostic_cards():
    repo = KnowledgeRepository("kb").load()

    assert len(repo.cards) >= 20
    assert repo.get_by_id("DIAG-SYMPTOM-002") is not None
    assert repo.get_by_id("DIAG-EMERGENCY-001") is not None
    assert not repo.parse_errors

```

## tests/test_search.py

```python
from src.repository import KnowledgeRepository
from src.search_engine import SearchEngine


def test_search_chest_pain():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    results = search.search("боль в груди")

    ids = [result.card.id for result in results]
    assert "DIAG-SYMPTOM-002" in ids


def test_filter_emergency():
    repo = KnowledgeRepository("kb").load()
    search = SearchEngine(repo)

    cards = search.filter_by_urgency("emergency")

    assert any(card.id == "DIAG-EMERGENCY-001" for card in cards)

```

## tests/test_validator.py

```python
from src.repository import KnowledgeRepository
from src.validator import KnowledgeBaseValidator


def test_validator_has_no_errors():
    repo = KnowledgeRepository("kb").load()
    report = KnowledgeBaseValidator(repo).validate()

    assert report.is_valid, report.to_markdown()

```
