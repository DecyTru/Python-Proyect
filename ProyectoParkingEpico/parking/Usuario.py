class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def guardar_en_bd(self, db):
        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        values = (self.username, self.password)
        db.execute_query(query, values)

    @staticmethod
    def eliminar_de_bd(username, db):
        query = "DELETE FROM usuarios WHERE username = %s"
        db.execute_query(query, (username,))

    @staticmethod
    def consultar_todos(db):
        query = "SELECT * FROM usuarios"
        return db.fetch_all(query)
