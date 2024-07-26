from parking.Usuario import Usuario


class Registro:
    def __init__(self, db):
        self.db = db
        self.usuarios = []

    def registrar_usuario(self):
        print("\n--- Registro de Usuario ---")
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")

        # Verificar si el nombre de usuario ya existe
        query = "SELECT username FROM usuarios WHERE username = %s"
        result = self.db.fetch_query(query, (username,))
        if result:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
            return

        usuario = Usuario(username, password,)
        usuario.guardar_en_bd(self.db)
        self.usuarios.append(usuario)
