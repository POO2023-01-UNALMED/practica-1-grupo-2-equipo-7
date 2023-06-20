from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.administracion.Horario import Horario
from excepciones.ObjetoInexistente import *
from excepciones.ErrorManejo import *

class DesmatricularAlumno(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        def listaEstudiantes():
            self.pack_forget()
            AlumnoPorLista(ventana)

        def buscarEstudiante():
            self.pack_forget()
            AlumnoPorBusqueda(ventana)
        
        titulo = Label(self, text="Desmatricular Alumno", font=("Arial", 14), fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c", padx=5, pady=5)

        textDescripcion = ("Esta funcionalidad permite:\n1. Desmatricular a un estudiante del grupo " +
                           "y/o materia que usted desee.\n2. Desmatricular estudiante del sistema.")

        descripcion = Button(self, text=textDescripcion, font=("Arial", 10), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20)

        frame = Frame(self, bg="#cedae0")
        frame.pack(padx=5, pady=5)

        nombre = Label(frame, text="Elija como quiere seleccionar el alumno", font=("Arial", 14), fg="white", bg="#085870")
        nombre.pack(side="top", anchor="n", pady=20)

        opcion1 = Button(frame, text="Ver la lista de estudiantes", font=("Arial", 10), fg="white", bg="#085870", command=listaEstudiantes)
        opcion1.pack(side="left", pady=20, padx=10)

        opcion2 = Button(frame, text="Buscar estudiante por ID (Documento) y nombre", font=("Arial", 10), fg="white", bg="#085870", command=buscarEstudiante)
        opcion2.pack(side="right", pady=20, padx=10)



        # criterios = ["Nombre", "Materia", "Grupo"]
        # valores = ["Libardo", "Fundamentos", "1"]
        # formulario = FieldFrame(self, "Criterio", criterios, "Valor", valores)
        # formulario.pack()

class AlumnoPorLista(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self._estudianteSeleccionado = None
        self._materiaSeleccionada = None

        def desmatricularGrupo():
            if self._materiaSeleccionada == None:
                return
            
            if (grupo.existenciaEstudiante(estudiante)):

                nombresMaterias1 = []

                for g in estudiante.getGrupos():
                    if g.getMateria().getNombre() == grupo.getMateria().getNombre():
                        continue
                    nombresMaterias1.append(g.getMateria().getNombre())

                comboMaterias.config(values=nombresMaterias1)

                grupo.eliminarEstudiante(estudiante)
                estudiante.getHorario().liberarHorario(grupo.getHorario())
                messagebox.showinfo("Estudiante desmatriculado", "El estudiante ha sido desmatriculado de la materia.")
                comboMaterias.set("")

            else:
                messagebox.showwarning("Estudiante no encontrado", "El estudiante no se encuentra en la materia o ya ha sido desmatriculado")

        def seleccionMateria(event):
                global grupo
                nombreMateria = comboMaterias.get()
                if self._materiaSeleccionada is not None:
                    self._materiaSeleccionada.destroy()
                
                materia = None
                grupo = None

                for i in range(len(estudiante.getMaterias())):
                    if estudiante.getMaterias()[i].getNombre() == nombreMateria:
                        materia = i

                for i in range(len(estudiante.getGrupos())):
                    if estudiante.getGrupos()[i].getMateria().getNombre() == nombreMateria:
                        grupo = i

                grupo = estudiante.getGrupos()[grupo]
                materia = estudiante.getMaterias()[materia]

                grupo = Grupo.buscarGrupo(materia, grupo)

                infoMateria = "Materia seleccionada: " + nombreMateria + "\n"
                infoMateria += "Informacion del grupo:\n"
                infoMateria += "Numero: " + str(grupo.getNumero()) + "\n"
                infoMateria += "Profesor: " + grupo.getProfesor().getNombre()
                
                self._materiaSeleccionada = Label(der, text=infoMateria, font=("Arial", 10),bg="#085870")
                self._materiaSeleccionada.pack(anchor="c", padx=10, pady=10)

        def eleccionEstudiante(event):
            
            est = combo.get()
            if self._estudianteSeleccionado is not None:
                self._estudianteSeleccionado.destroy()
            self._estudianteSeleccionado = Label(izq, text="Estudiante seleccionado:\n" + est, font=("Arial", 12), bg="#cedae0")
            self._estudianteSeleccionado.pack(anchor="c", padx=10, pady=10)

        def nombresAlumnos(estudiantes):
            listaNombres = []

            for estudiante in estudiantes:
                listaNombres.append(estudiante.getNombre())

            return listaNombres
        
        def desmatricularDelSistema():
            if combo.get() == "":
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())
                return
            
            estudiante = None

            combo.config(state="disabled")

            for e in Estudiante.getEstudiantes():
                if e.getNombre() == combo.get():
                    estudiante = e
            combo.set("")
            estudiante.setHorario(Horario())
            estudiante.getHorario().vaciarHorario(estudiante.getGrupos())
            estudiante.desmatricularMaterias()
            Coordinador._usuarioIngresado.desmatricularDelSistema(estudiante)

            nombresEstudiantes1 = nombresAlumnos(Estudiante.getEstudiantes())
            combo.config(values=nombresEstudiantes1)
            self._estudianteSeleccionado = None
            messagebox.showinfo("Estudiante desmatriculado", "El estudiante ha sido desmatriculado del sistema con exito")

        def desmatricularMateria():
            global estudiante, comboMaterias
            nombreMateria = ""

            if combo.get() != "":
                titulo.destroy()
                descripcion.destroy()
                desmatricular1.destroy()
                desmatricular2.destroy()
                subFrame.destroy()

            
            else:
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())
                return

            combo.config(state="disabled")

            titulo2 = Label(der, text="Desmatricular de Materia", font=("Arial", 14), bg="#085870")
            titulo2.pack(side="top", anchor="center", padx=10, pady=10)

            descripcionMayor = Label(der, text="Selecciona la materia de la que quiere desmatricular al alumno", font=("Arial", 12))
            descripcionMayor.pack(side="top", pady=10)

            estudiante = None

            for e in Estudiante.getEstudiantes():
                if e.getNombre() == combo.get():
                    estudiante = e

            nombresMateriasE = []


            for grupo in estudiante.getGrupos():
                nombresMateriasE.append(grupo.getMateria().getNombre())
            
            comboMaterias = ttk.Combobox(der, values=nombresMateriasE, state="readonly")
            comboMaterias.bind("<<ComboboxSelected>>", seleccionMateria)
            comboMaterias.pack(side="top", fill="x", pady="20", padx="25", anchor="c")

            botonDesmatricular = Button(der, text="Desmatricular", font=("Arial", 10), command=desmatricularGrupo, bg="#085870", fg="white")
            botonDesmatricular.pack(side="bottom", anchor="center", pady=10)

        def retroceder():
            izq.destroy()
            der.destroy()
            DesmatricularAlumno(ventana)

        izq=Frame(ventana, height=460,width=250, bg="#085870")
        izq.pack(side="left", anchor="e")
        izq.pack_propagate(False)

        atras = Button(izq, text="Atras", font=("Arial", 10), bg="#cedae0", fg="#085870", command=retroceder)
        atras.pack(side="bottom", anchor="center", padx=10, pady=10)

        desc = Label(izq, text="Elija al estudiante", font=("Arial", 14), bg="#cedae0")
        desc.pack(side="top", anchor="c", padx=10, pady=10)

        nombresEstudiantes = nombresAlumnos(Estudiante.getEstudiantes())
        valorPredeterminado = StringVar(value="Elige el estudiante")
        combo = ttk.Combobox(izq, textvariable=valorPredeterminado, values=nombresEstudiantes, state="readonly")
        combo.bind("<<ComboboxSelected>>", eleccionEstudiante)
        combo.pack(fill="x", pady="20", padx="25") 

        der=Frame(ventana, height=460,width=615, bg="#cedae0")
        der.pack(side="right", fill="both")
        der.pack_propagate(False)

        subFrame = Frame(der, highlightbackground="#085870", highlightthickness=3)
        subFrame.pack(padx=5, pady=5, expand=True)

        titulo = Label(subFrame, text="Desmatricular Alumno", font=("Arial", 14), fg="white", bg="#085870")
        titulo.pack(side="top", anchor="center", pady=10, padx=5)

        text = "Seleccione de que quiere desmatricular al estudiante"

        descripcion = Label(subFrame, text=text, font=("Arial", 10), fg="white", bg="#085870")
        descripcion.pack(pady=10, padx=5)

        desmatricular1 = Button(subFrame, text="Desmatricular del sistema", font=("Arial", 10), fg="white", bg="#085870", command=desmatricularDelSistema)
        desmatricular1.pack(pady=20, padx=5)

        desmatricular2 = Button(subFrame, text="Desmatricular de una materia", font=("Arial", 10), fg="white", bg="#085870", command=desmatricularMateria)
        desmatricular2.pack(pady=20, padx=5)

class AlumnoPorBusqueda(Frame):

    def __init__(self,ventana):
        super().__init__(ventana)
        self._estudianteSeleccionado = None
        self._materiaSeleccionada = None

        def desmatricularGrupo():
            if self._materiaSeleccionada == None:
                return
            
            if (grupo.existenciaEstudiante(estudiante)):
                
                nombresMaterias1 = []

                for g in estudiante.getGrupos():
                    if g.getMateria().getNombre() == grupo.getMateria().getNombre():
                        continue
                    nombresMaterias1.append(g.getMateria().getNombre())

                comboMaterias.config(values=nombresMaterias1)
                grupo.eliminarEstudiante(estudiante)
                estudiante.getHorario().liberarHorario(grupo.getHorario())
                comboMaterias.set("")
                messagebox.showinfo("Estudiante desmatriculado", "El estudiante ha sido desmatriculado de la materia.")
            else:
                messagebox.showwarning("Estudiante no encontrado", "El estudiante no se encuentra en la materia o ya ha sido desmatriculado")

        def seleccionMateria(event):
                global grupo
                nombreMateria = comboMaterias.get()
                if self._materiaSeleccionada is not None:
                    self._materiaSeleccionada.destroy()
                
                materia = None
                grupo = None

                for i in range(len(estudiante.getMaterias())):
                    if estudiante.getMaterias()[i].getNombre() == nombreMateria:
                        materia = i

                for i in range(len(estudiante.getGrupos())):
                    if estudiante.getGrupos()[i].getMateria().getNombre() == nombreMateria:
                        grupo = i

                grupo = estudiante.getGrupos()[grupo]
                materia = estudiante.getMaterias()[materia]

                grupo = Grupo.buscarGrupo(materia, grupo)

                infoMateria = "Materia seleccionada: " + nombreMateria + "\n"
                infoMateria += "Informacion del grupo:\n"
                infoMateria += "Numero: " + str(grupo.getNumero()) + "\n"
                infoMateria += "Profesor: " + grupo.getProfesor().getNombre()
                
                self._materiaSeleccionada = Label(der, text=infoMateria, font=("Arial", 10), bg="#085870")
                self._materiaSeleccionada.pack(anchor="c", padx=10, pady=10)

        def buscarEstudiante():
            try:
                estudiante = fildEstudiante.getValue("Nombre")
                documento = int(fildEstudiante.getValue("Documento"))
                indice = Estudiante.buscarEstudiante(estudiante, documento)

            except:
                messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
                return

            if self._estudianteSeleccionado is not None:
                    self._estudianteSeleccionado.destroy()
            try:
                if indice != -1:
                    alumno = Estudiante.getEstudiantes()[indice]
                    self._estudianteSeleccionado = Label(izq, text="Estudiante encontrado:\n" + estudiante, font=("Arial", 12), bg="#cedae0")
                    self._estudianteSeleccionado.pack(expand=True,padx=10, pady=10)
                else:
                    raise EstudianteInexistente(estudiante)
            except EstudianteInexistente:
                messagebox.showerror("Error",EstudianteInexistente(estudiante).mostrarMensaje())

        def limpiar():
            fildEstudiante.limpiarValues()

        def desmatricularDelSistema():
            try:
                if self._estudianteSeleccionado == None:
                    raise CampoVacio
            except CampoVacio:
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())
                return
            
            estudiante = None

            for e in Estudiante.getEstudiantes():
                if e.getNombre() == fildEstudiante.getValue("Nombre"):
                    estudiante = e

            fildEstudiante.limpiarValues()
            estudiante.setHorario(Horario())
            estudiante.getHorario().vaciarHorario(estudiante.getGrupos())
            estudiante.desmatricularMaterias()
            Coordinador._usuarioIngresado.desmatricularDelSistema(estudiante)
            self._estudianteSeleccionado = None

            messagebox.showinfo("Estudiante desmatriculado", "El estudiante ha sido desmatriculado del sistema con exito")

        def desmatricularMateria():
            global estudiante, comboMaterias
            nombreMateria = ""

            try:
                if self._estudianteSeleccionado != None:
                    titulo.destroy()
                    descripcion.destroy()
                    desmatricular1.destroy()
                    desmatricular2.destroy()
                    subFrame.destroy()
                
                else:
                    raise CampoVacio
            
            except:
                messagebox.showerror("Error",CampoVacio().mostrarMensaje())
                return

            titulo2 = Label(der, text="Desmatricular de Materia", font=("Arial", 14), fg="white", bg="#085870")
            titulo2.pack(side="top", anchor="center", padx=10, pady=10)

            descripcionMayor = Label(der, text="Selecciona la materia de la que quiere desmatricular al alumno", font=("Arial", 12))
            descripcionMayor.pack(side="top", pady=10)

            estudiante = None

            for e in Estudiante.getEstudiantes():
                if e.getNombre() == fildEstudiante.getValue("Nombre"):
                    estudiante = e

            nombresMateriasE = []

            for grupo in estudiante.getGrupos():
                nombresMateriasE.append(grupo.getMateria().getNombre())
            
            comboMaterias = ttk.Combobox(der, values=nombresMateriasE, state="readonly")
            comboMaterias.bind("<<ComboboxSelected>>", seleccionMateria)
            comboMaterias.pack(side="top", fill="x", pady="20", padx="25", anchor="c")

            botonDesmatricular = Button(der, text="Desmatricular", font=("Arial", 10), fg="white", bg="#085870", command=desmatricularGrupo)
            botonDesmatricular.pack(side="bottom", anchor="center", pady=10)
        
        def retroceder():
            izq.destroy()
            der.destroy()
            DesmatricularAlumno(ventana)


        izq=Frame(ventana, height=460,width=250, bg="#085870")
        izq.pack(side="left", anchor="e")
        izq.pack_propagate(False)

        atras = Button(izq, text="Atras", font=("Arial", 10), bg="#cedae0", fg="#085870", command=retroceder)
        atras.pack(side="bottom", anchor="center", padx=10, pady=10)

        der=Frame(ventana, height=460,width=615, bg="#cedae0")
        der.pack(side="right", fill="both")
        der.pack_propagate(False)

        criterios = ["Nombre", "Documento"]
        fildEstudiante = FieldFrame(izq, "Criterio", criterios, "Valor")
        fildEstudiante.pack()

        frame = Frame(izq)
        frame.pack(fill="x")

        acept = Button(frame, text="Buscar", font=("Arial", 10), fg="white", bg="#085870", command=buscarEstudiante)
        acept.pack(side="left", anchor="ne", padx=10, pady=10)

        borrar = Button(frame, text="Borrar", font=("Arial", 10), fg="white", bg="#085870", command=limpiar)
        borrar.pack(side="right", anchor="nw", padx=10, pady=10)

        subFrame = Frame(der, highlightbackground="#085870", highlightthickness=3)
        subFrame.pack(padx=5, pady=5, expand=True)

        titulo = Label(subFrame, text="Desmatricular Alumno", font=("Arial", 14), fg="white", bg="#085870",)
        titulo.pack(side="top", anchor="center", pady=10, padx=5)

        text = "Seleccione de que quiere desmatricular al estudiante"

        descripcion = Label(subFrame, text=text, font=("Arial", 10), fg="white", bg="#085870")
        descripcion.pack(pady=10, padx=5)

        desmatricular1 = Button(subFrame, text="Desmatricular del sistema", font=("Arial", 10), fg="white", bg="#085870", command=desmatricularDelSistema)
        desmatricular1.pack(pady=20, padx=5)

        desmatricular2 = Button(subFrame, text="Desmatricular de una materia", font=("Arial", 10), fg="white", bg="#085870", command=desmatricularMateria)
        desmatricular2.pack(pady=20, padx=5)
        