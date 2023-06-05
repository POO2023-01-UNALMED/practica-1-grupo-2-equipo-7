from gestorAplicacion.administracion.Beca import Beca
from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Horario import DiaSemana
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.administracion.Salon import Salon
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Profesor import Profesor
from gestorAplicacion.usuario.Usuario import Usuario
import pickle
import pathlib
import os


class Deserializador:
    def deserializar(nombre):
        lista = []
        ruta = os.path.join(
            pathlib.Path(__file__).parent.absolute(), "temp/" + nombre + ".txt"
        )
        try:
            picklefile = open(ruta, "rb")
        except:
            picklefile = open(ruta, "x")
            picklefile = open(ruta, "rb")
        if os.path.getsize(ruta) > 0:
            lista = pickle.load(picklefile)
        picklefile.close()
        return lista

    @classmethod
    def deserializarDatos(cls):
        Beca.setBecas(cls.deserializar("Beca"))
        Grupo.setGruposTotales(cls.deserializar("Grupo"))
        Horario.setHorariosTotales(cls.deserializar("Horario"))
        Materia.setMateriasTotales(cls.deserializar("Materia"))
        Salon.setSalones(cls.deserializar("Salon"))
        Coordinador.setCoordinadoresTotales(cls.deserializar("Coordinador"))
        Estudiante.setEstudiantes(cls.deserializar("Estudiante"))
        Profesor.setProfesores(cls.deserializar("Profesor"))
        Usuario.setUsuariosTotales(cls.deserializar("Usuario"))
