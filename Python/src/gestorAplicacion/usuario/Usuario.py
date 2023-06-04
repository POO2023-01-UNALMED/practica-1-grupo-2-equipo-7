# Autores:
#   MATEO ÁLVAREZ MURILLO
#   EFRAÍN GÓMEZ RAMÍREZ
#   LIBARDO JOSÉ NAVARRO PEDROZO
#   ANA SOFÍA GÓMEZ ZAPATA
#   SEBASTIÁN OCAMPO GALVIS

import pickle
from abc import ABC, abstractmethod

from Python.src.gestorAplicacion.administracion import Materia


class Usuario(ABC):
    _usuariosTotales = []

    def __init__(self, id, nombre, facultad):
        self._id = id
        self._nombre = nombre
        self._facultad = facultad
        Usuario._usuariosTotales.append(self)

    def __init__(self, id, nombre, pw, facultad):
        self._id = id
        self._nombre = nombre
        self._pw = pw
        self._facultad = facultad
        Usuario._usuariosTotales.append(self)

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    # def mostrarUsuarios(cls) -> str:
    #     retorno = ""
    #     i = 1
    #     for usuario in cls._usuariosTotales:
    #         retorno += (
    #             str(i) + ". " + usuario._nombre + ", id: " + str(usuario._id) + "\n"
    #         )
    #         i += 1
    #     return retorno
    def mostrarUsuarios() -> str:
        retorno = ""
        i = 1
        for usuario in Usuario._usuariosTotales:
            retorno += (
                str(i) + ". " + usuario._nombre + ", id: " + str(usuario._id) + "\n"
            )
            i += 1
        return retorno

    def comprobacionFacultad(self, usuario) -> bool:
        facultad1 = self.getFacultad().lower()
        facultad2 = usuario.getFacultad().lower()
        if facultad1 == facultad2:
            return True
        return False

    def desmatricularDelSistema(usuario) -> None:
        usuarios_totales = Usuario.getUsuariosTotales()
        for u in usuarios_totales:
            if usuario == u:
                usuarios_totales.remove(usuario)
                break

    def eliminar_materia(materia):
        Materia.getMateriasTotales().remove(materia)

    def agregar_materia(
        nombre, codigo, descripcion, creditos, facultad, prerrequisitos
    ):
        nMateria = Materia(
            nombre, codigo, descripcion, creditos, facultad, prerrequisitos
        )
        Materia.getMateriasTotales().append(nMateria)

    # @staticmethod
    # def getTipo(cls):
    #     return cls.tipo
    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getPw(self):
        return self._pw

    def setPw(self, pw):
        self._pw = pw

    def getFacultad(self):
        return self._facultad

    def setFacultad(self, facultad):
        self._facultad = facultad

    @staticmethod
    def getUsuariosTotales():
        return Usuario.usuariosTotales

    @staticmethod
    # def setUsuariosTotales(cls, usuariosTotales):
    #     cls._usuariosTotales = usuariosTotales
    def setUsuariosTotales(usuariosTotales):
        Usuario._usuariosTotales = usuariosTotales
