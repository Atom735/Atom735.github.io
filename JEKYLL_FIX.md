# Решение проблемы сборки Jekyll

## Проблема
Ошибка при сборке Jekyll сайта в GitHub Actions:
```
Error: could not read file /home/runner/work/flt_grepsearch/flt_grepsearch/www/vendor/bundle/ruby/2.7.0/gems/jekyll-3.9.5/lib/site_template/_posts/0000-00-00-welcome-to-jekyll.markdown.erb: Invalid date '<%= Time.now.strftime('%Y-%m-%d %H:%M:%S %z') %>'
```

## Причина
1. Использование устаревшей версии Ruby (2.7.0) и Jekyll (3.9.5)
2. Jekyll пытается обработать файлы шаблонов из vendor директории
3. Неправильная конфигурация исключений в _config.yml

## Решение

### 1. Обновлена конфигурация Jekyll (_config.yml)
- Добавлены исключения для vendor/, node_modules/, .sass-cache/, .jekyll-cache/
- Добавлены настройки для Jekyll 4.x (incremental: false, safe: true)

### 2. Обновлен GitHub Actions workflow
- Используется Ruby 3.1 вместо 2.7.0
- Добавлен шаг сборки Jekyll с флагом --safe
- Изменен путь публикации на ./www/_site

### 3. Обновлен Gemfile.github-pages
- Jekyll обновлен до версии 4.3.0
- Добавлен webrick для совместимости с Ruby 3.0+

### 4. Создан скрипт для локального тестирования
- `test_build.sh` - скрипт для проверки сборки локально
- `Gemfile.local` - альтернативный Gemfile для локальной разработки

## Использование

### Локальное тестирование
```bash
cd www
chmod +x test_build.sh
./test_build.sh
```

### Или вручную
```bash
cd www
bundle install
bundle exec jekyll build --safe --verbose
```

## Дополнительные исправления (обновление)

### Проблема с плагином jekyll-seo-tag
После первого исправления возникла новая ошибка:
```
Liquid syntax error (line 13): Unknown tag 'seo' in /home/runner/work/flt_grepsearch/flt_grepsearch/www/_layouts/default.html
```

### Дополнительные изменения:

1. **Обновлен GitHub Actions workflow**:
   - Отключен bundler-cache для принудительной переустановки зависимостей
   - Добавлен явный шаг установки bundler и зависимостей
   - Убран флаг `--safe` из команды сборки Jekyll

2. **Обновлена конфигурация Jekyll**:
   - Убрана настройка `safe: true` которая блокировала плагины

3. **Создан резервный layout**:
   - `default_no_seo.html` - альтернативный layout без зависимости от плагина seo

### Если проблема с плагинами продолжится:
Замените в `_config.yml`:
```yaml
defaults:
  - scope:
      path: ''
    values:
      layout: 'default_no_seo'  # вместо 'default'
```

## Результат
После применения всех изменений сборка Jekyll должна проходить успешно без ошибок с датами в шаблонах и с корректной работой плагинов.
