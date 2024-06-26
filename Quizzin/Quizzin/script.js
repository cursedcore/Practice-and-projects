function changeContent() {
  const container = document.querySelector('.container');
  const img = container.querySelector('img');

  container.style.backgroundColor = '#ffcc00'; // Cambiar el fondo a amarillo
  img.style.display = 'none'; // Ocultar la imagen
  container.innerHTML = '<p>Texto al pasar el cursor</p>';
}

function resetContent() {
  const container = document.querySelector('.container');
  const img = container.querySelector('img');

  container.style.backgroundColor = '#3498db'; // Restablecer el fondo original
  img.style.display = 'block'; // Mostrar la imagen
  container.innerHTML = ''; // Borrar el texto
}
