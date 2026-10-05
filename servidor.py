import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DB_NAME = "database.db"

def get_db_connection():
    """Establezco conexion con la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route('/registro', methods=['POST'])
def registro():
    """Endpoint para registrar nuevos usuarios con contraseña hasheada."""
    datos = request.get_json()

    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({"mensaje": "Datos incompletos. Se requiere 'usuario' y 'contraseña'."}), 400

    usuario = datos['usuario'].strip()
    password = datos['contraseña']

    if not usuario or not password:
        return jsonify({"mensaje": "El usuario y la contraseña no pueden estar vacios."}), 400


    hash_seguro = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)",
            (usuario, hash_seguro)
        )
        conn.commit()
        return jsonify({"mensaje": "Usuario registrado exitosamente."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"mensaje": "El nombre de usuario ya existe."}), 409
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)