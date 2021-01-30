class Calculadora():

    pilas = None
    marca = None    
    color = None
    tamaño = None
    pantalla = None
    teclado = None
    apartado_de_operaciones_especificas = None
    boton_de_encendido_y_apagado = None
    boton_para_borrar = None
    tapa = None

    def __init__(self):
        print("Clase calculadora")

    def enciende(self):
     print("Metodo enciende")

    def realiza(self):
     print("Metodo realiza operaciones")
        
    def resultados(self):
     print("Metodo muestra resultados correctos")

    def cientifica(self):
     print("Metodo la calculadora cintifica incluye otras operaciones")

    def operaciones(self):
     print("Metodo operaciones largas")

Numero = Calculadora()
Numero.pilas = "si"
Numero.marca = "casio"   
Numero.color = "negro"
Numero.tamaño = "87 x 58 x 12 mm."
Numero.pantalla = "si"
Numero.teclado = "si"
Numero.apartado_de_operaciones_especificas = "si"
Numero.boton_de_encendido_y_apagado = "si"
Numero.boton_para_borrar = "si"
Numero.tapa = "si "

print(Numero.pilas)
print(Numero.marca)   
print(Numero.color)
print(Numero.tamaño)
print(Numero.pantalla)
print(Numero.teclado)
print(Numero.apartado_de_operaciones_especificas)
print(Numero.boton_de_encendido_y_apagado)
print(Numero.boton_para_borrar)
print(Numero.tapa)

Numero.enciende()
Numero.realiza()
Numero.resultados()
Numero.cientifica()
Numero.operaciones()