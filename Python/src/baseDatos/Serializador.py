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


class Serializador:
    def serializar(nombre, lista):
        ruta = os.path.join(
            pathlib.Path(__file__).parent.absolute(), "temp/" + nombre + ".txt"
        )
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(lista, picklefile)
            picklefile.close()
        except:
            print("Ocurrió un error")

    @classmethod
    def serializarDatos(cls):
        cls.serializar("Beca", Beca.getBecas())
        cls.serializar("Grupo", Grupo.getGruposTotales())
        cls.serializar("Horario", Horario.getHorariosTotales())
        cls.serializar("Materia", Materia.getMateriasTotales())
        cls.serializar("Salon", Salon.getSalones())
        cls.serializar("Coordinador", Coordinador.getCoordinadoresTotales())
        cls.serializar("Estudiante", Estudiante.getEstudiantes())
        cls.serializar("Profesor", Profesor.getProfesores())
        cls.serializar("Usuario", Usuario.getUsuariosTotales())
