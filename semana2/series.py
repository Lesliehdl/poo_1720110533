class Serie_de_tv():

    acotores = None
    capitulos = None    
    localidad = None
    dialogo = None
    vestuarios = None
    escenarios = None
    audiociones = None
    maquillaje = None
    camaras = None
    luces = None

    def __init__(self):
        print("Clase serie de tv")


    def relato(self):
     print("Metodo relato de una historia")

    def conocimiento(self):
     print("Metodo conocimiento de los personajes")
        
    def reflexion(self):
     print("Metodo reflexion para el publico")

    def divertir(self):
     print("Metodo divertir y entretener")

    def emociones(self):
     print("Metodo crear emociones hacia la historias o personajes")

Serie = Serie_de_tv()
Serie.actores = "si"
Serie.capitulos = "depende del director"   
Serie.localidad = "deacuerodo alas escenas "
Serie.dialogo = "si"
Serie.vestuarios = "si"
Serie.escenarios = "si"
Serie.audiociones = "si"
Serie.maquillaje = "si"
Serie.camaras = "si"
Serie.luces = "deacuerodo a la localidad"

print(Serie.actores)
print(Serie.capitulos)   
print(Serie.localidad)
print(Serie.dialogo)
print(Serie.vestuarios)
print(Serie.escenarios)
print(Serie.audiociones)
print(Serie.maquillaje)
print(Serie.camaras)
print(Serie.luces)

Serie.relato()
Serie.conocimiento()
Serie.reflexion()
Serie.divertir()
Serie.emociones()