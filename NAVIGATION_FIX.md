# Исправление навигации "Назад к главной"

## Проблема
Ссылка "Назад к главной" во всех страницах документации вела на неправильный URL:
- ❌ `https://atom735.github.io/doc/index.html`
- ✅ Должна вести на корень: `https://atom735.github.io/`

## Причина
Во всех markdown файлах использовался неправильный путь в front matter:
```yaml
back_link: /index.html  # ❌ Неправильно
```

## Решение
Исправлены все файлы, заменив путь на корневой:
```yaml
back_link: /  # ✅ Правильно
```

## Исправленные файлы
- `doc/archs/flutter_architectures_analysis.md`
- `doc/sketches/app_features_overview.md`
- `doc/sketches/user_flows.md`
- `doc/b2b_features/admin_panel_features.md`
- `doc/b2b_features/crm_overview.md`
- `doc/b2b_features/seller_portal_features.md`
- `doc/kramdown_examples/index.md`
- `doc/kramdown_examples/themes_demo.md`
- `doc/kramdown_examples/basic_features.md`
- `doc/kramdown_examples/code_highlighting.md`
- `doc/kramdown_examples/tables.md`
- `doc/kramdown_examples/math_formulas.md`
- `doc/kramdown_examples/footnotes_definitions.md`
- `doc/kramdown_examples/abbreviations_symbols.md`
- `KRAMDOWN_GUIDE.md` (примеры в документации)

## Результат
Теперь все ссылки "← Назад к главной" корректно ведут на главную страницу сайта `https://atom735.github.io/`.
