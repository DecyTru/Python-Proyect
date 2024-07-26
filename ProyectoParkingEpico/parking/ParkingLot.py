from Vehiculo import Carro, Moto, Mula, Vehiculo


class ParkingLot:
    def __init__(self, db) -> None:
        self.db = db

    def gestionar_estacionamiento(self):
        while True:
            print("\n1 - Registrar vehículo")
            print("2 - Consultar vehículo")
            print("3 - Eliminar vehículo")
            print("4 - Salir")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.registrar_vehiculo()
            elif opcion == 2:
                self.consultar_vehiculo()
            elif opcion == 3:
                self.eliminar_vehiculo()
            elif opcion == 4:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def registrar_vehiculo(self):
        tipo = int(input("\nIngrese el tipo de vehículo:\n1 - Moto\n2 - Carro\n3 - Mula\nSeleccion: "))
        while tipo < 1 or tipo > 3:
            print("Error. Introduzca una opción válida.")
            tipo = int(input("Seleccione el tipo de vehículo nuevamente: "))

        tipo_clase = {1: Moto, 2: Carro, 3: Mula}[tipo]

        placa = input("Ingrese la placa del vehículo: ")
        while placa == "":
            print("Error. El campo no puede quedar vacío.")
            placa = input("Ingrese la placa del vehículo: ")

        hora = int(input("Ingrese las horas del vehículo: "))
        while hora < 0:
            print("Error. Ingrese un valor válido para las horas.")
            hora = int(input("Ingrese las horas del vehículo: "))

        minutos = int(input("Ingrese los minutos del vehículo: "))
        while minutos < 0:
            print("Error. Ingrese un valor válido para los minutos.")
            minutos = int(input("Ingrese los minutos del vehículo: "))

        vehiculo = tipo_clase(placa, hora, minutos, self.db)
        vehiculo.calcular_valor_a_pagar()
        print(vehiculo)
        vehiculo.guardar_en_bd()

    def consultar_vehiculo(self):
        placa = input("Ingrese la placa del vehículo a consultar: ")
        vehiculo = Vehiculo(placa, "", 0, 0, self.db)
        if vehiculo.consultar_de_bd():
            print(vehiculo)

    def eliminar_vehiculo(self):
        placa = input("Ingrese la placa del vehículo a eliminar: ")
        vehiculo = Vehiculo(placa, "", 0, 0, self.db)
        vehiculo.eliminar_de_bd()
        print("Vehículo eliminado exitosamente.")

    def menu_principal(self):
        self.gestionar_estacionamiento()

