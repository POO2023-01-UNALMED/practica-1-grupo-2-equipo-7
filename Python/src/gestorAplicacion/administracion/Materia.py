from gestorAplicacion.administracion.Grupo import Grupo
from excepciones.ErrorManejo import *
# from Salon import Salon


class Materia:
    materiasTotales = []

    def __init__(
        self,
        nombre,
        codigo,
        descripcion,
        creditos,
        facultad,
        prerrequisitos=None,
        grupos=None,
    ):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.creditos = creditos
        self.facultad = facultad
        self.prerrequisitos = prerrequisitos or []
        self.grupos =[]
        # self.cupos =0
        self.hacerAbreviatura(nombre)
        Materia.materiasTotales.append(self)

    # MÉTODOS ESTÁTICOS

    @staticmethod
    def buscarMateria(nombre, codigo):
        # Si existe la materia, retorna su índice en la lista materiasTotales.
        # Si no existe, retorna -1.

        for i in range(len(Materia.materiasTotales)):
            if (
                Materia.materiasTotales[i].getNombre() == nombre
                and Materia.materiasTotales[i].getCodigo() == codigo
            ):
                return i
        return -1

    @staticmethod
    def puedeVerMateria(estudiante, grupo):
        from gestorAplicacion.usuario.Coordinador import Coordinador
        
        # Comprueba si un estudiante puede estar en un grupo.

        if not (
            estudiante.getCreditos() + grupo.getMateria().getCreditos()
            <= Coordinador.getLimitesCreditos()
        ):
            return False
        if not estudiante.getHorario().comprobarDisponibilidad(grupo.getHorario()):
            return False
        if grupo.getCupos() == 0:
            return False
        if not Materia.comprobarPrerrequisitos(estudiante, grupo.getMateria()):
            return False
        return True

    @staticmethod
    def comprobarPrerrequisitos(estudiante, materiap):
        # Comprueba si un estudiante cumple con los prerrequisitos de una materia.

        materiasVistas = []
        materias_estudiante=[]
        for materia in estudiante.getMaterias():
            materias_estudiante.append(materia.getCodigo())
        for grupo in estudiante.getGruposVistos():
            materiasVistas.append(grupo.getMateria().getCodigo())
        for materia in materiap.getPrerrequisitos():
            flag = False
            for vista in materiasVistas:
                if materia.getCodigo() == vista:
                    flag = True
                    break
            if not flag:
                return False
        if materiap.getCodigo() in materiasVistas:
            return False
        if materiap.getCodigo() in materias_estudiante:
            return False
        return True

    @staticmethod
    def encontrarMateria(nombre):
        mater = None
        for materia in Materia.getMateriasTotales():
            if materia.getNombre() == nombre:
                mater = materia
        return mater

    @staticmethod
    def mostrarMaterias():
        retorno = ""
        i = 1
        for materia in Materia.materiasTotales:
            retorno += f"{i}. {materia.nombre}.\n"
            i += 1
        return retorno
    
    @staticmethod
    def listaNombresMaterias():
        retorno = []
        for materia in Materia.materiasTotales:
            retorno.append(materia.getNombre())
        return retorno


    # MÉTODOS DE INSTANCIA

    def cantidadCupos(self):
        cantidad = 0
        for pGrupo in self.grupos:
            cantidad += pGrupo.getCupos()
        return cantidad

    def crearGrupo(self, numero, profesor, horario, cupos, salon):
        grupo = Grupo(self, numero, profesor, horario, cupos, salon)

        self.cantidadCupos()
        self.grupos.append(grupo)

        return grupo

    def mostrarContenidos(self):
        contenido = (
            "Materia: "
            + self.nombre
            + "\n"
            + "Codigo: "
            + str(self.codigo)
            + "\n"
            + "Creditos: "
            + str(self.creditos)
            + "\n"
            + "Facultad: "
            + self.facultad
            + "\n"
            + "Descripcion:\n"
            + self.descripcion
        )
        return contenido

    def existenciaGrupo(self, grupoBuscado):
        if self.grupos:
            for grupo in self.grupos:
                if grupo == grupoBuscado:
                    return True
            return False
        else:
            return False

    def eliminarGrupo(self, numero):
        if numero>0 and numero<=len(self.grupos):
            grupo = self.grupos[numero - 1]
            grupo.getProfesor().desvincularGrupo(grupo)
            grupo.getSalon().getHorario().liberarHorario(grupo.getHorario())
            self.grupos.remove(grupo)
            
            for i in range(numero - 1, len(self.grupos)):
                grupoCamb = self.grupos[i]
                nGrupoAnt = grupoCamb.getNumero()
                grupoCamb.setNumero(nGrupoAnt - 1)
        else:
            raise CampoInvalido()

    def agregarGrupo(self, numero, profesor, horario, cupos, salon):
        dispSalon = True
        dispProfesor = True
        daMateria = profesor.daMateria(self.nombre)

        
        dispProfesor = profesor.getHorario().comprobarDisponibilidad(horario)
        dispSalon = salon.getHorario().comprobarDisponibilidad(horario)

        if dispProfesor and dispSalon and daMateria:
            nGrupo = self.crearGrupo(numero, profesor, horario, cupos, salon)
            salon.getHorario().ocuparHorario(nGrupo, horario)
            profesor.vincularGrupo(nGrupo)
        else:
            raise GrupoNoAgregado()

    def agregarGrupoHecho(self, grupoHecho):
        self.grupos.append(grupoHecho)

    def buscarGrupoDeEstudiante(self, estudiante):
        for grupo in self.grupos:
            for e in grupo.getEstudiantes():
                if e == estudiante:
                    return grupo
        return None

    def hacerAbreviatura(self, nombre):
        abreviatura = ""
        if len(nombre) <= 13:
            self.abreviatura = nombre
        else:
            palabras = nombre.split()
            for palabra in palabras:
                if len(palabra) >= 3:
                    abreviatura += palabra[:3] + " "
                else:
                    abreviatura += palabra[: len(palabra)] + " "
            if len(abreviatura) <= 13:
                self.abreviatura = abreviatura
            else:
                self.abreviatura = abreviatura[:13]

    def mostrarGrupos(self):
        retorno = ""
        i = 1
        for grupo in self.grupos:
            retorno += f"{i}. {grupo.getNumero()}.\n"
            i += 1
        return retorno
    
    def calcularCupos(self):
        cupos =0
        for i in self.grupos:
            cupos+=i.getCupos()
            
        return cupos

    # GETTERS Y SETTERS

    @classmethod
    def getMateriasTotales(cls):
        return cls.materiasTotales

    @classmethod
    def setMateriasTotales(cls, materias):
        cls.materiasTotales = materias

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCodigo(self):
        return self.codigo

    def getCreditos(self):
        return self.creditos

    def setCreditos(self, creditos):
        self.creditos = creditos

    def getFacultad(self):
        return self.facultad

    def setFacultad(self, facultad):
        self.facultad = facultad

    def getCupos(self):
        return self.calcularCupos()

    def setCupos(self, cupos):
        self.cupos = cupos

    def getPrerrequisitos(self):
        return self.prerrequisitos

    def setPrerrequisitos(self, prerrequisitos):
        self.prerrequisitos = prerrequisitos

    def getGrupos(self):
        return self.grupos

    def setGrupos(self, grupos):
        self.grupos = grupos

    def getAbreviatura(self):
        return self.abreviatura

    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura
