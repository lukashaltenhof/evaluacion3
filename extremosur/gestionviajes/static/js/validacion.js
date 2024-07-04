$(document).ready(function () {
    $('#contact-form').submit(function (e) {
        e.preventDefault();

        var nombre = $('#nombre').val();
        var celular = $('#celular').val();
        var email = $('#email').val();
        var pais = $('#pais').val();
        var ciudad = $('#ciudad').val();
        var consulta = $('#consulta').val();

        if (nombre === '' || celular === '' || email === '' || pais === '' || ciudad === '' || consulta === '') {
            alert('Por favor completa todos los campos obligatorios.');
            return;
        }

        var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert('Por favor ingresa un email válido.');
            return;
        }

        var phonePattern = /^\d+$/;
        if (!phonePattern.test(celular)) {
            alert('Por favor ingresa un número de teléfono válido.');
            return;
        }

        setTimeout(function () {
            alert('El formulario se ha enviado correctamente.');
            $('#contact-form')[0].reset(); 
        }, 1000);
    });
});


$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});