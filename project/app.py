import secrets
from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3
from datetime import datetime
secret_key = secrets.token_hex(32)
app = Flask(__name__)
app.secret_key = secret_key

# Ruta de inicio
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('home.html', username=username)
    return render_template('home.html')

# Ruta de cierre de sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verificar las credenciales del usuario en la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]  # Almacenar el nombre de usuario en la sesión
            print("Nombre de usuario almacenado en la sesión:", session['username'])  # Depuración
            return redirect('/inicio')
        else:
            return "Credenciales inválidas. Inténtalo nuevamente."
    else:
        return render_template('login.html')

# Ruta de contacto
@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

# Ruta de información
@app.route('/informacion')
def informacion():
    return render_template("informacion.html")

# Ruta de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        # Verificar si el correo electrónico ya existe en la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            conn.close()
            return "El correo electrónico ya está registrado"

        # Intentar insertar el nuevo usuario en la base de datos
        try:
            cursor.execute('INSERT INTO user (username, email, name, password) VALUES (?, ?, ?, ?)',
                           (username, email, name, password))
            conn.commit()
            conn.close()
            return redirect('/')
        except sqlite3.IntegrityError:
            conn.close()
            return "Error al registrar el usuario. Inténtalo nuevamente."
    else:
        if 'username' in session:
            return redirect('/login')
        return render_template('registro.html')

# Ruta de inicio con psets
@app.route('/inicio')
def inicio():
    if 'username' in session:
        # Obtener los datos del usuario de la sesión
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM user WHERE username = ?', (session['username'],))
        user = cursor.fetchone()

        print("Nombre de usuario almacenado en la sesión:", session['username'])  # Depuración

        if user is None:
            conn.close()
            return "Usuario no encontrado. Por favor, inicia sesión nuevamente."

        user_id = user[0]
        print("ID de usuario obtenido:", user_id)  # Depuración

        # Obtener los psets relacionados con el ID del usuario
        cursor.execute('SELECT * FROM psets INNER JOIN user ON psets.user_id = user.id WHERE psets.user_id = ?', (user_id,))
        rows = cursor.fetchall()

        conn.close()

        if len(rows) == 0:
            message = 'No se han creado psets todavía.'
            return render_template('inicio.html', message=message)
        else:
            psets = []
            column_names = [description[0] for description in cursor.description]
            for row in rows:
                pset = dict(zip(column_names, row))
                psets.append(pset)

            return render_template('inicio.html', psets=psets)
    else:
        return redirect('/login')
@app.route('/vencimiento')
def vencimiento():
    if 'username' in session:
        # Obtener los datos del usuario de la sesión
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM user WHERE username = ?', (session['username'],))
        user = cursor.fetchone()

        print("Nombre de usuario almacenado en la sesión:", session['username'])  # Depuración

        if user is None:
            conn.close()
            return "Usuario no encontrado. Por favor, inicia sesión nuevamente."

        user_id = user[0]
        print("ID de usuario obtenido:", user_id)  # Depuración

        # Obtener los psets relacionados con el ID del usuario y que tengan un valor "False" en una columna específica
        cursor.execute('SELECT * FROM psets WHERE user_id = ? AND estado = ?', (user_id, False))
        rows = cursor.fetchall()

        conn.close()

        if len(rows) == 0:
            message = 'No se han encontrado psets con valor "False" para este usuario.'
            return render_template('vencimiento.html', message=message)
        else:
            psets = []
            column_names = [description[0] for description in cursor.description]
            for row in rows:
                pset = dict(zip(column_names, row))
                psets.append(pset)

            return render_template('vencimiento.html', psets=psets)
    else:
        return redirect('/login')
@app.route('/realizados')
def realizados():
    if 'username' in session:
        # Obtener los datos del usuario de la sesión
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM user WHERE username = ?', (session['username'],))
        user = cursor.fetchone()

        print("Nombre de usuario almacenado en la sesión:", session['username'])  # Depuración

        if user is None:
            conn.close()
            return "Usuario no encontrado. Por favor, inicia sesión nuevamente."

        user_id = user[0]
        print("ID de usuario obtenido:", user_id)  # Depuración

        # Obtener los psets relacionados con el ID del usuario y que tengan un valor "True" en la columna "estado"
        cursor.execute('SELECT * FROM psets WHERE user_id = ? AND estado = ?', (user_id, True))
        rows = cursor.fetchall()

        conn.close()

        if len(rows) == 0:
            message = 'No se han encontrado psets con valor "True" para este usuario.'
            return render_template('vencimiento.html', message=message)
        else:
            psets = []
            column_names = [description[0] for description in cursor.description]
            for row in rows:
                pset = dict(zip(column_names, row))
                psets.append(pset)

            return render_template('realizados.html', psets=psets)
    else:
        return redirect('/login')





# Ruta para crear un nuevo pset
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if 'username' in session:
        if request.method == 'POST':
            titulo = request.form['titulo']
            descripcion = request.form['descripcion']
            fecha_creacion = request.form['fecha_creacion']
            fecha_vencimiento = request.form['fecha_vencimiento']

            # Obtener el ID del usuario de la sesión
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM user WHERE username = ?', (session['username'],))
            user_row = cursor.fetchone()

            if user_row is not None:
                user_id = user_row[0]
                # Resto del código
            else:
                conn.close()
                return "Usuario no encontrado. Por favor, inicia sesión nuevamente."

            # Obtener la fecha actual
            fecha_actual = datetime.now().strftime('%Y-%m-%d')

            # Verificar si la fecha de vencimiento ha pasado
            estado = fecha_actual <= fecha_vencimiento

            # Insertar el nuevo pset en la base de datos
            cursor.execute('INSERT INTO psets (user_id, titulo, descripcion, fecha_creacion, fecha_vencimiento, estado) '
                           'VALUES (?, ?, ?, ?, ?, ?)',
                           (user_id, titulo, descripcion, fecha_creacion, fecha_vencimiento, estado))
            conn.commit()
            conn.close()

            return redirect(url_for('inicio'))

        return render_template('crear.html')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run()






