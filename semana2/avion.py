class Avion():

    color = None
    ventanas = None
    alas = None 
    tanque_de_gasolina = None
    motor = None
    bodega_de_equipaje = None
    cabina_de_mando = None
    aleron_de_equilibrio = None
    turborreactor = None
    luz_de_navegacion = None

    def __init__(self):
        print("Clase avion")


    def transportar(self):
        print("Metodo transportar")

    def vuela(self):
        print("Metodo vuela")

    def enciende(self):
        print("Metodo enciende luces")

    def gira(self):
        print("Metodo gira")

    def estacionarse(self):
        print("Metodo estacionarse")


Volar = Avion()
Volar.color = "Blanco"
Volar.ventanas = "si"
Volar.alas = "si"
Volar.tanque_de_gasolina = "si"
Volar.motor = "Funcionando"
Volar.bodega_de_equipaje = "si pero con limite"
Volar.cabina_de_mando = "si"
Volar.aleron_de_equilibrio = "si"
Volar.turborreactor = "Funcionando"
Volar.luz_de_navegacion = "Funcionando"

print(Volar.color)
print(Volar.ventanas)   
print(Volar.alas)
print(Volar.tanque_de_gasolina)
print(Volar.motor)
print(Volar.bodega_de_equipaje)
print(Volar.cabina_de_mando)
print(Volar.aleron_de_equilibrio)
print(Volar.turborreactor)
print(Volar.luz_de_navegacion)

Volar.transportar()
Volar.vuela()
Volar.enciende()
Volar.gira()
Volar.estacionarse()