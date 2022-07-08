import pickle

def main():
    archivoEscritura = open('obj.pckl', 'wb')
    miVehiculo = Vehiculo(color = 'azul', puertas = 2, motor = 'V8')
    pickle.dump(miVehiculo, archivoEscritura)
    archivoEscritura.close()
    del(miVehiculo)
    try:
        miVehiculo.getMotor()
    except Exception:
        print('El objeto ya no existe!')
        print('----------------------------------')

    archivoLectura = open('obj.pckl', 'rb')
    vehiculoRecuperado = pickle.load(archivoLectura)
    print('Cargado desde el archivo obj.pckl')
    print('----------------------------------')
    print(f'Color: {vehiculoRecuperado.getColor()}')
    print(f'Nro. de Puertas: {vehiculoRecuperado.getPuertas()}')
    print(f'Motor: {vehiculoRecuperado.getMotor()}')


class Vehiculo:
    def __init__(self, color = 'blanco', puertas = 4, motor = 'V6'):
        self.color = color
        self.puertas = puertas
        self.motor = motor
    
    def getColor(self):
        return self.color
    def getPuertas(self):
        return self.puertas
    def getMotor(self):
        return self.motor


if __name__ == '__main__':
    main()