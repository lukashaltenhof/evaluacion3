function cambiarColorTitulo() {
    var titulo = document.querySelector('#quienes-somos h1');
    titulo.style.color = getRandomColor();
}

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function modifyItemQuantity(itemId, action) {
    $.ajax({
        url: '/path/to/modify_quantity/', // Make sure to replace this with the actual URL to your view
        type: 'POST',
        data: JSON.stringify({ itemId: itemId, action: action }),
        contentType: 'application/json; charset=utf-8',
        headers: { "X-CSRFToken": getCookie("csrftoken") }, // Ensure CSRF token is included if needed
        dataType: 'json',
        success: function(response) {
            if(response.success) {
                $('#quantity-' + itemId).text(response.newQuantity);
            }
        }
    });
}

// Helper function to get CSRF token for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Helper function to get CSRF token for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function clearCartAndNotify() {
    $.ajax({
        url: '/path/to/ver_carrito/', // Replace with the actual URL to your Django view
        type: 'POST',
        data: '{}',
        contentType: 'application/json; charset=utf-8',
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        success: function(response) {
            if(response.success) {
                alert("Has pagado");
                // Optionally, redirect to a different page or update the UI to reflect the empty cart
            }
        }
    });
}