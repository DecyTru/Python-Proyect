# En Vehiculo.py
class Vehiculo:
    def __init__(self, placa, tipo, hora, minuto, db) -> None:
        self._placa = placa
        self._tipo = tipo
        self._hora = hora
        self._minuto = minuto
        self._total_a_pagar = 0
        self._db = db

    def calcular_valor_a_pagar(self):
        valor_minutos = self.obtener_tarifa()
        tiempo_en_minutos = self._hora * 60 + self._minuto
        self._total_a_pagar = tiempo_en_minutos * valor_minutos / 10  # Dividir entre 10 para ajustar el valor

    def obtener_tarifa(self):
        query = "SELECT tarifa_por_hora FROM tarifas WHERE tipo = %s"
        result = self._db.fetch_query(query, (self._tipo,))
        return result[0] if result else 0

    def guardar_en_bd(self):
        self.calcular_valor_a_pagar()
        query = """
        INSERT INTO vehiculos (placa, tipo, hora, minuto, total_a_pagar) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (self._placa, self._tipo, self._hora, self._minuto, self._total_a_pagar)
        self._db.execute_query(query, values)

    def eliminar_de_bd(self):
        query = "DELETE FROM vehiculos WHERE placa = %s"
        self._db.execute_query(query, (self._placa,))

    def consultar_de_bd(self):
        query = "SELECT placa, tipo, hora, minuto, total_a_pagar FROM vehiculos WHERE placa = %s"
        result = self._db.fetch_query(query, (self._placa,))
        if result:
            self._placa, self._tipo, self._hora, self._minuto, self._total_a_pagar = result
            return True
        else:
            print("Vehículo no encontrado.")
            return False

    def __str__(self):
        return f"| Placa: {self._placa} | Tipo: {self._tipo} | Horas: {self._hora} | Minutos: {self._minuto} | Valor a pagar: {self._total_a_pagar} |"

class Carro(Vehiculo):
    def __init__(self, placa, hora, minuto, db) -> None:
        super().__init__(placa, "Carro", hora, minuto, db)

class Moto(Vehiculo):
    def __init__(self, placa, hora, minuto, db) -> None:
        super().__init__(placa, "moto", hora, minuto, db)

class Mula(Vehiculo):
    def __init__(self, placa, hora, minuto, db) -> None:
        super().__init__(placa, "mula", hora, minuto, db)
