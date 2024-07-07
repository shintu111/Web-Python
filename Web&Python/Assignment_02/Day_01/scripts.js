// Task 3: Use JavaScript to dynamically update route options on the client side based on user interactions.
// script.js

const originInput = document.getElementById('origin');
const destinationInput = document.getElementById('destination');
const modeSelect = document.getElementById('mode');
const routeOptionsDiv = document.getElementById('route-options');

// add event listener to form submission
document.addEventListener('submit', (e) => {
    e.preventDefault();
    const origin = originInput.value;
    const destination = destinationInput.value;
    const mode = modeSelect.value;

    // make API call to retrieve route options
    fetch('/api/route-options', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ origin, destination, mode })
    })
   .then(response =>
