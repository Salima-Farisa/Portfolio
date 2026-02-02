const toggle = document.getElementById("themeToggle");
const html = document.documentElement;

toggle.addEventListener("click", () => {
    const current = html.getAttribute("data-bs-theme");
    const next = current === "dark" ? "light" : "dark";
    html.setAttribute("data-bs-theme", next);
    localStorage.setItem("theme", next);
    toggle.textContent = next === "dark" ? "🌙" : "☀️";
});
