from Database import Database
from Registro import Registro
from InicioSesion import InicioSesion
from Vehiculo import Carro, Moto, Mula
from ParkingLot import ParkingLot

def main():
    db = Database(host='localhost', port=3306, user='root', password='', database='ParkingLotDB')
    db.connect()

    registro = Registro(db)
    registro.registrar_usuario()

    inicio_sesion = InicioSesion(db)
    usuario_id = inicio_sesion.iniciar_sesion()
    if usuario_id:
        parking_lot = ParkingLot(db)
        parking_lot.menu_principal()

    db.close()

if __name__ == "__main__":
    main()
