const ids = [];
const deudas = [];
const nombres = [];
const direcciones = [];
const telefonos = [];
const estadosDeuda = [];

function ordenarClientesPorDeuda() {
  for (let i = 0; i < deudas.length - 1; i++) {
    for (let j = 0; j < deudas.length - i - 1; j++) {
      if (deudas[j] > deudas[j + 1]) {
        [deudas[j], deudas[j + 1]] = [deudas[j + 1], deudas[j]];
        [ids[j], ids[j + 1]] = [ids[j + 1], ids[j]];
        [nombres[j], nombres[j + 1]] = [nombres[j + 1], nombres[j]];
        [direcciones[j], direcciones[j + 1]] = [direcciones[j + 1], direcciones[j]];
        [telefonos[j], telefonos[j + 1]] = [telefonos[j + 1], telefonos[j]];
        [estadosDeuda[j], estadosDeuda[j + 1]] = [estadosDeuda[j + 1], estadosDeuda[j]];
      }
    }
  }
}

function listarClientes() {
    const resultadoDiv = document.getElementById("resultado");
    resultadoDiv.innerHTML = "<h2>Listado de Clientes</h2>";

    if (ids.length === 0) {
      resultadoDiv.innerHTML += "<p>No hay clientes registrados.</p>";
      return;
    }

    let tableHtml = `
      <table>
        <tr>
          <th>ID</th>
          <th>Deuda</th>
          <th>Nombre</th>
          <th>Dirección</th>
          <th>Teléfono</th>
          <th>Estado de Deuda</th>
        </tr>
    `;

    for (let i = 0; i < ids.length; i++) {
      tableHtml += `
        <tr>
          <td>${ids[i]}</td>
          <td>${deudas[i]}</td>
          <td>${nombres[i]}</td>
          <td>${direcciones[i]}</td>
          <td>${telefonos[i]}</td>
          <td>${estadosDeuda[i]}</td>
        </tr>
      `;
    }

    tableHtml += "</table>";
    resultadoDiv.innerHTML += tableHtml;
  }
  function validarEstadoDeuda(estado) {
    return estado.toLowerCase() === "pagada" || estado.toLowerCase() === "no pagada";
  }

  function validarTelefono(telefono) {
    // Expresión regular para validar el formato de un número de teléfono (10 dígitos)
    const telefonoPattern = /^[0-9]{8}$/;
    return telefonoPattern.test(telefono);
  }



  function insertarCliente() {
    const id = parseInt(prompt("Ingrese el ID del cliente:"));

    if (isNaN(id) || id <= 0 || ids.includes(id)) {
      alert("ID inválido o duplicado.");
      return;
    }

    const deuda = parseFloat(prompt("Ingrese la deuda del cliente:"));

    if (isNaN(deuda) || deuda <= 0) {
      alert("La deuda debe ser un valor positivo.");
      return;
    }

    const nombre = prompt("Ingrese el nombre del cliente:");
    const direccion = prompt("Ingrese la dirección del cliente:");
    const telefono = prompt("Ingrese el teléfono del cliente:");
    if (!validarTelefono(telefono)) {
      alert("Ingrese un número de teléfono válido (8 dígitos numéricos).");
      return;
    }
    const estadoDeuda = prompt("Ingrese el estado de la deuda del cliente (Pagada o No pagada):");
    if (!validarEstadoDeuda(estadoDeuda)) {
      alert("El estado de la deuda debe ser 'Pagada' o 'No pagada'.");
      return;
    }

  if (!id || isNaN(deuda) || !nombre || !direccion || !telefono || !estadoDeuda) {
    alert("Todos los campos son obligatorios.");
    return;
  }
    insertarOrdenado(id, deuda, nombre, direccion, telefono, estadoDeuda);
    alert("Cliente insertado exitosamente.");
  }

function eliminarCliente() {
  const idEliminar = prompt("Ingrese el ID del cliente a eliminar:");
  const index = ids.indexOf(parseInt(idEliminar));

  if (index !== -1) {
    ids.splice(index, 1);
    deudas.splice(index, 1);
    nombres.splice(index, 1);
    direcciones.splice(index, 1);
    telefonos.splice(index, 1);
    estadosDeuda.splice(index, 1);

    alert("Cliente eliminado exitosamente.");
  } else {
    alert("Cliente no encontrado.");
  }
}

function insertarOrdenado(id, deuda, nombre, direccion, telefono, estadoDeuda) {
  let insertIndex = deudas.length;

  for (let i = 0; i < deudas.length; i++) {
    if (deuda < deudas[i]) {
      insertIndex = i;
      break;
    }
  }

  ids.splice(insertIndex, 0, id);
  deudas.splice(insertIndex, 0, deuda);
  nombres.splice(insertIndex, 0, nombre);
  direcciones.splice(insertIndex, 0, direccion);
  telefonos.splice(insertIndex, 0, telefono);
  estadosDeuda.splice(insertIndex, 0, estadoDeuda);
}

function modificarCliente() {
  const idModificar = parseInt(prompt("Ingrese el ID del cliente a modificar:"));
  const index = ids.indexOf(idModificar);

  if (index !== -1) {
    const nuevaDeuda = parseFloat(prompt("Ingrese la nueva deuda del cliente:"));
    const nuevoNombre = prompt("Ingrese el nuevo nombre del cliente:");
    const nuevaDireccion = prompt("Ingrese la nueva dirección del cliente:");
    const nuevoTelefono = prompt("Ingrese el nuevo teléfono del cliente:");
    const nuevoEstadoDeuda = prompt("Ingrese el nuevo estado de la deuda del cliente (Pagada o No pagada):");

    deudas[index] = nuevaDeuda;
    nombres[index] = nuevoNombre;
    direcciones[index] = nuevaDireccion;
    telefonos[index] = nuevoTelefono;
    estadosDeuda[index] = nuevoEstadoDeuda;

    alert("Cliente modificado exitosamente.");
  } else {
    alert("Cliente no encontrado.");
  }
}

function listarClienteEspecifico() {
  const idBuscar = parseInt(prompt("Ingrese el ID del cliente a listar:"));
  const index = ids.indexOf(idBuscar);

  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "<h2>Detalles del Cliente</h2>";

  if (index !== -1) {
    let tableHtml = `
      <table>
        <tr>
          <th>ID</th>
          <th>Deuda</th>
          <th>Nombre</th>
          <th>Dirección</th>
          <th>Teléfono</th>
          <th>Estado de Deuda</th>
        </tr>
        <tr>
          <td>${ids[index]}</td>
          <td>${deudas[index]}</td>
          <td>${nombres[index]}</td>
          <td>${direcciones[index]}</td>
          <td>${telefonos[index]}</td>
          <td>${estadosDeuda[index]}</td>
        </tr>
      </table>
    `;

    resultadoDiv.innerHTML += tableHtml;
  } else {
    resultadoDiv.innerHTML += "<p>Cliente no encontrado.</p>";
  }
}


function listarDeudasPendientes() {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "<h2>Deudas Pendientes</h2>";

  let deudasPendientesHtml = `
    <table>
      <tr>
        <th>ID</th>
        <th>Deuda</th>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Estado de Deuda</th>
      </tr>
  `;

  for (let i = 0; i < ids.length; i++) {
    if (estadosDeuda[i] === "No pagada") {
      deudasPendientesHtml += `
        <tr>
          <td>${ids[i]}</td>
          <td>${deudas[i]}</td>
          <td>${nombres[i]}</td>
          <td>${direcciones[i]}</td>
          <td>${telefonos[i]}</td>
          <td>${estadosDeuda[i]}</td>
        </tr>
      `;
    }
  }

  if (deudasPendientesHtml === `
    <table>
      <tr>
        <th>ID</th>
        <th>Deuda</th>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Estado de Deuda</th>
      </tr>
    `) {
    resultadoDiv.innerHTML += "<p>No hay deudas pendientes.</p>";
  } else {
    deudasPendientesHtml += "</table>";
    resultadoDiv.innerHTML += deudasPendientesHtml;
  }
}


function listarClientesSinDeudas() {
  const resultadoDiv = document.getElementById("resultado");
  resultadoDiv.innerHTML = "<h2>Clientes sin Deudas</h2>";

  let clientesSinDeudasHtml = `
    <table>
      <tr>
        <th>ID</th>
        <th>Deuda</th>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Estado de Deuda</th>
      </tr>
  `;

  for (let i = 0; i < ids.length; i++) {
    if (estadosDeuda[i] === "Pagada") {
      clientesSinDeudasHtml += `
        <tr>
          <td>${ids[i]}</td>
          <td>${deudas[i]}</td>
          <td>${nombres[i]}</td>
          <td>${direcciones[i]}</td>
          <td>${telefonos[i]}</td>
          <td>${estadosDeuda[i]}</td>
        </tr>
      `;
    }
  }

  if (clientesSinDeudasHtml === `
    <table>
      <tr>
        <th>ID</th>
        <th>Deuda</th>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Estado de Deuda</th>
      </tr>
    `) {
    resultadoDiv.innerHTML += "<p>No hay clientes sin deudas.</p>";
  } else {
    clientesSinDeudasHtml += "</table>";
    resultadoDiv.innerHTML += clientesSinDeudasHtml;
  }
}
