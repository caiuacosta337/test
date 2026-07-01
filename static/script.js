const root = document.documentElement;
const themeToggle = document.getElementById("themeToggle");
const themeLabel = document.getElementById("themeLabel");
const themeIcon = document.getElementById("themeIcon");

const preferredTheme = window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";

function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    if (themeLabel && themeIcon) {
        themeLabel.textContent = theme === "dark" ? "Dark" : "Light";
        themeIcon.textContent = theme === "dark" ? "🌙" : "☀️";
    }
}

const initialTheme = localStorage.getItem("theme") || preferredTheme;
applyTheme(initialTheme);

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        localStorage.setItem("theme", nextTheme);
        applyTheme(nextTheme);
    });
}
