class Estudiante():

   libretas = None
   lapices_colores = None
   libros = None
   participacion = None
   palabras_u_opinion = None
   aprender = None
   presentarse_a_clases = None
   festivales = None
   talleres = None
   conocimiento = None

   def __init__(self):
        print("Clase estudiante")

   def estudiar(self):
        print("Metodo estudiar")

   def asistir(self):
        print("Metodo asistir al instituto")

   def realizar(self):
        print("Metodos realizar tareas y actividades")

   def respetar(self):
        print("Metodo respetar a los profesores")

   def participar(self):
        print("Metodo participar")


alumno = Estudiante()
alumno.libretas = "cualquiera de su agrado"
alumno.lapices_colores = "los del agrado del estudiante"
alumno.libros = "asignados por los maestros"
alumno.participacion = "si"
alumno.palabra_u_opinion = "si"
alumno.aprender = "si"
alumno.presentarse_a_clases = "si"
alumno.festivales = "si"
alumno.talleres = "si"
alumno.conocimiento = "si"

print(alumno.libretas)
print(alumno.lapices_colores)
print(alumno.libros)
print(alumno.participacion)
print(alumno.palabra_u_opinion)
print(alumno.aprender)
print(alumno.presentarse_a_clases)
print(alumno.festivales)
print(alumno.talleres)
print(alumno.conocimiento)

alumno.estudiar()
alumno.asistir()
alumno.realizar()
alumno.respetar()
alumno.participar()