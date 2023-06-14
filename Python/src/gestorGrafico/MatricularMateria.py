from Estudiante import Estudiante
from Coordinador import Coordinador
from Materia import Materia
from tkinter import *


class MatricularMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Matricular Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = """Primero debe seleccionar al estudiante al cual se le matriculará
la materia deseada, luego se deberá seleccionar la materia
teniendo en cuenta los créditos y situación del estudiante y
por último se debe seleccionar el grupo de la materia, teniendo en
cuenta la disponibilidad del estudiante


Luego continúo :b"""
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

    def seleccionar_estudiante(busqueda_manual=False, busqueda_lista=False):
        estudiantes_totales = Estudiante.getEstudiantes()
        limite_creditos = Coordinador.getLimitesCreditos()
        if busqueda_lista:
            estudiantes_mostrados = []
            for estudiante in estudiantes_totales:
                if not estudiante.isMatriculaPagada():
                    continue
                elif estudiante.getCreditos() == limite_creditos:
                    continue
                estudiantes_mostrados.append(estudiante)
                print(
                    len(estudiantes_mostrados)
                    + " Nombre: "
                    + estudiante.getNombre()
                    + " ID: "
                    + estudiante.getId()
                )
                opcion2 = "Aca debe seleccionar al estudiante de todos los mostrados"
                if len(estudiantes_mostrados) == 0:
                    return "No hay estudiantes disponibles"
                try:
                    opcion2 = int(opcion2)
                    if opcion2 <= len(estudiantes_mostrados) and opcion2 >= 1:
                        estudiante_seleccionado = estudiantes_mostrados[opcion2 - 1]
                        print(
                            "Estudiante seleccionado, nombre: "
                            + estudiante_seleccionado.getNombre()
                            + " ID: "
                            + estudiante_seleccionado.getId()
                        )
                        return estudiante_seleccionado
                    else:
                        return "Error al seleccionar al estudiante mediante lista"
                except:
                    return "Error al seleccionar al estudiante mediante lista"
        elif busqueda_manual:
            nombre_estudiante = "Aca se debe ingresar el nombre del estudiante"
            id_estudiante = "Aca se debe ingresar el id del estudiante"
            try:
                id_estudiante = int(id_estudiante)
                index = Estudiante.buscarEstudiante(nombre_estudiante, id_estudiante)
                if index == -1:
                    return "Estudiante no encontrado"
                estudiante_seleccionado = estudiantes_totales[index]
                if not estudiante_seleccionado.isMatriculaPagada():
                    return "Estudiante con matricula no pagada"
                elif estudiante_seleccionado.getCreditos() >= limite_creditos:
                    return "Estudiante sin creditos suficientes"
                print(
                    "Estudiante seleccionado, nombre: "
                    + estudiante_seleccionado.getNombre()
                    + " ID: "
                    + estudiante_seleccionado.getId()
                )
                return estudiante_seleccionado
            except:
                return "Error al seleccionar al estudiante de forma manual"
        return "Sin busqueda especificada"

    def seleccionar_materia(estudiante, busqueda_manual=False, busqueda_lista=False):
        materias_totales = Materia.getMateriasTotales()
        limite_creditos = Coordinador.getLimitesCreditos()
        creditos_estudiante = estudiante.getCreditos()
        materias_estudiante = estudiante.getMaterias()
        if busqueda_lista:
            materias_disponibles = []
            for materia in materias_totales:
                if not Materia.comprobarPrerrequisitos(estudiante, materia):
                    continue
                elif materia.getCupos() <= 0:
                    continue
                elif creditos_estudiante + materia.getCreditos() > limite_creditos:
                    continue
                elif materia in materias_estudiante:
                    continue
                materias_disponibles.append(materia)
                print(
                    len(materias_disponibles)
                    + " Nombre: "
                    + materia.getNombre()
                    + " Cupos: "
                    + materia.getCupos()
                )
            opcion = "Aca debe ir la eleccion del usuario"
            if len(materias_disponibles) == 0:
                return "No hay materias disponibles para el estudiante"
            try:
                opcion = int(opcion)
                if 1 <= opcion and opcion <= len(materias_disponibles):
                    materia_seleccionada = materias_disponibles[opcion]
                    print("Materia seleccionada " + materia_seleccionada.getNombre())
                    return materia_seleccionada
                return "No se selecciono materia"
            except:
                return "Error al seleccionar la materia mediante lista"
        elif busqueda_manual:
            nombre_materia = "Aca se debe ingresar el nombre de la materia"
            codigo_materia = "Aca se debe ingresar el codigo de la materia"
            try:
                codigo_materia = int(codigo_materia)
                index = Materia.buscarMateria(nombre_materia, codigo_materia)
                if index == -1:
                    return "Materia no encontrada"
                materia_seleccionada = materias_totales[index]
                if materia_seleccionada.getCupos() <= 0:
                    return "Materia sin cupos disponibles"
                elif not Materia.comprobarPrerrequisitos(
                    estudiante, materia_seleccionada
                ):
                    return "El estudiante no cumple con los prerrequisitos"
                elif (
                    creditos_estudiante + materia_seleccionada.getCreditos()
                    > limite_creditos
                ):
                    return "El estudiante no tiene creditos suficientes"
                elif materia_seleccionada in materias_estudiante:
                    return "El estudiante ya la tiene matriculada"
                print("Materia seleccionada " + materia_seleccionada.getNombre())
                return materia_seleccionada
            except:
                return "Error al seleccionar la materia de forma manual"
        return "Sin busqueda especificada"

    def seleccionar_grupo(estudiante, materia):
        grupos_disponibles = []
        grupos_materia = materia.getGrupos()
        horario_estudiante = estudiante.getHorario()
        materias_estudiante = estudiante.getMaterias()
        grupos_estudiante = estudiante.getGrupos()
        for grupo in grupos_materia:
            horario_grupo = grupo.getHorario()
            if not horario_estudiante.comprobarDisponibilidad(horario_grupo):
                continue
            elif grupo.getCupos() <= 0:
                continue
            grupos_disponibles.append(grupo)
            print(
                len(grupos_disponibles)
                + " Grupo #"
                + grupo.getNumero()
                + " cupos: "
                + grupo.getCupos()
                + " Profesor: "
                + grupo.getProfesor().getNombre()
            )
        if len(grupos_disponibles) == 0:
            return "La materia no cuenta con grupos disponibles para el estudiante"
        opcion = "Aca va el grupo seleccionado por el usuario"
        try:
            opcion = int(opcion)
            if opcion > 0 and opcion <= len(grupos_disponibles):
                grupo_seleccionado = grupos_disponibles[opcion - 1]
                grupos_estudiante.append(grupo_seleccionado)
                materias_estudiante.append(materia)
                grupo_seleccionado.agregarEstudiante(estudiante)
                materia.cantidadCupos()
                estudiante.setCreditos(estudiante.getCreditos() + materia.getCreditos())
                estudiante.setMaterias(materias_estudiante)
                estudiante.setGrupos(grupos_estudiante)

                imprimir = (
                    "Materia "
                    + materia.getNombre()
                    + " - grupo #"
                    + grupo_seleccionado.getNumero()
                )
                print(
                    imprimir
                    + ". Ha sido matriculado al estudiante: "
                    + estudiante.getNombre()
                )
                return "Se pudo!"
            return "Error al seleccionar el grupo"
        except:
            return "Error al ingresar el grupo"

    def visualizar_horario(estudiante):
        print("estudiante.getHorario().mostrarHorario()")
