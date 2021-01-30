class Cajero_automatico():

    color = None
    luces = None    
    pantalla = None
    entrada_de_tarjeta = None
    salida_de_dinero = None
    botones = None
    salida_para_tickets = None
    salida_para_monedas = None
    abertura_para_meter_dinero = None
    camaras = None

    def __init__(self):
        print("Clase cajero automatico")

    def dinero(self):
     print("Metodo entrega de dinero")

    def limite(self):
     print("Metodo limite de retiro de dinero")
        
    def codigo(self):
     print("Metodo pin")

    def prender(self):
     print("Metodo prender")

    def entrega(self):
     print("Metodo entrega de ticket")

Persona = Cajero_automatico()
Persona.color = "gris con azul"
Persona.luces= "si"   
Persona.pantalla = "si"
Persona.entrada_de_tarjeta = "si"
Persona.salida_de_dinero = "si "
Persona.botones = "si"
Persona.salida_para_tickets  = "si"
Persona.salida_para_monedas = "si"
Persona.abertura_para_meter_dinero = "si"
Persona.camaras = "si "

print(Persona.color)
print(Persona.luces)   
print(Persona.pantalla)
print(Persona.entrada_de_tarjeta)
print(Persona.salida_de_dinero)
print(Persona.botones)
print(Persona.salida_para_tickets)
print(Persona.salida_para_monedas)
print(Persona.abertura_para_meter_dinero)
print(Persona.camaras)

Persona.dinero()
Persona.limite()
Persona.codigo()
Persona.prender()
Persona.entrega()