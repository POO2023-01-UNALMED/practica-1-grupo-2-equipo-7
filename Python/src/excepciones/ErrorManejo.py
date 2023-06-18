from excepciones.ErrorAplicacion import ErrorAplicacion

class ErrorManejo(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(error)

class CamposVacios(ErrorManejo):
    def __init__(self):
        super().__init__("Los campos del formulario no fueron llenados")

class CamposInvalidos(ErrorManejo):
    def __init__(self):
        super().__init__("Los campos del formulario fueron llenados incorrectamente")

class CampoNumero(ErrorManejo):
    def __init__(self):
        super().__init__("Se debe ingresar un número")

class MateriaMatriculada(ErrorManejo):
    def __init__(self, nombre):
        super().__init__("El estudiante ya tiene la materia "+nombre+" matriculada")

class MateriaCursada(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__("El estudiante ya curso la materia "+nombre)

class EstudianteSinCreditos(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__("El estudiante "+nombre+" no tiene creditos suficientes")


class EstudianteSinMatriculaPagada(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__("El estudiante "+nombre+" no tiene la matricula pagada")


class PrerrequisitosMateria(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__("El estudiante "+nombre+" no cumple con los prerrequisitos")


class MateriaSinCupos(ErrorManejo):
    def __init__(self, nombre=""):
        super().__init__("La materia "+nombre+" no cuenta con cupos suficientes")



