from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Profesor import Profesor
from gestorAplicacion.usuario.Usuario import Usuario
from gestorAplicacion.administracion.Beca import Beca
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *

class Coordinador(Usuario):
    _usuarioIngresado = None
    _LIMITES_CREDITOS = 20
    _coordinadoresTotales = []
    _facultades = [
        "Facultad de arquitectura",
        "Facultad de ciencias",
        "Facultad de ciencias agrarias",
        "Facultad de ciencias humanas y economicas",
        "Facultad de minas",
        "Sede",
    ]

    def __init__(self, facultad, id, nombre, pw):
        super().__init__(id, nombre, facultad, pw)
        super().setTipo("Coordinador")
        Coordinador._coordinadoresTotales.append(self)

    # METODOS

    @staticmethod
    def desmatricular(estudiante, grupo):
        estaMatriculado = grupo.existenciaEstudiante(estudiante)

        if estaMatriculado:
            grupo.eliminarEstudiante(estudiante)
            return "El estudiante ha sido desmatriculado de la materia y su respectivo grupo"
        else:
            return "El estudiante no estaba matriculado"

    @staticmethod
    def restaurarMateria(materia):
        for i in range(len(materia.getGrupos())):
            puntero_Grupo = materia.getGrupos()[i]
            puntero_Grupo.getProfesor().desvincularGrupo(puntero_Grupo)

            for j in range(len(puntero_Grupo.getEstudiantes())):
                puntero_Estudiante = puntero_Grupo.getEstudiantes()[j]
                Coordinador.desmatricular(puntero_Estudiante, puntero_Grupo)


    def desmatricularDelSistema(self, estudiante):
        e1 = None
        for e in Estudiante.getEstudiantes():
            if e == estudiante:
                e1 = e

        if e1 is not None:
            Estudiante.getEstudiantes().remove(e1)

        for usuario in Usuario.getUsuariosTotales():
            if isinstance(usuario, Estudiante):
                if usuario == estudiante:
                    Usuario.getUsuariosTotales().remove(usuario)
                    break

    def crearHorario(materias):
        """
        Toma una lista de materias que se desean ver.

        Crea un horario aleatorio basado en los grupos disponibles.

        Retorna una lista estática de dos elementos: Un booleano que nos dirá si fue posible o no
        crear el horario, el horario generado y la materia que no permitió crear el horario en caso de existir.
        """

        resultado = [None, None, None]
        horario = Horario()
        ok = True
        materiaObstaculo = None

        gPosible = [0] * len(materias)
        mPosibles = [0] * len(materias)
        i = 0  # índice de materias

        while True:
            pClases = materias[i].getGrupos()[gPosible[i]].getHorario()
            if horario.comprobarDisponibilidad(pClases):
                # Asignamos la materia al horario
                horario.ocuparHorario(materias[i].getGrupos()[gPosible[i]])
                # Al ponerse 1 significa que sí es posible poner dicha materia
                mPosibles[i] = 1
                # Pasamos a la siguiente materia
                i += 1
                # Comprobamos si es la última
                if i == len(materias):
                    break
            else:
                # Pasamos al siguiente grupo en la materia i
                gPosible[i] += 1

                # Comprobamos si la materia es imposible de dar
                if gPosible[i] == len(materias[i].getGrupos()):
                    # Tenemos que probar todas las posibilidades, por lo tanto probamos con el siguiente grupo de la materia i-1
                    i -= 1
                    horario.liberarHorario(
                        materias[i].getGrupos()[gPosible[i]].getHorario()
                    )
                    gPosible[i] += 1
                    gPosible[i + 1] = 0

                    # Comprobamos si, aunque iteramos todas las posibilidades, no se puede poner la materia i
                    if gPosible[i] == len(materias[i].getGrupos()):
                        m = 0
                        for k in mPosibles:
                            if k == 0:
                                materiaObstaculo = materias[m]
                                ok = False
                            else:
                                m += 1
                        break

        resultado[0] = ok
        resultado[1] = horario
        resultado[2] = materiaObstaculo

        return resultado

    
    def eliminarMateria(self, materia):
        if materia in Materia.getMateriasTotales():
            Coordinador.restaurarMateria(materia)
            Materia.getMateriasTotales().remove(materia)
        else:
            raise CampoVacio("Se ha ingresado un valor inválido")

    
    def agregarMateria(self, nombre, codigo, descripcion, creditos, facultad, prerrequisitos):
        nombreMaterias = []

        for materia in Materia.getMateriasTotales():
            nombreMaterias.append(materia.getNombre())

        if nombre not in nombreMaterias:
            nMateria = Materia(
                nombre, codigo, descripcion, creditos, facultad, prerrequisitos
            )

    @classmethod
    def candidatoABeca(cls,estudiante, tipoDeBeca):
        if tipoDeBeca.getCupos() > 0:
            if (
                estudiante.getPromedio() >= tipoDeBeca.getPromedioRequerido()
                and estudiante.getAvance() >= tipoDeBeca.getAvanceRequerido()
                and estudiante.getCreditos()
                >= tipoDeBeca.getCreditosInscritosRequeridos()
                and estudiante.getEstrato() <= tipoDeBeca.getEstratoMinimo()
            ):
                if tipoDeBeca.getNecesitaRecomendacion():
                    if Profesor.recomendarEstudiante(estudiante):
                        return True
                    else:
                        return False
                else:
                    return True  # No necesita recomendación, pero cumple los demás requisitos
            else:
                return False
        else:
            return False
    @classmethod
    def mostrarFacultades(cls):
        retorno = ""
        i = 1
        for facultad in Coordinador._facultades:
            retorno += str(i) + ". " + facultad + "\n"
            i += 1
        return retorno

    def __str__(self):
        return "Nombre Coordinador: " + self.getNombre() + "\nDocumento: " + self.getId()

    # Setters y Getters

    @classmethod
    def getLimitesCreditos(cls):
        return cls._LIMITES_CREDITOS

    @classmethod
    def getCoordinadoresTotales(cls):
        return cls._coordinadoresTotales

    @classmethod
    def setCoordinadoresTotales(cls, coordinadores):
        cls._coordinadoresTotales = coordinadores

    @classmethod
    def getFacultades(cls):
        return cls._facultades

    @classmethod
    def setFacultades(cls, facultades):
        cls._facultades = facultades
    
    @classmethod
    def mostrarBecas(cls):
        i = 1
        for beca in Beca.getBecas():
            a = beca.getConvenio()
    
    @classmethod
    def getUsuarioIngresado(cls):
        return cls._usuarioIngresado
    
    @classmethod
    def setUsuarioIngresado(cls, usuario):
        cls._usuarioIngresado = usuario