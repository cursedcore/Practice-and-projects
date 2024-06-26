// Arreglos para almacenar los datos
const carnets = [];
const nombres = [];
const nombresProyecto = [];
const fechasEntrega = [];
const fechasLimite = [];
const calificaciones = [];

// Funciones para manipular los datos

function listarRegistros() {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "<h2>Listado de Registros</h2>";
  ordenarRegistrosPorFecha();


  if (carnets.length === 0) {
    resultadoDiv.innerHTML += "<p>No hay registros de entregas.</p>";
    return;
  }

  let tableHtml = `
    <table>
      <tr>
        <th>Carnet</th>
        <th>Nombres y Apellido</th>
        <th>Nombre del Proyecto</th>
        <th>Fecha de Entrega</th>
        <th>Fecha Límite de Entrega</th>
        <th>Calificación</th>
      </tr>
  `;

  for (let i = 0; i < carnets.length; i++) {
    tableHtml += `
      <tr>
        <td>${carnets[i]}</td>
        <td>${nombres[i]}</td>
        <td>${nombresProyecto[i]}</td>
        <td>${fechasEntrega[i]}</td>
        <td>${fechasLimite[i]}</td>
        <td>${calificaciones[i]}</td>
      </tr>
    `;
  }

  tableHtml += "</table>";
  resultadoDiv.innerHTML += tableHtml;
}

function eliminarEntrega() {
  const carnet = prompt("Ingrese el carnet del estudiante:");
  if (!carnet) return;

  const index = carnets.indexOf(carnet);
  if (index !== -1) {
    carnets.splice(index, 1);
    nombres.splice(index, 1);
    nombresProyecto.splice(index, 1);
    fechasEntrega.splice(index, 1);
    fechasLimite.splice(index, 1);
    calificaciones.splice(index, 1);
    alert("Entrega eliminada correctamente.");
  } else {
    alert("No se encontró ninguna entrega con ese carnet.");
  }
}

function mostrarFormularioInsertar() {
  const formularioDiv = document.getElementById("formulario");
  formularioDiv.innerHTML = `
    <h2>Insertar Entrega</h2>
    <form id="formularioInsertar">
      <label for="carnet">Carnet:</label>
      <input type="text" id="carnet" required><br>
      <label for="nombres">Nombres y Apellido:</label>
      <input type="text" id="nombres" required><br>
      <label for="nombreProyecto">Nombre del Proyecto:</label>
      <input type="text" id="nombreProyecto" required><br>
      <label for="fechaEntrega">Fecha de Entrega:</label>
      <input type="date" id="fechaEntrega" required><br>
      <label for="fechaLimite">Fecha Límite de Entrega:</label>
      <input type="date" id="fechaLimite" required><br>
      <label for="calificacion">Calificación:</label>
      <input type="number" id="calificacion" required><br>
      <button type="button" onclick="insertarEntrega()">Insertar</button>
    </form>
  `;
}

function insertarEntrega() {
  const carnet = document.getElementById("carnet").value;
  const nombresValor = document.getElementById("nombres").value;
  const nombreProyecto = document.getElementById("nombreProyecto").value;
  const fechaEntrega = document.getElementById("fechaEntrega").value;
  const fechaLimite = document.getElementById("fechaLimite").value;
  const calificacion = document.getElementById("calificacion").value;

  if (!carnet || !nombresValor || !nombreProyecto || !fechaEntrega || !fechaLimite || !calificacion) {
    alert("Todos los campos son obligatorios.");
    return;
  }

  if (calificacion < 0 || isNaN(calificacion)) {
    alert("La calificación debe ser un número positivo.");
    return;
  }

  carnets.push(carnet);
  nombres.push(nombresValor);
  nombresProyecto.push(nombreProyecto);
  fechasEntrega.push(fechaEntrega);
  fechasLimite.push(fechaLimite);
  calificaciones.push(calificacion);

  alert("Entrega insertada correctamente.");
  document.getElementById("formularioInsertar").reset();
}

function mostrarFormularioModificar() {
  const formularioDiv = document.getElementById("formulario");
  formularioDiv.innerHTML = `
    <h2>Modificar Entrega</h2>
    <form id="formularioModificar">
      <label for="carnetModificar">Carnet:</label>
      <input type="text" id="carnetModificar" required><br>
      <label for="calificacionModificar">Nueva Calificación:</label>
      <input type="number" id="calificacionModificar" required><br>
      <button type="button" onclick="modificarEntrega()">Modificar</button>
    </form>
  `;
}

function modificarEntrega() {
  const carnetModificar = document.getElementById("carnetModificar").value;
  const calificacionModificar = document.getElementById("calificacionModificar").value;

  if (!carnetModificar || calificacionModificar < 0 || isNaN(calificacionModificar)) {
    alert("Ingrese un carnet válido y una calificación positiva.");
    return;
  }

  const index = carnets.indexOf(carnetModificar);
  if (index !== -1) {
    calificaciones[index] = calificacionModificar;
    alert("Calificación modificada correctamente.");
  } else {
    alert("No se encontró ninguna entrega con ese carnet.");
  }
  document.getElementById("formularioModificar").reset();
}

function mostrarFormularioProyectoEspecifico() {
  const formularioDiv = document.getElementById("formulario");
  formularioDiv.innerHTML = `
    <h2>Mostrar Proyecto Específico</h2>
    <form id="formularioProyectoEspecifico">
      <label for="carnetMostrar">Carnet:</label>
      <input type="text" id="carnetMostrar" required><br>
      <button type="button" onclick="mostrarProyectoEspecifico()">Mostrar</button>
    </form>
  `;
}

function mostrarProyectoEspecifico() {
  const carnetMostrar = document.getElementById("carnetMostrar").value;

  if (!carnetMostrar) {
    alert("Ingrese un carnet válido.");
    return;
  }

  const index = carnets.indexOf(carnetMostrar);
  if (index !== -1) {
    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = "<h2>Proyecto Específico</h2>";
    resultadoDiv.innerHTML += `
      <p><strong>Carnet:</strong> ${carnets[index]}</p>
      <p><strong>Nombres y Apellido:</strong> ${nombres[index]}</p>
      <p><strong>Nombre del Proyecto:</strong> ${nombresProyecto[index]}</p>
      <p><strong>Fecha de Entrega:</strong> ${fechasEntrega[index]}</p>
      <p><strong>Fecha Límite de Entrega:</strong> ${fechasLimite[index]}</p>
      <p><strong>Calificación:</strong> ${calificaciones[index]}</p>
    `;
  } else {
    alert("No se encontró ninguna entrega con ese carnet.");
  }
  document.getElementById("formularioProyectoEspecifico").reset();
}

function listarProyectosFueraDeFecha() {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "<h2>Proyectos Fuera de Fecha Límite</h2>";

  let hayProyectosFueraDeFecha = false;

  ordenarRegistrosPorFecha();

  for (let i = 0; i < carnets.length; i++) {
    if (fechasEntrega[i] > fechasLimite[i]) {
      resultadoDiv.innerHTML += `
        <p><strong>Carnet:</strong> ${carnets[i]}</p>
        <p><strong>Nombres y Apellido:</strong> ${nombres[i]}</p>
        <p><strong>Nombre del Proyecto:</strong> ${nombresProyecto[i]}</p>
        <p><strong>Fecha de Entrega:</strong> ${fechasEntrega[i]}</p>
        <p><strong>Fecha Límite de Entrega:</strong> ${fechasLimite[i]}</p>
        <p><strong>Calificación:</strong> ${calificaciones[i]}</p>
      `;
      hayProyectosFueraDeFecha = true;
    }
  }

  if (!hayProyectosFueraDeFecha) {
    resultadoDiv.innerHTML += "<p>No hay proyectos fuera de fecha.</p>";
  }
}
function ordenarRegistrosPorFecha() {
    const n = carnets.length;

    for (let i = 0; i < n - 1; i++) {
      let minIndex = i;
      for (let j = i + 1; j < n; j++) {
        const fechaEntregaI = new Date(fechasEntrega[minIndex]);
        const fechaEntregaJ = new Date(fechasEntrega[j]);
        if (fechaEntregaJ < fechaEntregaI) {
          minIndex = j;
        }
      }

      if (minIndex !== i) {
        [carnets[i], carnets[minIndex]] = [carnets[minIndex], carnets[i]];
        [nombres[i], nombres[minIndex]] = [nombres[minIndex], nombres[i]];
        [nombresProyecto[i], nombresProyecto[minIndex]] = [nombresProyecto[minIndex], nombresProyecto[i]];
        [fechasEntrega[i], fechasEntrega[minIndex]] = [fechasEntrega[minIndex], fechasEntrega[i]];
        [fechasLimite[i], fechasLimite[minIndex]] = [fechasLimite[minIndex], fechasLimite[i]];
        [calificaciones[i], calificaciones[minIndex]] = [calificaciones[minIndex], calificaciones[i]];
      }
    }
  }

