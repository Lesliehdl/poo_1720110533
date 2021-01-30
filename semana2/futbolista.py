class Futbolista():

    balon = None
    playera = None    
    espinilleras = None
    tacos = None
    pantalones_cortos = None
    calcetas_cortas = None
    mochila = None
    equipo = None
    bomba_de_aire = None
    cancha = None

    def __init__(self):
        print("Clase futbolista")

    def juego(self):
     print("Metodo juego")

    def entrenamiento(self):
     print("Metodo entrenamiento")
        
    def anotaciones(self):
     print("Metodo anotaciones de goles")

    def jurados(self):
     print("Metodo jurados")

    def competencias(self):
     print("Metodo competencias")

Persona = Futbolista()
Persona.balon = "negro con blanco"
Persona.playera = "si"   
Persona.espinilleras = "si"
Persona.tacos = "si"
Persona.pantalones_cortos = "si"
Persona.calcetas_cortas = "si"
Persona.mochila = "si deacuerdo ala persona"
Persona.equipo = "si"
Persona.bomba_de_aire = "si"
Persona.cancha = "obligatoria"

print(Persona.balon)
print(Persona.playera)   
print(Persona.espinilleras)
print(Persona.tacos)
print(Persona.pantalones_cortos)
print(Persona.calcetas_cortas)
print(Persona.mochila)
print(Persona.equipo)
print(Persona.bomba_de_aire)
print(Persona.cancha)

Persona.juego()
Persona.entrenamiento()
Persona.anotaciones()
Persona.jurados()
Persona.competencias()