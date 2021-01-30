class Vacaciones():

    lugar = None
    horarios = None    
    fechas = None
    ropa = None
    maletas = None
    personas = None
    costos = None
    hotel = None
    dinero = None
    objetos_importantes = None

    def __init__(self):
        print("Clase coche")


    def conocimiento(self):
        print("Metodo conocimiento")

    def relajacion(self):
        print("Metodo relajacion")
        
    def descansar(self):
        print("Metodo descansar")

    def comer(self):
        print("Metodo comer")

    def diversion(self):
        print("Metodo diversion")

Persona = Vacaciones ()
Persona.lugar = "seleccion de la persona"
Persona.horario = "asignados por que viajara"   
Persona.fechas = "deaceurdo a sus vacaciones"
Persona.ropa = "si"
Persona.maletas = "si"
Persona.personas = "si"
Persona.costos = "deaceurdo al que viaja"
Persona.hotel = "si"
Persona.dinero = "si"
Persona.objetos_importantes = "si"

print(Persona.lugar)
print(Persona.horario)   
print(Persona.fechas)
print(Persona.ropa)
print(Persona.maletas)
print(Persona.personas)
print(Persona.costos)
print(Persona.hotel)
print(Persona.dinero)
print(Persona.objetos_importantes)

Persona.conocimiento()
Persona.relajacion()
Persona.descansar()
Persona.comer()
Persona.diversion()