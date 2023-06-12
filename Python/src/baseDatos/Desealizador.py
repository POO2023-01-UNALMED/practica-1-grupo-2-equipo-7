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
        Beca.setBecas(cls.deserializar("Becas"))
        Grupo.setGruposTotales(cls.deserializar("Grupos"))
        Horario.setHorariosTotales(cls.deserializar("Horarios"))
        Materia.setMateriasTotales(cls.deserializar("Materias"))
        Salon.setSalones(cls.deserializar("Salones"))
        Coordinador.setCoordinadoresTotales(cls.deserializar("Coordinadores"))
        Estudiante.setEstudiantes(cls.deserializar("Estudiantes"))
        Profesor.setProfesores(cls.deserializar("Profesores"))
        Usuario.setUsuariosTotales(cls.deserializar("Usuarios"))
