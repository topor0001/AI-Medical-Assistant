# MedAssist Knowledge Base MVP

MVP курсового проекта **MedAssist** — это небольшой обработчик документно-ориентированной базы знаний интеллектуального медицинского ассистента.

Проект демонстрирует не постановку диагноза, а работу с базой знаний: загрузку Markdown-карточек, чтение YAML-метаданных, поиск, навигацию по связям и проверку целостности.

## 1. Что входит в MVP

- 38 диагностические карточки в формате Markdown + YAML.
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

- инженер знаний №1: `diag` — 38 карточки диагностического контура;
- инженер знаний №2: `pharm` — 39 карточек фармакологии и терапии, включая 8 основных карточек из переданных файлов и 5 служебных карточек для замыкания связей;
- инженер знаний №3: `protocols` — 49 карточек клинических протоколов и маршрутизации.

Проверка валидатором:

```text
Проверено карточек: 126
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

