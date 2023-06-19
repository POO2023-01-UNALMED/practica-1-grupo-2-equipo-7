# Autores:
#   MATEO ÁLVAREZ MURILLO
#   EFRAÍN GÓMEZ RAMÍREZ
#   LIBARDO JOSÉ NAVARRO PEDROZO
#   ANA SOFÍA GÓMEZ ZAPATA
#   SEBASTIÁN OCAMPO GALVIS

from abc import ABC, abstractmethod
from gestorAplicacion.administracion.Materia import Materia


class Usuario(ABC):
    _usuariosTotales = []

    def __init__(self, id, nombre, facultad, pw="0000"):
        self._id = id
        self._nombre = nombre
        self._pw = str(pw)
        self._facultad = facultad
        Usuario._usuariosTotales.append(self)


    @abstractmethod
    def __str__(self):
        pass

    # Por si alguien utiliza el otro constructor que estaban en Java

    # def __init__(self, id, nombre, facultad):
    #     self._id = id
    #     self._nombre = nombre
    #     self._facultad = facultad
    #     Usuario._usuariosTotales.append(self)
    @classmethod
    def mostrarUsuarios(cls) -> str:
        retorno = ""
        i = 1
        for usuario in cls.getUsuariosTotales():
            retorno += (
                str(i) + ". " + usuario._nombre + ", id: " + str(usuario._id) + "\n"
            )
            i += 1
        return retorno

    def comprobacionFacultad(self, usuario) -> bool:
        facultad1 = self.getFacultad().lower()
        facultad2 = usuario.getFacultad().lower()
        return facultad1 == facultad2

    def desmatricularDelSistema(usuario) -> None:
        usuariosTotales = Usuario.getUsuariosTotales()
        for user in usuariosTotales:
            if usuario == user:
                usuariosTotales.remove(usuario)
                break

    def eliminar_materia(materia) -> None:
        Materia.getMateriasTotales().remove(materia)

    def agregar_materia(
        nombre, codigo, descripcion, creditos, facultad, prerrequisitos
    ) -> None:
        nuevaMateria = Materia(
            nombre, codigo, descripcion, creditos, facultad, prerrequisitos
        )
        Materia.getMateriasTotales().append(nuevaMateria)

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

    @classmethod
    def getUsuariosTotales(cls):
        return cls._usuariosTotales

    @classmethod
    def setUsuariosTotales(cls, usuariosTotales):
        cls._usuariosTotales = usuariosTotales
