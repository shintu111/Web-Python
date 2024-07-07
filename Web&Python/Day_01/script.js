// Task 3: Write JavaScript to validate forms on the client side to provide immediate feedback on user input errors before submission.

// script.js
document.addEventListener("DOMContentLoaded", function() {
    const registrationForm = document.getElementById("registration-form");
    const loginForm = document.getElementById("login-form");

    registrationForm.addEventListener("submit", validateRegistrationForm);
    loginForm.addEventListener
});