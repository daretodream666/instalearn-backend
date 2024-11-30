const themeToggle = document.getElementById('theme-toggle');
const rootElement = document.documentElement;

if (typeof(Storage) !== "undefined") {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        rootElement.classList.add(savedTheme);
        themeToggle.textContent = savedTheme === 'light-theme' ? '☀️' : '🌙';
    } else {
        localStorage.setItem('theme', 'dark-theme');
        themeToggle.textContent = '🌙';
    }

    themeToggle.addEventListener('click', () => {
        if (rootElement.classList.contains('light-theme')) {
            rootElement.classList.remove('light-theme');
            themeToggle.textContent = '🌙';
            localStorage.setItem('theme', 'dark-theme');
        } else {
            rootElement.classList.add('light-theme');
            themeToggle.textContent = '☀️';
            localStorage.setItem('theme', 'light-theme');
        }
    });
} else {
    console.warn('Ваш браузер не поддерживает localStorage');
}
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
});
