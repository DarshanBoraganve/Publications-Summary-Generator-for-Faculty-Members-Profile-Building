document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const sidebar = document.querySelector(".sidebar");

    // Sidebar toggle event
    menuToggle.addEventListener("click", () => {
        sidebar.classList.toggle("active");
    });

    // Sample publication data (replace this with dynamic Flask data)
    const years = [2018, 2019, 2020, 2021, 2022, 2023, 2024];
    const publications = [5, 8, 14, 18, 20, 22, 25]; // Example data

    // Chart.js Configuration
    const ctx = document.getElementById("publicationChart").getContext("2d");
    new Chart(ctx, {
        type: "line",
        data: {
            labels: years,
            datasets: [{
                label: "Publications Per Year",
                data: publications,
                borderColor: "#007BFF",
                backgroundColor: "rgba(0, 123, 255, 0.2)",
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { title: { display: true, text: "Year" } },
                y: { title: { display: true, text: "Publications" }, beginAtZero: true }
            }
        }
        
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const darkModeToggle = document.getElementById("dark-mode-toggle");

    // Dark mode toggle event
    darkModeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });

    // Sidebar toggle event
    const menuToggle = document.querySelector(".menu-toggle");
    const sidebar = document.querySelector(".sidebar");

    menuToggle.addEventListener("click", () => {
        sidebar.classList.toggle("active");


        document.addEventListener("DOMContentLoaded", () => {
            const menuToggle = document.querySelector(".menu-toggle");
            const sidebar = document.querySelector(".sidebar");
        
            // Sidebar toggle event
            menuToggle.addEventListener("click", () => {
                sidebar.classList.toggle("active");
            });
        
            // Dark mode toggle event
            const darkModeToggle = document.getElementById("dark-mode-toggle");
            if (darkModeToggle) {
                darkModeToggle.addEventListener("click", () => {
                    document.body.classList.toggle("dark-mode");
                });
            }
        });

    });
});
