class Coche():

    motor = None
    marca = None    
    velocidad = None
    kilimetraje = None
    año = None
    modelo = None
    color = None
    transmision = None
    quemacocos = None
    tamaño = None

    def __init__(self):
        print("Clase coche")


    def encender(self):
     print("Metodo encender")

    def acelerar(self):
     print("Metodo acelerar")
        
    def estacionarse(self):
     print("Metodo estacionarse")

    def transportar(self):
     print("Metodo transportar")

    def frenar(self):
     print("Metodo frenar")
    
Camioneta = Coche ()
Camioneta.motor = "Motor V6"
Camioneta.marca = "chevrolet"   
Camioneta.velocidad = "si"
Camioneta.kilimetraje = "si"
Camioneta.año = "2019"
Camioneta.modelo = "Chevrolet Blazer"
Camioneta.color = "negro"
Camioneta.transmision = "automática de 9 velocidades"
Camioneta.quemacocos = "no"
Camioneta.tamaño = "67.0 in de largo, 191.4in de ancho"

print(Camioneta.motor)
print(Camioneta.marca)   
print(Camioneta.velocidad)
print(Camioneta.kilimetraje)
print(Camioneta.año)
print(Camioneta.modelo)
print(Camioneta.color)
print(Camioneta.transmision)
print(Camioneta.quemacocos)
print(Camioneta.tamaño)

Camioneta.encender()
Camioneta.acelerar()
Camioneta.estacionarse()
Camioneta.transportar()
Camioneta.frenar()
