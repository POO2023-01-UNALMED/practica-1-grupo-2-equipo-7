# Autores:
#   EFRAÍN GÓMEZ RAMÍREZ
#   LIBARDO JOSÉ NAVARRO PEDROZO
#   SEBASTIÁN OCAMPO GALVIS
#   MATEO ÁLVAREZ MURILLO

import pickle
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

    @staticmethod
    def getDiaPorIndice(indice) -> str:
        for dia in DiaSemana:
            if dia.value[0] == indice:
                return dia.name
        return None


class Horario:
    _horariosTotales = []

    def __init__(self):
        Horario._horariosTotales.append(self)
        self._horario = [[None] * 24 for _ in range(7)]
        self._grupoContenidos = []

    def __init__(self, diaSemana, horaInicio, horaFinal, grupo):
        self._horario = [[None] * 24 for _ in range(7)]
        self._grupoContenidos = []
        self._grupoContenidos.append(grupo)
        for hora in range(horaInicio, horaFinal):
            self._horario[diaSemana][hora] = grupo

    def __init__(self, horario, grupo):
        self._horario = [[None] * 24 for _ in range(7)]
        self._grupoContenidos = []
        self._grupoContenidos.append(grupo)
        for clase in horario:
            dia = int(clase[0]) - 1
            horaInicio = int(clase[2:4])
            horaFinal = int(clase[5:7])
            for hora in range(horaInicio, horaFinal):
                self._horario[dia][hora] = grupo

    def ocuparHorario(self, horario, grupo) -> None:
        self._grupoContenidos.append(grupo)
        for clase in horario:
            dia = int(clase[0]) - 1
            horaInicio = int(clase[2:4])
            horaFinal = int(clase[5:7])
            for hora in range(horaInicio, horaFinal):
                self._horario[dia][hora] = grupo

    def ocuparHorario(self, grupo) -> None:
        self._grupoContenidos.append(grupo)
        horario = grupo.getHorario()
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
            self._grupoContenidos.remove(grupoEliminado)

    def vaciarHorario(self, grupos) -> None:
        for grupo in grupos:
            self.liberarHorario(grupo.getHorario())

    def comprobarDisponibilidad(self, clase) -> bool:
        dia = int(clase[0]) - 1
        horaInicio = int(clase[2:4])
        horaFinal = int(clase[5:7])
        for hora in range(horaInicio, horaFinal):
            if self._horario[dia][hora] is not None:
                return False
        return True

    def comprobarDisponibilidad(self, clases) -> bool:
        ok = True
        for i in clases:
            if not self.comprobarDisponibilidad(i):
                ok = False
        return ok

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
                cantidad_espacios = (DiaSemana.getDiaPorIndice(j).length + 8) - len(
                    materia
                )
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
