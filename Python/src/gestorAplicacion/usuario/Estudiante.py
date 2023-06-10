from gestorAplicacion.administracion.Grupo import Grupo
from Usuario import Usuario


class Estudiante(Usuario):
    _estudiantes = []

    def __init__(
        self,
        id,
        nombre,
        programa,
        semestre,
        facultad,
        estrato,
        sueldo,
        materias=None,
        gruposVistos=None,
    ):
        super().__init__(id, nombre, facultad)
        super().setTipo("Estudiante")
        self._programa = programa
        self._semestre = semestre
        self._creditos = 0
        self._materias = materias or []  # no se que tan bien este esto
        self._grupos = []
        self._estrato = estrato
        self._sueldo = sueldo
        self._valorMatricula = 1234567 * estrato
        self._matriculaPagada = False
        self._promedio = 0
        self._avance = 0
        self._CREDITOS_PARA_GRADURASE = 120
        self._beca = None
        self._notas = None
        self._gruposVistos = gruposVistos or []
        self._horario = None  # Revisar
        Estudiante._estudiantes.append(self)

    # METODOS

    def mostrarMaterias():
        retorno = ""
        i = 1
        for grupo in Estudiante._grupos:
            retorno += (
                str(i)
                + "- "
                + grupo._materia._nombre
                + " | Grupo "
                + str(grupo._numero)
                + "\n"
            )
            i += 1
        return retorno

    @staticmethod
    def buscarEstudiante(nombre, id):
        # Si el estudiante existe, retorna su indice en la lista 'estudiantes'
        # Si no existe, retorna -1.
        for i in range(len(Estudiante._estudiantes)):
            if (Estudiante._estudiantes[i].nombre == nombre) and (
                Estudiante._estudiantes[i].id == id
            ):
                return i
            else:
                return -1

    def eliminarMateria(self, materia):
        self._materias.remove(materia)
        self._creditos -= materia.creditos

    def eliminarGrupo(self, grupo):
        self._grupos.remove(grupo)
        self.eliminarMateria(grupo.materia)

    def pagarMatricula(self):
        if self._sueldo >= self.valorMatricula:
            self._sueldo -= self.valorMatricula
            self._matriculaPagada = True
            return True
        else:
            self._matriculaPagada = False
            return False

    def calcularPromedio():
        promedio = 0
        for nota in Estudiante._notas:
            promedio += nota
        promedio = promedio / len(Estudiante._notas)
        Estudiante.setPromedio(promedio)

    def calcularAvance():
        creditosVistos = 0

        for pGrupo in Estudiante._gruposVistos:
            creditosVistos += pGrupo.getMateria().getCreditos()

        Estudiante.setAvance(
            (creditosVistos * 100.0) / Estudiante.getCreditosParaGraduarse()
        )

    def agregarNota(self, nota):
        self._notas.append(nota)
        self.calcularPromedio()

    @staticmethod
    def mostrarEstudiantes():
        estudiantes = ""
        i = 1
        for estudiante in Estudiante._estudiantes:
            estudiantes += f"\n{i}. {estudiante.getNombre()}"
            i += 1
        return estudiantes[1:]

    def buscarMateriaPorNombre(self, nombre):
        for materia in self._materias:
            if materia.getNombre() == nombre:
                return materia
        return None

    def buscarMateriaEnInscritas(self, nombre, codigo):
        for materia in self._materias:
            if materia.getNombre() == nombre and materia.getCodigo() == codigo:
                return True
        return False

    def desmatricularMaterias(self):
        # Desmatricula todas las materias de un estudiante
        gruposEliminar = []
        self.setMaterias([])
        for grupoE in self._grupos:
            grupo = Grupo.buscarGrupo(grupoE.getMateria(), grupoE)
            grupo.getMateria().setCupos(grupo.getMateria().getCupos() + 1)
            self.setCreditos(self.getCreditos() - grupo.getMateria().getCreditos())
            gruposEliminar.append(grupo)
        num = len(gruposEliminar)
        for i in range(num):
            gruposEliminar[i].eliminarEstudiante(self)

    # Getters y setters
    def getPrograma(self):
        return self._programa

    def setPrograma(self, programa):
        self._programa = programa

    def getSemestre(self):
        return self._semestre

    def setSemestre(self, semestre):
        self._semestre = semestre

    def getCreditos(self):
        return self._creditos

    def setCreditos(self, creditos):
        self._creditos = creditos

    def getMaterias(self):
        return self._materias

    def setMaterias(self, materias):
        self._materias = materias

    def getGrupos(self):
        return self._grupos

    def setGrupos(self, grupos):
        self._grupos = grupos

    def getHorario(self):
        return self._horario

    def setHorario(self, horario):
        self._horario = horario

    @classmethod
    def getEstudiantes(cls):
        return cls._estudiantes

    @classmethod
    def setEstudiantes(cls, estudiantes):
        cls._estudiantes = estudiantes

    def getEstrato(self):
        return self._estrato

    def setEstrato(self, estrato):
        self._estrato = estrato

    def getSueldo(self):
        return self._sueldo

    def setSueldo(self, sueldo):
        self._sueldo = sueldo

    def getValorMatricula(self):
        return self._valorMatricula

    def isMatriculaPagada(self):
        return self._matriculaPagada

    def getPromedio(self):
        return self._promedio

    def setPromedio(self, promedio):
        self._promedio = promedio

    def getAvance(self):
        return self._avance

    def setAvance(self, avance):
        self._avance = avance

    def getCreditosParaGraduarse(self):
        return self._creditosParaGraduarse

    def getBeca(self):
        return self._beca

    def setBeca(self, beca):
        self._beca = beca

    def getNotas(self):
        return self._notas

    def setNotas(self, notas):
        self._notas = notas


def getGruposVistos(self):
    return self._gruposVistos


def setGruposVistos(self, gruposVistos):
    self._gruposVistos = gruposVistos