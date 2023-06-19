# Autores:
# EFRAÍN GÓMEZ RAMÍREZ
# LIBARDO JOSÉ NAVARRO PEDROZO
# ANA SOFÍA GÓMEZ ZAPATA
# SEBASTIÁN OCAMPO GALVIS
from gestorAplicacion.administracion.Horario import Horario
import random


class Profesor:
    _profesores = []

    def __init__(self, nombre, facultad, materiasDadas, horario=Horario(), grupos=[]):
        self._nombre = nombre
        self._facultad = facultad
        self._materiasDadas = materiasDadas
        self._horario = horario
        self._grupos = grupos if grupos is not None else []
        Profesor._profesores.append(self)

    def vincularGrupo(self, g):
        self._grupos.append(g)
        self._horario.ocuparHorario(g, g.getHorario())

    def desvincularGrupo(self, g):
        if g in self._grupos:
            indice = self._grupos.index(g)
            horaLibre = self._grupos[indice].getHorario()
            self._horario.liberarHorario(horaLibre)
            self._grupos.remove(g)

    def daMateria(self, nombre):
        for materia in self.getMateriasDadas():
            if materia.getNombre() == nombre:
                return True
        return False

    @classmethod
    def recomendarEstudiante(cls, estudiante):
        for profesor in cls._profesores:
            chance = 0
            suerte = random.randint(1, 10)
            for grupo in estudiante.getGruposVistos():
                if grupo.getProfesor().getNombre() == profesor.getNombre():
                    chance += 5
                    break
            if estudiante.getFacultad() == profesor.getFacultad():
                chance += 3
            if chance >= suerte:
                return True
        return False

    @classmethod
    def mostrarProfesores(cls):
        r = ""
        i = 1
        for profesor in cls._profesores:
            r += f"{i}. {profesor.getNombre()}. Materias: "
            for materia in profesor.getMateriasDadas():
                if (
                    profesor.getMateriasDadas().index(materia)
                    == len(profesor.getMateriasDadas()) - 1
                ):
                    r += f"{materia.getNombre()}.\n"
                else:
                    r += f"{materia.getNombre()}, "
            i += 1
        return r

    @classmethod
    def profesoresDeMateria(cls, nombre):
        profes = []
        for profesor in cls._profesores:
            if profesor.daMateria(nombre) and profesor not in profes:
                profes.append(profesor)
        return profes
    
    @classmethod
    def nombresProfesDeMateria(cls, materia):
        profes = []
        for profesor in cls._profesores:
            if profesor.daMateria(materia) and profesor not in profes:
                profes.append(profesor.getNombre())
        return profes

    @classmethod
    def encontrarProfe(cls, profesor):
        for profe in Profesor._profesores:
            if profe.getNombre()== profesor:
                return profe

    @classmethod
    def mostrarProfesMateria(cls, nombre):
        r = ""
        i = 1
        profes = cls._profesoresDeMateria(nombre)
        for profesor in profes:
            r += f"{i}. {profesor.getNombre()}.\n"
            i += 1
        return r

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getFacultad(self):
        return self._facultad

    def setFacultad(self, facultad):
        self._facultad = facultad

    def getMateriasDadas(self):
        return self._materiasDadas

    def setMateriasDadas(self, materiasDadas):
        self._materiasDadas = materiasDadas

    def getGrupos(self):
        return self._grupos

    def setGrupos(self, grupos):
        self._grupos = grupos

    def setHorario(self, horario):
        self._horario = horario

    def getHorario(self):
        return self._horario

    @classmethod
    def getProfesores(cls):
        return cls._profesores

    @classmethod
    def setProfesores(cls, profesores):
        cls._profesores = profesores
