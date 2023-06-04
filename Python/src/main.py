from gestorAplicacion.administracion.Beca import Beca
from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.administracion.Salon import Salon
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Profesor import Profesor
from gestorAplicacion.usuario.Usuario import Usuario
import pickle

if __name__ == "__main__":
    opcion = int(input("Que desea hacer?\n1- Serializar\n2-Desealizar"))
    if opcion == 1:
        objetos = {
            "Beca": Beca.getBecas(),
            "Grupo": Grupo.getGruposTotales(),
            "Horario": Horario.getHorariosTotales(),
            "Materia": Materia.getMateriasTotales(),
            "Salon": Salon.getSalones(),
            "Coordinador": Coordinador.getCoordinadoresTotales(),
            "Estudiante": Estudiante.getEstudiantes(),
            "Profesor": Profesor.getProfesores(),
            "Usuario": Usuario.getUsuariosTotales(),
        }
        pickefile = open("Python\src\baseDatos\objetos.pkl", "wb")
        pickle.dump(objetos, pickefile)
        pickefile.close()
    elif opcion == 2:
        pickefile = open("Python\src\baseDatos\objetos.pkl", "rb")
        objetos = pickle.load(pickefile)
        pickefile.close()
        Beca.setBecas(objetos["Beca"])
        Grupo.setGruposTotales(objetos["Grupo"])
        Horario.setHorariosTotales(objetos["Horario"])
        Materia.setMateriasTotales(objetos["Materia"])
        Salon.setSalones(objetos["Salon"])
        Coordinador.setCoordinadoresTotales(objetos["Coordinador"])
        Estudiante.setEstudiantes(objetos["Estudiante"])
        Profesor.setProfesores(objetos["Profesor"])
        Usuario.setUsuariosTotales(objetos["Usuario"])
    else:
        print("Muy pendejo")
