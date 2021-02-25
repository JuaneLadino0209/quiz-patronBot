class Command:
    def execute(self, recivier):
        pass

class Recivier():
    def mostrar_mensaje(self, mensaje):
        print(mensaje)

class Encender(Command):
    def execute(self, recivier):
        recivier.mostrar_mensaje("El dispositivo Encendio correctamente")

class Apagar(Command):
    def execute(self, recivier):
        recivier.mostrar_mensaje("El dispositivo se apago correctamente")

class Dormir(Command):
    def execute(self, recivier):
        recivier.mostrar_mensaje("El dispositivo se encuentra en modo avion..")

class Hablar(Command):
    def execute(self, recivier):
        recivier.mostrar_mensaje("El dispositivo esta tratando de comunicarse..")