class Banco():

    color = None
    tarjeta = None    
    ventanilla = None


    def __init__(self):
      print("Clase banco")

    ""
    Metodos
    ""
    def entregar(self):
        print("Metodo entregar dinero")

    def transacciones(self):
        print("Metodo transacciones")


BBVA = Banco()
BBVA.color = "azul"
BBVA.tarjeta = "azul con blanco"   
BBVA.ventanilla = "si"

print(BBVA.color)
print(BBVA.tarjeta)   
print(BBVA.ventanilla)

BBVA.entregar()
BBVA.transacciones()