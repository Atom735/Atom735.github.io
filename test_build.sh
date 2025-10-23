#!/bin/bash

# Скрипт для тестирования сборки Jekyll локально

echo "🔧 Проверка установки Ruby..."
ruby --version

echo "🔧 Проверка установки Bundler..."
bundle --version

echo "🔧 Очистка предыдущей сборки..."
rm -rf _site

echo "🔧 Установка зависимостей..."
bundle install

echo "🔧 Проверка установленных плагинов..."
bundle exec jekyll doctor

echo "🔧 Сборка Jekyll сайта..."
bundle exec jekyll build --verbose

if [ $? -eq 0 ]; then
    echo "✅ Сборка успешно завершена!"
    echo "📁 Файлы созданы в директории _site/"
    ls -la _site/

    echo "🔍 Проверка наличия SEO тегов в HTML..."
    if grep -r "seo" _site/ > /dev/null 2>&1; then
        echo "✅ SEO теги найдены в сгенерированных файлах"
    else
        echo "⚠️  SEO теги не найдены - возможно проблема с плагином jekyll-seo-tag"
    fi
else
    echo "❌ Ошибка при сборке!"
    exit 1
fi
