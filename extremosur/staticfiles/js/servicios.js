document.addEventListener("DOMContentLoaded", function() {
    // Set a timeout of 3 seconds (3000 milliseconds)
    setTimeout(function() {
        // Hide the spinner and show the content for the first card
        document.getElementById('spinner1').style.visibility = 'hidden';  // Oculta el spinner de la primera card
        document.getElementById('content1').classList.remove('d-none'); // Muestra el contenido de la primera card
        document.getElementById('img1').classList.remove('d-none'); // Muestra la imagen de la primera card

        // Hide the spinner and show the content for the second card
        document.getElementById('spinner2').style.visibility = 'hidden'; // Oculta el spinner de la segunda card
        document.getElementById('content2').classList.remove('d-none'); // Muestra el contenido de la segunda card
        document.getElementById('img2').classList.remove('d-none'); // Muestra la imagen de la segunda card

        // Hide the spinner and show the content for the third card
        document.getElementById('spinner3').style.visibility = 'hidden'; // Oculta el spinner de la tercera card
        document.getElementById('content3').classList.remove('d-none'); // Muestra el contenido de la tercera card
        document.getElementById('img3').classList.remove('d-none'); // Muestra la imagen de la tercera card
    }, 2000); // Tiempo de espera de 3 segundos
});