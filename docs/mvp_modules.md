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
