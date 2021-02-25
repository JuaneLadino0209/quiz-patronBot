from command import *

class EjemploCommand:
    def obtener_nombre(self):
        return "Command"

    def operacion(command):
        r = Recivier()
        command.execute(r)

bot = EjemploCommand
command = Hablar()
bot.operacion(command)

