
$(document).ready(function() {
    $('#formularioPreguntas').submit(function(e) {
        e.preventDefault(); // Evita el envío tradicional del formulario

        $.ajax({
            url: '/cargar_contenido',
            type: 'POST',
            success: function(response) {
                $('#respuesta').html(response); // Inserta el contenido en el div
                $('#miModal').fadeIn();
            },
            error: function() {
                alert('Hubo un error al cargar el contenido.');
            }
        });
    });
}); 

fetch('/datos')
.then(response => response.json())
.then(data => {
    const lista = document.getElementById('lista');
    data.forEach(row => {
        const item = document.createElement('li');
        item.textContent = JSON.stringify(row);
        lista.appendChild(item);
    });
});

function enviarFormulario(){
    // Obtener los datos del formulario
    const formData = new FormData(document.getElementById('Idformulario'));
    const datos = Object.fromEntries(formData); // Convertir a objeto JS

    // Realizar la llamada AJAX
    fetch('/procesar_formulario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
            body: JSON.stringify(datos) // Enviar datos como JSON
    })
    .then(response => response.json()) // Parsear la respuesta como JSON
    .then(data => {
        // Mostrar la respuesta JSON en el div
        document.getElementById('resultado').innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultado').innerText = 'Error al procesar la solicitud';
    });
}
