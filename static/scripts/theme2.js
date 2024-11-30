document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    const root = document.documentElement;
    const localTheme = localStorage.getItem("theme");

    // Apply saved theme
    if (localTheme) {
        root.classList.add(localTheme);
        themeToggle.textContent = localTheme === "light-theme" ? "🌙" : "☀️";
    }

    // Toggle theme
    themeToggle.addEventListener("click", () => {
        const isLight = root.classList.toggle("light-theme");
        themeToggle.textContent = isLight ? "🌙" : "☀️";
        localStorage.setItem("theme", isLight ? "light-theme" : "");
    });

    // Fetch skill data from backend
    fetch("/api/skill")
        .then(response => response.json())
        .then(data => {
            const { title, description, videos } = data;
            document.getElementById("skill-title").textContent = title;
            document.getElementById("skill-description").textContent = description;

            // Select a random video
            const randomVideo = videos[Math.floor(Math.random() * videos.length)];
            document.getElementById("skill-video").src = `https://www.youtube.com/embed/${randomVideo}`;
        })
        .catch(error => {
            console.error("Error fetching skill data:", error);
        });
});
