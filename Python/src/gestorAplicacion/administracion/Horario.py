# Autores:
#   EFRAÍN GÓMEZ RAMÍREZ
#   LIBARDO JOSÉ NAVARRO PEDROZO
#   SEBASTIÁN OCAMPO GALVIS
#   MATEO ÁLVAREZ MURILLO

from enum import Enum


class DiaSemana(Enum):
    # Indice y lenght
    LUNES = (0, 5)
    MARTES = (1, 6)
    MIERCOLES = (2, 9)
    JUEVES = (3, 6)
    VIERNES = (4, 7)
    SABADO = (5, 6)
    DOMINGO = (6, 7)

    @classmethod
    def getDiaPorIndice(cls, indice) -> str:
        for dia in cls:
            if dia.value[0] == indice:
                return dia.name
        return None


class Horario:
    _horariosTotales = []

    def __init__(self, diaSemana=0, horaInicio=0, horaFinal=0, grupo=""):
        self._horario = [[None] * 24 for _ in range(7)]
        self._grupoContenidos = []
        if grupo != "":
            self._grupoContenidos.append(grupo)
            for hora in range(horaInicio, horaFinal):
                self._horario[diaSemana][hora] = grupo

    # Por si alguien utiliza los demas constructores que estaban en Java

    # def __init__(self):
    #     Horario._horariosTotales.append(self)
    #     self._horario = [[None] * 24 for _ in range(7)]
    #     self._grupoContenidos = []

    # def __init__(self, horario, grupo):
    #     self._horario = [[None] * 24 for _ in range(7)]
    #     self._grupoContenidos = []
    #     self._grupoContenidos.append(grupo)
    #     for clase in horario:
    #         dia = int(clase[0]) - 1
    #         horaInicio = int(clase[2:4])
    #         horaFinal = int(clase[5:7])
    #         for hora in range(horaInicio, horaFinal):
    #             self._horario[dia][hora] = grupo

    def ocuparHorario(self, grupo, horario=None) -> None:
        if horario == None:
            horario = grupo.getHorario()
        self._grupoContenidos.append(grupo)
        for clase in horario:
            dia = int(clase[0]) - 1
            horaInicio = int(clase[2:4])
            horaFinal = int(clase[5:7])
            for hora in range(horaInicio, horaFinal):
                self._horario[dia][hora] = grupo

    def liberarHorario(self, horario) -> None:
        for clase in horario:
            dia = int(clase[0]) - 1
            horaInicio = int(clase[2:4])
            horaFinal = int(clase[5:7])
            for hora in range(horaInicio, horaFinal):
                grupoEliminado = self._horario[dia][hora]
                self._horario[dia][hora] = None
      
            for pGrupo in self._grupoContenidos:
                if not isinstance(pGrupo,str):
                    if pGrupo.getNumero() == grupoEliminado.getNumero():
                        if pGrupo.getMateria().getNombre()==grupoEliminado.getMateria().getNombre():
                            self._grupoContenidos.remove(pGrupo)    

    def vaciarHorario(self, grupos) -> None:
        for grupo in grupos:
            self.liberarHorario(grupo.getHorario())

    def comprobarDisponibilidadUna(self, clase) -> bool:
        # print("esto es: "+str(clase))
        # clase = clase[0]
        dia = int(clase[0])-1
        horaInicio = int(clase[2:4])
        horaFinal = int(clase[5:7])
        for hora in range(horaInicio, horaFinal):
            if self._horario[dia][hora] is not None:
                return False
        return True

    def comprobarDisponibilidad(self, clases) -> bool:
        for clase in clases:
            if not self.comprobarDisponibilidadUna(clase):
                return False
        return True

    def mostrarHorario(self) -> str:
        horario = "HORA        LUNES        MARTES        MIERCOLES        JUEVES        VIERNES        SABADO        DOMINGO\n"

        for i in range(24):
            if i < 9:
                horaConCeroDelante = "0" + str(i)
                horaSiguienteConCeroDelante = "0" + str(i + 1)
                horario += (
                    horaConCeroDelante + "-" + horaSiguienteConCeroDelante + "       "
                )
            elif i == 9:
                horario += "09-10" + "       "
            else:
                horario += str(i) + "-" + str(i + 1) + "       "

            for j in range(7):
                materia = ""
                if self._horario[j][i] is not None:
                    materia = self._horario[j][i].getMateria().getAbreviatura()
                cantidad_espacios = (len(DiaSemana.getDiaPorIndice(j)) + 8) - len(
                    materia
                )
                espacios = " " * cantidad_espacios
                horario += materia + espacios
            horario += "\n"
        return horario
    
    def mostrarHorario2(self) -> str:
        # Si el dos, y este si es bueno, porque tiene mano de efrain >:O 
        horario = "HORA        LUNES        MARTES        MIERCOLES        JUEVES        VIERNES        SABADO        DOMINGO\n"

        for i in range(6,24):
            if i < 9:
                horaConCeroDelante = "0" + str(i)
                horaSiguienteConCeroDelante = "0" + str(i + 1)
                horario += (
                    horaConCeroDelante + "-" + horaSiguienteConCeroDelante + "       "
                )
            elif i == 9:
                horario += "09-10" + "       "
            else:
                horario += str(i) + "-" + str(i + 1) + "       "

            for j in range(7):
                materia = ""
                if self._horario[j][i] is not None:
                    materia = self._horario[j][i].getMateria().getAbreviatura()
                if j != 6:
                    cantidad_espacios = (len(DiaSemana.getDiaPorIndice(j)) + 8) - len(materia)
                else:
                    cantidad_espacios = len(materia)
                espacios = " " * cantidad_espacios
                horario += materia + espacios
            horario += "\n"
        return horario

    def getGrupoContenidos(self):
        return self._grupoContenidos

    def setGrupoContenidos(self, grupoContenidos):
        self._grupoContenidos = grupoContenidos

    @classmethod
    def getHorariosTotales(cls):
        return cls._horariosTotales

    @classmethod
    def setHorariosTotales(cls, horarios):
        cls._horariosTotales = horarios
