document.addEventListener("DOMContentLoaded", () => {
    console.log("PDFResultKhoj page loaded.");

    // Navbar toggle for mobile
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    // Future enhancement: live filtering, debounce, AJAX
});