from  excepciones.ErrorAplicacion import ErrorAplicacion

class ObjetoInexistente(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(error)

class UsuarioInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("El usuario "+str(nombre)+" no existe")

class EstudianteInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("El estudiante "+str(nombre)+" no existe")

class CoordinadorInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("El coordinador "+str(nombre)+" no existe")

class ProfesorInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("El profesor "+str(nombre)+" no existe")

class BecaInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("La beca "+str(nombre)+" no existe")

class GrupoInexistente(ObjetoInexistente):
    def __init__(self, numero=""):
        super().__init__("El grupo "+str(numero)+" no existe")

class MateriaInexistente(ObjetoInexistente):
    def __init__(self, nombre):
        super().__init__("La materia "+str(nombre)+" no existe")

class SalonInexistente(ObjetoInexistente):
    def __init__(self, numero):
        super().__init__("El salon "+str(numero)+" no existe")