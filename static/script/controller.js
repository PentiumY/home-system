"use strict";
console.log('Controller loaded!');
var lightOn = false;
function ledSwitch(state, itemID) {
    var dataToSend = {
        itemID: 1,
        state: state
    };
    fetch('/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
    })
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
        .then(data => {
        console.log('Received response from server:', data);
    })
        .catch(error => {
        console.error('Error sending data to server:', error);
    });
}
document.addEventListener('DOMContentLoaded', function () {
    console.log('Website loaded!');
    const button = document.getElementById("led-switch");
    if (button) {
        button.addEventListener("click", function (event) {
            lightOn = !lightOn;
            ledSwitch(lightOn, 1);
            console.log(lightOn);
        });
    }
});
