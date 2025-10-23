#!/bin/bash

# Скрипт для локальной разработки Jekyll сайта

echo "🚀 Запуск Jekyll для локальной разработки..."

# Переходим в папку www
cd "$(dirname "$0")"

# Проверяем наличие Ruby
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby не установлен. Установите Ruby 3.1+ для продолжения."
    exit 1
fi

# Проверяем версию Ruby
RUBY_VERSION=$(ruby -v | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📋 Версия Ruby: $RUBY_VERSION"

# Используем минимальный Gemfile для локальной разработки
if [ -f "Gemfile.minimal" ]; then
    echo "📦 Используем минимальный Gemfile..."
    cp Gemfile.minimal Gemfile
fi

# Устанавливаем зависимости
echo "📦 Устанавливаем зависимости..."
bundle install

# Запускаем Jekyll сервер
echo "🌐 Запускаем Jekyll сервер..."
echo "📍 Сайт будет доступен по адресу: http://localhost:4000"
echo "🛑 Для остановки нажмите Ctrl+C"

bundle exec jekyll serve --host 0.0.0.0 --port 4000
