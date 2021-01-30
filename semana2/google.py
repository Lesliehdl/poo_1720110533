class Google_classroom():

    color = None
    calendario = None    
    grupos = None
    archivos = None
    links = None
    ajustes = None
    unirse_a_clases = None
    notificaciones = None
    configuracion_de_cuenta = None
    comentarios = None

    def __init__(self):
        print("Clase google_classroom")
    
    def entregar(self):
     print("Metodo entregar trabajos")

    def conectarnos(self):
     print("Metodo conectarnos")
        
    def comunicacion(self):
     print("Metodo comunicacion")

    def comentario(self):
     print("Metodo comentarios privados y de clase")

    def fecha(self):
     print("Metodo fecha de entrega")

Persona = Google_classroom()
Persona.color = "verde con amarillo"
Persona.calendario = "cuenta con uno"   
Persona.grupos = "si"
Persona.archivos = "si"
Persona.links = "si de color blanco"
Persona.ajustes = "si"
Persona.unirse_a_clases = "si"
Persona.notificaciones = "si y personalisadas"
Persona.configuracion_de_cuenta = "si"
Persona.comentarios = "si"

print(Persona.color)
print(Persona.calendario)   
print(Persona.grupos)
print(Persona.archivos)
print(Persona.links)
print(Persona.ajustes)
print(Persona.unirse_a_clases)
print(Persona.notificaciones)
print(Persona.configuracion_de_cuenta)
print(Persona.comentarios)

Persona.entregar()
Persona.conectarnos()
Persona.comunicacion()
Persona.comentario()
Persona.fecha()