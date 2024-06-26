import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conn = sqlite3.connect('usuarios.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla 'user' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username VARCHAR(80) NOT NULL UNIQUE,
        email VARCHAR(120) NOT NULL UNIQUE,
        name VARCHAR(80) NOT NULL,
        password VARCHAR(80) NOT NULL
    )
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()


