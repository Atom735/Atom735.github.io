# 🌐 Статический сайт документации

Этот сайт автоматически деплоится в репозиторий `atom735.github.io` при любых изменениях в папке `www/`.

## 📁 Структура

```
www/
├── index.html              # Главная страница
├── convert_md_to_html.py   # Скрипт конвертации Markdown → HTML
├── README.md              # Эта инструкция
└── doc/                   # Документация
    ├── archs/             # Архитектура
    ├── b2b_features/      # B2B функции
    └── sketches/          # Эскизы и планы
```

## 🚀 Как это работает

1. **Редактируете** Markdown файлы в папке `doc/`
2. **Коммитите** изменения в приватный репозиторий
3. **GitHub Actions** автоматически:
   - Конвертирует `.md` → `.html`
   - Деплоит в `atom735.github.io`
4. **Сайт обновляется** по адресу `https://atom735.github.io`

## ✏️ Добавление новой документации

### 1. Создайте Markdown файл

```bash
# Например, новый раздел
mkdir -p www/doc/new_section
nano www/doc/new_section/my_new_doc.md
```

### 2. Добавьте ссылку в index.html

Отредактируйте `www/index.html` и добавьте ссылку в нужный раздел:

```html
<li><a href="doc/new_section/my_new_doc.html">Мой новый документ</a></li>
```

### 3. Закоммитьте изменения

```bash
git add www/
git commit -m "Add new documentation"
git push origin main
```

## 🔧 Локальная разработка

### Предварительный просмотр

```bash
# Конвертируйте Markdown в HTML
cd www
python3 convert_md_to_html.py

# Откройте index.html в браузере
open index.html
```

### Тестирование изменений

```bash
# После изменений в Markdown
cd www
python3 convert_md_to_html.py

# Проверьте результат
open doc/sketches/app_features_overview.html
```

## 🎨 Кастомизация стилей

### Изменить цвета

Отредактируйте CSS в `index.html`:

```css
:root {
    --primary-color: #667eea;    /* Основной цвет */
    --secondary-color: #764ba2;  /* Вторичный цвет */
}
```

### Изменить макет

Отредактируйте HTML структуру в `index.html` и CSS стили.

## 📝 Поддерживаемый Markdown

Скрипт `convert_md_to_html.py` поддерживает:

- ✅ Заголовки (`#`, `##`, `###`, `####`)
- ✅ Жирный текст (`**текст**`)
- ✅ Курсив (`*текст*`)
- ✅ Ссылки (`[текст](url)`)
- ✅ Списки (`- элемент`)
- ✅ Параграфы

### Расширение функциональности

Если нужны дополнительные возможности (таблицы, код, изображения), отредактируйте `convert_md_to_html.py`.

## 🐛 Troubleshooting

### Сайт не обновляется

1. Проверьте **Actions** в GitHub → убедитесь, что workflow выполнился
2. Проверьте логи workflow на наличие ошибок
3. Убедитесь, что изменения запушены в ветку `main`

### Ошибки конвертации

1. Проверьте синтаксис Markdown файлов
2. Убедитесь, что файлы имеют расширение `.md`
3. Запустите конвертацию локально: `python3 convert_md_to_html.py`

### Проблемы с доступом

1. Убедитесь, что репозиторий `atom735.github.io` существует
2. Проверьте настройки GitHub Pages
3. Убедитесь, что у workflow есть права на запись

## 🔄 Автоматизация

Workflow запускается при изменениях в:
- `www/**` - любые файлы в папке www
- `.github/workflows/deploy-www-to-github-pages.yml` - сам workflow

Можно запустить вручную через **Actions** → **Deploy www to atom735.github.io** → **Run workflow**.

---

<div align="center">
  <sub>🚀 Сайт автоматически обновляется при каждом push!</sub>
</div>
