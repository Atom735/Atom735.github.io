# 🔧 Решение проблемы с Ruby версиями

## Проблема

GitHub Actions падает с ошибкой:
```
Bundler found conflicting requirements for the Ruby version:
  In Gemfile:
    github-pages was resolved to 1, which depends on
      Ruby (~> 1.9.3)

    jekyll (~> 4.3.0) was resolved to 4.3.4, which depends on
      Ruby (>= 2.5.0)
```

## Причина

Пакет `github-pages` требует старую версию Ruby (~> 1.9.3), а Jekyll 4.3.0 требует новую версию (>= 2.5.0). Это создает конфликт зависимостей.

## Решение

### 1. Создан минимальный Gemfile

Файл `Gemfile.minimal` содержит только необходимые зависимости без конфликтов:

```ruby
source "https://rubygems.org"

# Jekyll
gem "jekyll", "~> 4.3.0"

# Плагины
gem "jekyll-feed", "~> 0.12"
gem "jekyll-seo-tag", "~> 0.12"
gem "jekyll-sitemap", "~> 1.4"

# Синтаксис подсветка
gem "rouge", "~> 4.0"

# Дополнительные плагины
gem "kramdown-parser-gfm", "~> 1.1"

# Минимальные зависимости для GitHub Pages
gem "minima", "~> 2.5"
gem "jekyll-remote-theme", "~> 0.4"
```

### 2. Обновлен GitHub Actions workflow

Workflow теперь использует минимальный Gemfile:

```yaml
- name: Install Jekyll dependencies
  run: |
      cd www
      cp Gemfile.minimal Gemfile
      bundle install
```

### 3. Создан скрипт для локальной разработки

Файл `start-dev.sh` для запуска локального сервера:

```bash
#!/bin/bash
cd "$(dirname "$0")"
cp Gemfile.minimal Gemfile
bundle install
bundle exec jekyll serve --host 0.0.0.0 --port 4000
```

## Альтернативные решения

### Вариант 1: Использовать Jekyll 3.x

Если нужна полная совместимость с GitHub Pages:

```ruby
gem "jekyll", "~> 3.9.0"
gem "github-pages", group: :jekyll_plugins
```

### Вариант 2: Использовать только GitHub Pages

```ruby
gem "github-pages", group: :jekyll_plugins
```

Но тогда будет старая версия Jekyll.

### Вариант 3: Кастомный деплой

Не использовать GitHub Pages, а деплоить статические файлы напрямую.

## Проверка решения

### Локально

```bash
cd www
./start-dev.sh
```

### В GitHub Actions

Workflow должен пройти успешно без ошибок зависимостей.

## Рекомендации

1. **Для разработки**: используйте `Gemfile.minimal`
2. **Для продакшена**: используйте GitHub Actions с минимальным Gemfile
3. **Для локальной разработки**: используйте скрипт `start-dev.sh`

## Отладка

### Проверка зависимостей

```bash
bundle check
```

### Обновление зависимостей

```bash
bundle update
```

### Очистка кэша

```bash
bundle clean --force
```

## Будущие улучшения

- [ ] Автоматическое определение совместимых версий
- [ ] Поддержка нескольких версий Jekyll
- [ ] Интеграция с GitHub Pages без конфликтов
- [ ] Автоматическое обновление зависимостей

---

<div align="center">
  <sub>🔧 Проблема решена! Теперь Jekyll работает без конфликтов версий</sub>
</div>
