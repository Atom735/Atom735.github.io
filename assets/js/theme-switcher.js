/**
 * Theme Switcher для Kramdown Examples
 * Поддерживает светлую, темную и системную темы
 */

class ThemeSwitcher {
  constructor() {
    this.themes = ["light", "dark", "system"];
    this.currentTheme = this.getStoredTheme() || "system";
    this.init();
  }

  init() {
    this.createSwitcher();
    this.applyTheme(this.currentTheme);
    this.setupEventListeners();
    this.setupSystemThemeListener();
  }

  createSwitcher() {
    // Создаем контейнер для переключателя
    const switcher = document.createElement("div");
    switcher.className = "theme-switcher";
    switcher.innerHTML = `
      <select id="theme-select">
        <option value="light">☀️ Светлая</option>
        <option value="dark">🌙 Темная</option>
        <option value="system">🖥️ Системная</option>
      </select>
    `;

    // Добавляем в body
    document.body.appendChild(switcher);

    // Устанавливаем текущую тему
    const select = document.getElementById("theme-select");
    select.value = this.currentTheme;
  }

  setupEventListeners() {
    const select = document.getElementById("theme-select");
    select.addEventListener("change", (e) => {
      this.setTheme(e.target.value);
    });
  }

  setupSystemThemeListener() {
    // Слушаем изменения системной темы
    if (window.matchMedia) {
      const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
      mediaQuery.addEventListener("change", () => {
        if (this.currentTheme === "system") {
          this.applyTheme("system");
        }
      });
    }
  }

  setTheme(theme) {
    if (this.themes.includes(theme)) {
      this.currentTheme = theme;
      this.storeTheme(theme);
      this.applyTheme(theme);
    }
  }

  applyTheme(theme) {
    const body = document.body;

    // Удаляем все классы тем
    body.removeAttribute("data-theme");

    if (theme === "system") {
      // Для системной темы определяем автоматически
      if (
        window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches
      ) {
        body.setAttribute("data-theme", "dark");
      } else {
        body.setAttribute("data-theme", "light");
      }
    } else {
      body.setAttribute("data-theme", theme);
    }

    // Обновляем выбранную опцию
    const select = document.getElementById("theme-select");
    if (select) {
      select.value = theme;
    }

    // Добавляем анимацию перехода
    body.style.transition = "background 0.3s ease, color 0.3s ease";

    // Убираем transition после анимации
    setTimeout(() => {
      body.style.transition = "";
    }, 300);
  }

  getStoredTheme() {
    try {
      return localStorage.getItem("kramdown-theme");
    } catch (e) {
      return null;
    }
  }

  storeTheme(theme) {
    try {
      localStorage.setItem("kramdown-theme", theme);
    } catch (e) {
      console.warn("Не удалось сохранить тему в localStorage");
    }
  }

  // Публичные методы
  getCurrentTheme() {
    return this.currentTheme;
  }

  setLightTheme() {
    this.setTheme("light");
  }

  setDarkTheme() {
    this.setTheme("dark");
  }

  setSystemTheme() {
    this.setTheme("system");
  }
}

// Инициализация при загрузке страницы
document.addEventListener("DOMContentLoaded", () => {
  window.themeSwitcher = new ThemeSwitcher();
});

// Экспорт для использования в других скриптах
if (typeof module !== "undefined" && module.exports) {
  module.exports = ThemeSwitcher;
}
