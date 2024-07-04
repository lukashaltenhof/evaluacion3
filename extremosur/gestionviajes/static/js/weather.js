$(document).ready(function () {
    const settings = {
        async: true,
        crossDomain: true,
        url: 'https://yahoo-weather5.p.rapidapi.com/weather?location=Punta%20Arenas&format=json&u=c',
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': 'e7d197f213mshc0d6e3708daf68dp1b715cjsn4a23d3475127',
            'X-RapidAPI-Host': 'yahoo-weather5.p.rapidapi.com'
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response.forecasts);
        $.each(response.forecasts, function (i, item) {
            var iconClass = getWeatherIconClass(item.code); // Obtener la clase del icono del clima
            var html = `
                <div class="forecast-item">
                    <h3>${item.day}</h3>
                    <i class="${iconClass}"></i>
                    <p><strong>Mínima:</strong> ${item.low} °C</p>
                    <p><strong>Máxima:</strong> ${item.high} °C</p>
                </div>`;
            $("#Pronostico").append(html);
        })
    });

    function getWeatherIconClass(weatherCode) {
        var weatherIcons = {
            "32": "wi wi-day-sunny",           // Soleado
            "11": "wi wi-rain",                // Lluvia
            "26": "wi wi-cloud",               // Nublado
            "34": "wi wi-day-cloudy",          // Parcialmente nublado
            "28": "wi wi-day-cloudy-high",     // Mayormente nublado
            "16": "wi wi-snow"                 // Nieve
            // Agrega más códigos de clima y las clases correspondientes aquí
        };
        // Si no hay una clase definida para el código de clima, usa una clase por defecto
        return weatherIcons[weatherCode] || "wi wi-day-sunny";
    }
});