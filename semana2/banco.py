class Banco():

    color = None
    tarjeta = None    
    ventanilla = None
    personal = None
    logotipo = None
    sillas = None
    atencion_al_cliente = None
    camaras = None
    muebles = None
    computadoras = None

    def __init__(self):
      print("Clase banco")


    def entregar(self):
        print("Metodo entregar dinero")

    def transacciones(self):
        print("Metodo transacciones")
        
    def resolver(self):
        print("Metodo resolver dudas")

    def tramite(self):
        print("MEtodo tramite para obtener una tarjeta")

    def consulta(self):
        print("Metodo consulta de saldo")


BBVA = Banco()
BBVA.color = "azul"
BBVA.tarjeta = "azul con blanco"   
BBVA.ventanilla = "si"
BBVA.personal = "si"
BBVA.logotipo = "si de color blanco"
BBVA.sillas = "si"
BBVA.atencion_al_cliente = "si"
BBVA.camaras = "si"
BBVA.muebles = "si"
BBVA.computadoras = "si cuentan con varias"

print(BBVA.color)
print(BBVA.tarjeta)   
print(BBVA.ventanilla)
print(BBVA.personal)
print(BBVA.logotipo)
print(BBVA.sillas)
print(BBVA.atencion_al_cliente)
print(BBVA.camaras)
print(BBVA.muebles)
print(BBVA.computadoras)

BBVA.entregar()
BBVA.transacciones()
BBVA.resolver()
BBVA.tramite()
BBVA.consulta()