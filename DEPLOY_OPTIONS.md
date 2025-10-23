# 🚀 Варианты деплоя для решения проблемы с Ruby

## Проблема

GitHub Actions падает с ошибкой конфликта версий Ruby между `github-pages` и `jekyll` 4.3.0.

## Решения

### Вариант 1: Jekyll 3.9 (Рекомендуется)

Использует совместимую версию Jekyll с GitHub Pages.

**Файлы:**

- `Gemfile.github-pages` - совместимые зависимости
- Workflow использует Ruby 2.7

**Преимущества:**

- ✅ Полная совместимость с GitHub Pages
- ✅ Все функции Jekyll работают
- ✅ Стабильная версия

**Недостатки:**

- ❌ Старая версия Jekyll (3.9 вместо 4.3)

### Вариант 2: Статический деплой

Использует Python скрипт для конвертации Markdown в HTML.

**Файлы:**

- `deploy-www-static.yml` - статический workflow
- `convert_md_to_html.py` - конвертер Markdown

**Преимущества:**

- ✅ Нет конфликтов зависимостей
- ✅ Быстрая сборка
- ✅ Простая настройка

**Недостатки:**

- ❌ Нет продвинутых функций Jekyll
- ❌ Ручная конвертация Markdown

### Вариант 3: Минимальный Jekyll

Использует только необходимые зависимости без GitHub Pages.

**Файлы:**

- `Gemfile.minimal` - минимальные зависимости
- Текущий workflow

**Преимущества:**

- ✅ Современная версия Jekyll
- ✅ Минимальные зависимости

**Недостатки:**

- ❌ Может не работать с GitHub Pages
- ❌ Ограниченная функциональность

## Как выбрать вариант

### Для продакшена (рекомендуется)

```bash
# Используйте Вариант 1 - Jekyll 3.9
# Workflow автоматически использует Gemfile.github-pages
```

### Для быстрого деплоя

```bash
# Используйте Вариант 2 - Статический
# Переименуйте deploy-www-static.yml в deploy-www-to-github-pages.yml
```

### Для разработки

```bash
# Используйте Вариант 3 - Минимальный
# Для локальной разработки
```

## Переключение между вариантами

### На Вариант 1 (Jekyll 3.9)

```bash
# Workflow уже настроен на использование Gemfile.github-pages
# Ничего дополнительно делать не нужно
```

### На Вариант 2 (Статический)

```bash
# Переименуйте файлы
mv .github/workflows/deploy-www-to-github-pages.yml .github/workflows/deploy-www-to-github-pages.yml.backup
mv .github/workflows/deploy-www-static.yml .github/workflows/deploy-www-to-github-pages.yml
```

### На Вариант 3 (Минимальный)

```bash
# Измените workflow
# Замените cp Gemfile.github-pages Gemfile на cp Gemfile.minimal Gemfile
```

## Тестирование

### Локальное тестирование

```bash
cd www

# Вариант 1
cp Gemfile.github-pages Gemfile
bundle install
bundle exec jekyll build

# Вариант 2
python convert_md_to_html.py

# Вариант 3
cp Gemfile.minimal Gemfile
bundle install
bundle exec jekyll build
```

### Тестирование в GitHub Actions

1. Сделайте тестовый коммит
2. Проверьте логи в Actions
3. Убедитесь, что деплой прошел успешно

## Рекомендации

### Для большинства случаев

**Используйте Вариант 1** - он обеспечивает стабильную работу с GitHub Pages.

### Для простых сайтов

**Используйте Вариант 2** - быстрый и надежный статический деплой.

### Для экспериментов

**Используйте Вариант 3** - минимальные зависимости для тестирования.

## Отладка

### Проверка зависимостей

```bash
bundle check
bundle outdated
```

### Очистка кэша

```bash
bundle clean --force
rm -rf vendor/bundle
```

### Проверка версий

```bash
ruby -v
bundle -v
jekyll -v
```

## Будущие улучшения

- [ ] Автоматическое определение совместимых версий
- [ ] Поддержка нескольких версий Jekyll
- [ ] Интеграция с GitHub Pages без конфликтов
- [ ] Автоматическое переключение между вариантами

---

<div align="center">
  <sub>🚀 Выберите подходящий вариант и наслаждайтесь стабильным деплоем!</sub>
</div>
