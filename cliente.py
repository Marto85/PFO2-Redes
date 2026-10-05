import sys
import requests

BASE_URL = "http://127.0.0.1:5000"

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    usuario = input("Ingrese nombre de usuario: ").strip()
    password = input("Ingrese contraseña: ").strip()

    if not usuario or not password:
        print("[!] El usuario y la contraseña no pueden estar vacios.")
        return

    payload = {
        "usuario": usuario,
        "contraseña": password
    }

    try:
        respuesta = requests.post(f"{BASE_URL}/registro", json=payload)
        datos = respuesta.json()
        print(f"Estado HTTP: {respuesta.status_code}")
        print(f"Respuesta: {datos.get('mensaje')}")
    except requests.exceptions.ConnectionError:
        print("[X] Error: No se pudo conectar al servidor. Asegurate de que servidor.py este corriendo.")

def iniciar_sesion():
    print("\n--- Inicio de Sesion ---")
    usuario = input("Ingrese su usuario: ").strip()
    password = input("Ingrese su contraseña: ").strip()

    if not usuario or not password:
        print("[!] El usuario y la contraseña no pueden estar vacios.")
        return False

    payload = {
        "usuario": usuario,
        "contraseña": password
    }

    try:
        respuesta = requests.post(f"{BASE_URL}/login", json=payload)
        datos = respuesta.json()
        print(f"Estado HTTP: {respuesta.status_code}")
        print(f"Respuesta: {datos.get('mensaje')}")
        return respuesta.status_code == 200
    except requests.exceptions.ConnectionError:
        print("[X] Error: No se pudo conectar al servidor. Asegurate de que servidor.py este corriendo.")
        return False

def consultar_tareas():
    print("\n--- Consultar /tareas ---")
    try:
        respuesta = requests.get(f"{BASE_URL}/tareas")
        print(f"Estado HTTP: {respuesta.status_code}")
        if respuesta.status_code == 200:
            print("[+] HTML de bienvenida recibido correctamente desde el servidor.")
            print(f"Tamaño del contenido recibido: {len(respuesta.text)} bytes.")
        else:
            print("[!] No se pudo obtener la vista de tareas.")
    except requests.exceptions.ConnectionError:
        print("[X] Error: No se pudo conectar al servidor.")

def menu():
    while True:
        print("\n===============================")
        print("  CLIENTE DE GESTION DE TAREAS ")
        print("===============================")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesion")
        print("3. Consultar /tareas (GET)")
        print("0. Salir")
        print("===============================")
        
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            consultar_tareas()
        elif opcion == "0":
            print("Cerrando el cliente. ¡Hasta luego!")
            sys.exit(0)
        else:
            print("[!] Opcion no valida, intente nuevamente.")

if __name__ == "__main__":
    menu()