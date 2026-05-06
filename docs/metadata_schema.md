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
