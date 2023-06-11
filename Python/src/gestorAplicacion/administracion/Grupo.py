# Autores:
#  MATEO ÁLVAREZ MURILLO
#  EFRAÍN GÓMEZ RAMÍREZ
#  LIBARDO JOSÉ NAVARRO PEDROZO
#  SEBASTIÁN OCAMPO GALVIS
# from gestorAplicacion.usuario.Estudiante import Estudiante
# from Salon import Salon


class Grupo:
    _gruposTotales = []

    def __init__(self, materia, numero, profesor, horario=[], cupos=None, salon=None):
        self._materia = materia
        self._numero = numero
        self._profesor = profesor
        self._horario = horario if horario is not None else []
        self._cupos = cupos
        self._salon = salon
        self._estudiantes = []
        Grupo._gruposTotales.append(self)

    def mostrarInformacionGrupo(self):
        return "Número del grupo: {}, Profesor: {}, Horario: {}, Cupos: {}, Salón: {}".format(
            self.numero, self.profesor, self.horario, self.cupos, self.salon
        )

    def existenciaEstudiante(self, estudiante):
        for e in self._estudiantes:
            if e.getId() == estudiante.getId():
                return True
        return False

    def eliminarEstudiante(self, estudiante):
        indice = -1
        for i, e in enumerate(self._estudiantes):
            if e.getNombre() == estudiante.getNombre():
                indice = i
                self._cupos += 1
                estudiante.eliminarGrupo(self)
                break
        if indice != -1:
            self._estudiantes.pop(indice)

    @staticmethod
    def buscarGrupo(materiaE, grupoE):
        from gestorAplicacion.administracion.Materia import Materia
        
        indicei = -1
        indicej = -1
        for i in range(len(Materia.getMateriasTotales())):
            materia = Materia.getMateriasTotales()[i]
            if materia.getNombre() == materiaE.getNombre():
                indicei = i
                for j in range(len(materia.getGrupos())):
                    grupo = materia.getGrupos()[j]
                    if grupo.getNumero() == grupoE.getNumero():
                        indicej = j
                        break

        return Materia.getMateriasTotales()[indicei].getGrupos()[indicej]

    def agregarEstudiante(self, estudiante):
        self._estudiantes.append(estudiante)
        self._cupos -= 1

    def getNumero(self):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getProfesor(self):
        return self._profesor

    def setProfesor(self, profesor):
        self._profesor = profesor

    def getHorario(self):
        return self._horario

    def setHorario(self, horario):
        self._horario = horario

    def getCupos(self):
        return self._cupos

    def setCupos(self, cupos):
        self._cupos = cupos

    def getSalon(self):
        return self._salon

    def setSalon(self, salon):
        self._salon = salon

    def getEstudiantes(self):
        return self._estudiantes

    def setEstudiantes(self, estudiantes):
        self._estudiantes = estudiantes

    def getMateria(self):
        return self._materia

    def setMateria(self, materia):
        self._materia = materia

    @classmethod
    def getGruposTotales(cls):
        return cls._gruposTotales

    @classmethod
    def setGruposTotales(cls, grupos):
        cls._gruposTotales = grupos
