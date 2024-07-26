import mysql.connector

class Database:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            print("Query ejecutada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar query: {err}")
        finally:
            cursor.close()

    def fetch_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(f"Error al ejecutar query: {err}")
        finally:
            cursor.close()

    def fetch_all(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error al ejecutar query: {err}")
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
