# 🎨 Система тем для Kramdown Examples

## Обзор

Сайт поддерживает три темы:

- **Светлая** - классическая тема с белым фоном
- **Темная** - современная тема с темным фоном
- **Системная** - автоматически следует настройкам ОС

## Структура файлов

```
www/
├── assets/
│   ├── css/
│   │   └── themes.css          # CSS с темами
│   └── js/
│       └── theme-switcher.js   # JavaScript переключатель
├── _layouts/
│   └── default.html            # Layout с подключением CSS/JS
└── doc/kramdown_examples/
    └── themes_demo.md          # Демонстрация тем
```

## CSS переменные

### Светлая тема

```css
:root {
  --bg-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --bg-secondary: #ffffff;
  --text-primary: #333333;
  --accent-color: #667eea;
}
```

### Темная тема

```css
[data-theme="dark"] {
  --bg-primary: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  --bg-secondary: #2d3748;
  --text-primary: #e2e8f0;
  --accent-color: #81c784;
}
```

### Системная тема

```css
@media (prefers-color-scheme: dark) {
  [data-theme="system"] { /* темные цвета */ }
}

@media (prefers-color-scheme: light) {
  [data-theme="system"] { /* светлые цвета */ }
}
```

## JavaScript API

### Инициализация

```javascript
// Автоматически при загрузке страницы
window.themeSwitcher = new ThemeSwitcher();
```

### Методы

```javascript
// Переключить тему
window.themeSwitcher.setTheme('light');
window.themeSwitcher.setTheme('dark');
window.themeSwitcher.setTheme('system');

// Получить текущую тему
const theme = window.themeSwitcher.getCurrentTheme();

// Быстрые методы
window.themeSwitcher.setLightTheme();
window.themeSwitcher.setDarkTheme();
window.themeSwitcher.setSystemTheme();
```

## Использование

### 1. Переключение через UI

- Найдите переключатель в правом верхнем углу
- Выберите нужную тему из выпадающего списка
- Настройка сохранится в localStorage

### 2. Программное переключение

```javascript
// В консоли браузера
window.themeSwitcher.setDarkTheme();
```

### 3. Автоматическое переключение

Системная тема автоматически переключается при изменении настроек ОС.

## Кастомизация

### Добавление новой темы

1. Добавьте CSS переменные в `themes.css`:

```css
[data-theme="custom"] {
  --bg-primary: /* ваш цвет */;
  --bg-secondary: /* ваш цвет */;
  /* ... */
}
```

2. Обновите JavaScript:

```javascript
this.themes = ['light', 'dark', 'system', 'custom'];
```

3. Добавьте опцию в HTML:

```html
<option value="custom">🎨 Кастомная</option>
```

### Изменение цветов

Отредактируйте CSS переменные в `themes.css`:

```css
:root {
  --accent-color: #your-color;
  --bg-secondary: #your-bg;
  /* ... */
}
```

## Совместимость

### Браузеры

- ✅ Chrome 49+
- ✅ Firefox 31+
- ✅ Safari 9.1+
- ✅ Edge 16+

### Функции

- ✅ CSS Custom Properties
- ✅ LocalStorage
- ✅ Media Queries
- ✅ ES6 Classes

## Производительность

### Оптимизации

- CSS переменные для быстрого переключения
- Минимальный JavaScript
- Кэширование в localStorage
- Плавные CSS transitions

### Размер файлов

- `themes.css`: ~15KB
- `theme-switcher.js`: ~3KB
- Общий размер: ~18KB

## Отладка

### Проверка темы

```javascript
// В консоли браузера
console.log('Current theme:', window.themeSwitcher.getCurrentTheme());
console.log('Stored theme:', localStorage.getItem('kramdown-theme'));
```

### Проверка CSS переменных

```javascript
// В консоли браузера
const root = document.documentElement;
const styles = getComputedStyle(root);
console.log('--accent-color:', styles.getPropertyValue('--accent-color'));
```

### Сброс настроек

```javascript
// В консоли браузера
localStorage.removeItem('kramdown-theme');
location.reload();
```

## Будущие улучшения

- [ ] Анимации перехода между темами
- [ ] Дополнительные цветовые схемы
- [ ] Настройка контрастности
- [ ] Поддержка пользовательских тем
- [ ] Экспорт/импорт настроек

---

<div align="center">
  <sub>🎨 Создано с ❤️ для лучшего пользовательского опыта</sub>
</div>
