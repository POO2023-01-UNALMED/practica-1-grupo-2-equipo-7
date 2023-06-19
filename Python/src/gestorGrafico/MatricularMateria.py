from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Materia import Materia
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *
from gestorGrafico.FieldFrame import FieldFrame
from tkinter import messagebox
from tkinter import *


class MatricularMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self._ventana=ventana
        titulo = Label(self, text="Matricular Materia", foreground="#085870",font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")
        texto = """En esta parte, debes seleccionar al estudiante deseado de dos formas:
1. Búsqueda manual: Ingresa el ID y nombre del estudiante.
2. Búsqueda por lista: Selecciona un estudiante de una lista disponible."""
        descripcion = Label(self, text=texto, font=("Arial", 11))
        descripcion.pack(anchor="n", pady=10)
        opciones = Frame(self)
        opciones.pack()
        manual = Button(opciones,text="Seleccionar al estudiante\n de forma manual",foreground="white",background="#085870",font=("Helvetica", 12),command=lambda: self.seleccionar_estudiante(caja, label_vacio, False))
        lista = Button(opciones,text="Seleccionar al estudiante\n mediante una lista",foreground="white",background="#085870",font=("Helvetica", 12),command=lambda: self.seleccionar_estudiante(caja, label_vacio, True))
        manual.pack(side=LEFT, padx=(0, 10))
        lista.pack(side=LEFT, padx=(10, 10))
        busqueda = Frame(self)
        busqueda.pack()
        label_vacio = Label(busqueda, text="",font=("Arial", 11))
        label_vacio.pack(pady=(10, 10))
        caja = Frame(self)
        caja.pack()

    @classmethod
    def mostrar_texto(cls, string, texto):
        texto.delete("1.0", "end")
        texto.insert(INSERT, string)
        texto.pack(fill=X, expand=True, padx=(10, 10))

    @classmethod
    def es_numero(cls, numero):
        try:
            numero=int(numero)
            return True
        except:
            return False

    @classmethod
    def limpiar_frame(cls, frame):
        for widget in frame.winfo_children():
            widget.destroy()


    def seleccionar_estudiante(self, frame, label, busqueda_lista=False):
        MatricularMateria.limpiar_frame(frame)
        self.estudiantes_totales = Estudiante.getEstudiantes()
        self.limite_creditos = Coordinador.getLimitesCreditos()
        if busqueda_lista:
            label.config(text="Entro a busqueda por lista")
            nombres_texto = ""
            self.estudiantes_mostrados = []
            for estudiante in self.estudiantes_totales:
                if not estudiante.isMatriculaPagada():
                    continue
                elif estudiante.getCreditos() == self.limite_creditos:
                    continue
                self.estudiantes_mostrados.append(estudiante)
                nombres_texto+=str(len(self.estudiantes_mostrados))+ "- Nombre: "+ estudiante.getNombre()+ " ID: "+ str(estudiante.getId())+"\n"
            if nombres_texto=="":
                nombres_texto="No hay estudiantes disponibles para matricular"
            lista = Text(frame, border=False, font=("Arial", 11))
            lista.pack()
            lista.configure(height=5)
            self.mostrar_texto(nombres_texto, lista)
            self.campo = FieldFrame(frame, "Criterio", ["Numero"], "Valor")
            self.campo.crearBotones(self.comprobacion1, "Aceptar", 10, 0, 0)
            self.campo.crearBotones(self.campo.limpiarValues, "Limpiar", 10, 1, 0)
            self.campo.pack()
        else:
            MatricularMateria.limpiar_frame(frame)
            label.config(text="Entro a busqueda manual")
            self.campo2 = FieldFrame(frame, "Criterio", ["Nombre", "ID"], "Valor")
            self.campo2.crearBotones(self.comprobacion2, "Aceptar", 10, 0, 0)
            self.campo2.crearBotones(self.campo2.limpiarValues, "Limpiar", 10, 1, 0)
            self.campo2.pack()


    def comprobacion1(self):
        opcion=self.campo.getValue("Numero")
        try:
            if opcion=="":
                    raise Exception
            try:
                opcion=int(opcion)
                if opcion <= len(self.estudiantes_mostrados) and opcion >= 1:
                    estudiante_seleccionado = self.estudiantes_mostrados[opcion - 1]
                    opcion = messagebox.askokcancel("Confirmación","Estudiante seleccionado: "+ estudiante_seleccionado.getNombre())
                    if opcion:
                        self.destroy()
                        MatricularMateria2(self._ventana, estudiante_seleccionado).pack()
                else:
                    raise Exception
            except:
                messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
        except:
            messagebox.showerror("Error",CampoVacio().mostrarMensaje())
            

    def comprobacion2(self):
        id_estudiante=self.campo2.getValue("ID")
        nombre_estudiante=self.campo2.getValue("Nombre")
        if id_estudiante=="" or nombre_estudiante=="":
            messagebox.showerror("Error",CampoVacio().mostrarMensaje())
        try:
            index = Estudiante.buscarEstudiante(nombre_estudiante, int(id_estudiante))
            if index == -1:
                messagebox.showerror("Error",EstudianteInexistente("").mostrarMensaje())
            else:
                estudiante_seleccionado = self.estudiantes_totales[index]
                if not estudiante_seleccionado.isMatriculaPagada():
                    messagebox.showerror("Error",EstudianteSinMatriculaPagada(nombre_estudiante).mostrarMensaje())
                elif estudiante_seleccionado.getCreditos() >= self.limite_creditos:
                    messagebox.showerror("Error",EstudianteSinCreditos(nombre_estudiante).mostrarMensaje())
                else:
                    opcion = messagebox.askokcancel("Confirmación","Estudiante seleccionado: "+ estudiante_seleccionado.getNombre())
                    if opcion:
                        self.destroy()
                        MatricularMateria2(self._ventana, estudiante_seleccionado).pack()
        except:
            messagebox.showerror("Error",CampoInvalido().mostrarMensaje())


class MatricularMateria2(Frame):
    def __init__(self, ventana, estudiante):
        super().__init__(ventana)
        self.ventana=ventana
        self.estudiante=estudiante
        titulo = Label(self, text="Matricular Materia 2", foreground="#085870",font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")
        texto = """En esta parte, debes seleccionar la materia deseada de dos formas:
1. Búsqueda manual: Ingresa el código y nombre de la materia.
2. Búsqueda por lista: Selecciona una materia de una lista disponible."""
        seleccionados="Estudiante: "+self.estudiante.getNombre()
        seleccion=Label(self, text=seleccionados, font=("Arial", 11,"bold"))
        seleccion.pack(anchor="n", pady=5)
        descripcion = Label(self, text=texto, font=("Arial", 11))
        descripcion.pack(anchor="n", pady=5)
        opciones = Frame(self)
        opciones.pack()
        manual = Button(opciones,text="Seleccionar la materia\n de forma manual",foreground="white",background="#085870",font=("Helvetica", 12),command=lambda: self.seleccionar_materia(caja, label_vacio, False))
        lista = Button(opciones,text="Seleccionar la materia\n mediante una lista",foreground="white",background="#085870",font=("Helvetica", 12),command=lambda: self.seleccionar_materia(caja, label_vacio, True))
        manual.pack(side=LEFT, padx=(0, 10))
        lista.pack(side=LEFT, padx=(10, 10))
        busqueda = Frame(self)
        busqueda.pack()
        label_vacio = Label(busqueda, text="",font=("Arial", 11))
        label_vacio.pack(pady=(10, 10))
        caja = Frame(self)
        caja.pack()


    def seleccionar_materia(self, ventana, label, busqueda_lista=False):
        self.materias_totales = Materia.getMateriasTotales()
        self.limite_creditos = Coordinador.getLimitesCreditos()
        self.creditos_estudiante = self.estudiante.getCreditos()
        self.materias_estudiante = self.estudiante.getMaterias()
        if busqueda_lista:
            MatricularMateria.limpiar_frame(ventana)
            label.config(text="Entro a busqueda por lista")
            materias_texto=""
            self.materias_disponibles = []
            for materia in self.materias_totales:
                if not Materia.comprobarPrerrequisitos(self.estudiante, materia):
                    continue
                elif materia.getCupos() <= 0:
                    continue
                elif self.creditos_estudiante + materia.getCreditos() > self.limite_creditos:
                    continue
                elif materia in self.materias_estudiante:
                    continue
                self.materias_disponibles.append(materia)
                materias_texto+=str(len(self.materias_disponibles))+ " - Nombre: "+ materia.getNombre()+ " Cupos: "+ str(materia.getCupos())+"\n"
            lista = Text(ventana, border=False, font=("Arial", 11))
            lista.pack()
            lista.configure(height=5)
            if (materias_texto==""):
                materias_texto="No hay materias disponibles para el estudiante"
            MatricularMateria.mostrar_texto(materias_texto, lista)
            self.campo = FieldFrame(ventana, "Criterio", ["Numero"], "Valor")
            self.campo.crearBotones(self.comprobar1, "Aceptar", 10, 0, 0)
            self.campo.crearBotones(self.campo.limpiarValues, "Limpiar", 10, 1, 0)
            self.campo.crearBotones(self.regreso, "Regresar", 10, 2, 0)
            self.campo.pack()
        else:
            MatricularMateria.limpiar_frame(ventana)
            label.config(text="Entro a busqueda manual")
            self.campo2 = FieldFrame(ventana, "Criterio", ["Nombre", "Codigo"], "Valor")
            self.campo2.crearBotones(self.comprobar2, "Aceptar", 10, 0, 0)
            self.campo2.crearBotones(self.campo2.limpiarValues, "Limpiar", 10, 1, 0)
            self.campo2.crearBotones(self.regreso, "Regresar", 10, 2, 0) 
            self.campo2.pack()


    def regreso(self):
        self.destroy()
        MatricularMateria(self.ventana).pack()
        

    def comprobar1(self):
        opcion = self.campo.getValue("Numero")
        if opcion=="":
            messagebox.showerror("Error",CampoVacio().mostrarMensaje())
        else:
            try:
                opcion=int(opcion)
                if opcion <= len(self.materias_disponibles) and opcion >= 1:
                    materia_seleccionada = self.materias_disponibles[opcion-1]
                    opcion2 = messagebox.askokcancel("Confirmación","Materia seleccionada: "+ materia_seleccionada.getNombre())
                    if opcion2:
                        self.destroy()
                        MatricularMateria3(self.ventana, self.estudiante, materia_seleccionada).pack()
                else:
                    messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
            except:
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())

    def comprobar2(self):
        nombre_materia = self.campo2.getValue("Nombre")
        codigo_materia = self.campo2.getValue("Codigo")
        if codigo_materia=="" or nombre_materia=="":
            messagebox.showerror("Error",CampoVacio().mostrarMensaje())
        else:
            try:
                index = Materia.buscarMateria(nombre_materia, int(codigo_materia))
                if index == -1:
                    messagebox.showerror("Error",MateriaInexistente("").mostrarMensaje())
                else:
                    materia_seleccionada = self.materias_totales[index]
                    if materia_seleccionada.getCupos() <= 0:
                        messagebox.showerror("Error",MateriaSinCupo(nombre_materia).mostrarMensaje())
                    elif not Materia.comprobarPrerrequisitos(self.estudiante, materia_seleccionada):
                        messagebox.showerror("Error",PrerrequisitosMateria(nombre_materia).mostrarMensaje())
                    elif (self.creditos_estudiante + materia_seleccionada.getCreditos()> self.limite_creditos):
                        messagebox.showerror("Error",EstudianteSinCreditos(self.estudiante.getNombre()).mostrarMensaje())
                    elif materia_seleccionada in self.materias_estudiante:
                        messagebox.showerror("Error",MateriaMatriculada(self.estudiante.getNombre()).mostrarMensaje())
                    else:
                        opcion = messagebox.askokcancel("Confirmación","Materia seleccionada: "+ materia_seleccionada.getNombre())
                        if opcion:
                            self.destroy()
                            MatricularMateria3(self.ventana, self.estudiante, materia_seleccionada).pack()
            except:
                messagebox.showerror("Error",CampoInvalido().mostrarMensaje())


class MatricularMateria3(Frame):
    def __init__(self, ventana, estudiante, materia):
        super().__init__(ventana)
        self.ventana=ventana
        self.estudiante=estudiante
        self.materia=materia
        titulo = Label(self, text="Matricular Materia 3", foreground="#085870",font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")
        texto = """En esta parte, debes seleccionar el grupo deseado mediante una lista de los disponibles:"""
        seleccionados="Estudiante: "+self.estudiante.getNombre()+"\nMateria: "+self.materia.getNombre()
        seleccion=Label(self, text=seleccionados, font=("Arial", 11,"bold"))
        seleccion.pack(anchor="n", pady=5)
        descripcion = Label(self, text=texto, font=("Arial", 11))
        descripcion.pack(anchor="n", pady=5)
        caja = Frame(self)
        caja.pack()
        self.grupos_disponibles = []
        self.grupos_materia = self.materia.getGrupos()
        horarioPrueba=self.estudiante.getHorario()
        self.horario_estudiante = horarioPrueba if not horarioPrueba is None else Horario()
        self.materias_estudiante = self.estudiante.getMaterias()

        self.grupos_estudiante = self.estudiante.getGrupos() 
        grupos_texto = ""
        for grupo in self.grupos_materia:
            horario_grupo = grupo.getHorario()
            if horario_grupo is None:
                horario_grupo==Horario()
            if not self.horario_estudiante.comprobarDisponibilidad(horario_grupo):
                continue
            if grupo.getCupos() <= 0:
                continue
            if grupo.getHorario()==[]:
                continue
            self.grupos_disponibles.append(grupo)
            grupos_texto+=str(len(self.grupos_disponibles))+ " - Grupo #"+ str(grupo.getNumero())+ " cupos: "+ str(grupo.getCupos())+ " Profesor: "+ grupo.getProfesor().getNombre()+"\n"
        if grupos_texto=="":
            grupos_texto="No hay grupos disponibles para el estudiante"
        lista = Text(caja, border=False, font=("Arial", 11))
        lista.pack()
        lista.configure(height=7)
        MatricularMateria.mostrar_texto(grupos_texto, lista)
        self.campo = FieldFrame(caja, "Criterio", ["Numero"], "Valor")
        self.campo.crearBotones(self.comprobar, "Aceptar", 10, 0, 0)
        self.campo.crearBotones(self.campo.limpiarValues, "Limpiar", 10, 1, 0)
        self.campo.crearBotones(self.regreso, "Regresar", 10, 2, 0) 
        self.campo.pack()

    
    def regreso(self):
        self.destroy()
        MatricularMateria2(self.ventana, self.estudiante).pack()

    def comprobar(self):
        opcion = self.campo.getValue("Numero")
        if opcion=="":
            messagebox.showerror("Error",CampoVacio().mostrarMensaje())
        else:
            try:
                opcion=int(opcion)
                if opcion <= len(self.grupos_disponibles) and opcion >= 1:
                    grupo_seleccionado = self.grupos_disponibles[opcion - 1]
                    self.grupos_estudiante.append(grupo_seleccionado)
                    self.materias_estudiante.append(self.materia)
                    grupo_seleccionado.agregarEstudiante(self.estudiante)
                    self.materia.cantidadCupos()
                    self.estudiante.setCreditos(self.estudiante.getCreditos() + self.materia.getCreditos())
                    self.estudiante.setMaterias(self.materias_estudiante)
                    self.estudiante.setGrupos(self.grupos_estudiante)
                    self.horario_estudiante.ocuparHorario(grupo_seleccionado, grupo_seleccionado.getHorario())
                    self.estudiante.setHorario(self.horario_estudiante)
                    imprimir = "Materia "+ self.materia.getNombre()+ " - grupo #"+ str(grupo_seleccionado.getNumero())
                    imprimir+=". Ha sido matriculado al estudiante: "+ self.estudiante.getNombre()
                    opcion3 = messagebox.askokcancel("Confirmación","Matriculación exitosa "+imprimir+"\n\nDesea ver el horario del estudiante?")
                    if opcion3:
                        self.destroy()
                        MatricularMateria4(self.ventana, self.estudiante).pack()
                    else:
                        self.destroy()
                        MatricularMateria(self.ventana).pack()
                else:
                    raise Exception
            except:
                messagebox.showerror("Error",CampoInvalido().mostrarMensaje())


class MatricularMateria4(Frame):
    def __init__(self, ventana, estudiante):
        super().__init__(ventana)
        self.ventana=ventana
        self.estudiante=estudiante
        titulo = Label(self, text="Mostrar horario estudiante", foreground="#085870",font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")
        seleccionado="Estudiante seleccionado: "+self.estudiante.getNombre()
        seleccion=Label(self, text=seleccionado, font=("Arial", 11,"bold"))
        seleccion.pack(anchor="n", pady=10)
        caja = Frame(self)
        caja.pack()

        horarioFrame = Frame(caja,width=855,height=310)
        horarioFrame.pack(side="top",padx=5,pady=5)
        horarioFrame.pack_propagate(False)
        horario=self.estudiante.getHorario().mostrarHorario2()
        horarioText = Text(horarioFrame,width=855,height=100)
        horarioText.pack(side="top",fill="x")
        horarioText.insert(1.0,horario)

        boton = Button(caja, text="Regresar",foreground="white",background="#085870",font=("Helvetica", 12), command=self.regresar)
        boton.pack(pady=10)


    def regresar(self):
        self.destroy()
        MatricularMateria(self.ventana).pack()    
