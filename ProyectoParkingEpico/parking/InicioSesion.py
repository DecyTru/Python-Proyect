class InicioSesion:
    def __init__(self, db):
        self.db = db

    def iniciar_sesion(self):
        print("\n--- Inicio de Sesión ---")
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")

        query = "SELECT id FROM usuarios WHERE username = %s AND password = %s"
        result = self.db.fetch_query(query, (username, password))
        if result:
            print("Inicio de sesión exitoso.")
            return result[0]
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None
