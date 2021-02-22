class Persona():

    # Variables miembro de la clase
    materia = None
    numero_alumnos = None
    nombre_alumno = None
    numero_clases = None
    numero_faltas = None
    retardos = None
    porcentaje_asistencia = None
    resultado = None

    def __init__(self):
        pass

    def imprimirDatos(self):
       
        print("Materia", self.materia)
        print("Numero de alumnos", self.numero)
        print("Nombre del alumno {}".format(self.nombre))
        print("Numero de clases", self.clases)
        print("Numero de faltas", self.faltas)
        print("Retardos", self.retardos)
        print("Porcentaje de asistencia", self.asistencia)
        print("Resultado", self.resultado)


    def bucleWhile(self):
        repetir = "s"
        while repetir == "s":
            print("Otra evaluacion",self.nombre)
            repetir = input("Otra evaluacion (s/n) ")

    def bucleFor(self):
        for i in range(2):
            print("Nombre alumno {}".format(self.nombre))

    
dejah = Persona()
jhon = Persona()

dejah.materia = "programación orientada a objetos"
jhon.materia ="Base de datos"

dejah.nombre = "dejah"
jhon.nombre = "jhon"

dejah.numero = "2"
jhon.numero = "2"

dejah.clases = "10"
jhon.clases = "10"

dejah.faltas = "2"
jhon.faltas = "2"

dejah.retardos = "2"
jhon.retardos = "3"

dejah.asistencia = "80"
jhon.asistencia = "70"

dejah.resultado = "no tiene derecho"
jhon.resultado = "no tiene derecho"

dejah.imprimirDatos()
jhon.imprimirDatos()




dejah.bucleWhile()
jhon.bucleWhile()


