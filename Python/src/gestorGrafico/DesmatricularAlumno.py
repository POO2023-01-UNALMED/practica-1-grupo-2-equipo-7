from tkinter import *
from tkinter import ttk
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.usuario.Estudiante import Estudiante

class DesmatricularAlumno(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)

        def listaEstudiantes():
            self.pack_forget()
            AlumnoPorLista(ventana)
        
        nombre = Label(self, text="Desmatricular Alumno", font=("Arial", 14), fg="#42f2f5", bg="#241d1d",)
        nombre.pack(side="top", anchor="c")

        textDescripcion = ("Esta funcionalidad permite:\n1. Desmatricular a un estudiante del grupo " +
                           "y/o materia que usted desee.\n2. Desmatricular estudiante del sistema.")

        descripcion = Button(self, text=textDescripcion, font=("Arial", 10), fg="#1c0226")
        descripcion.pack(anchor="n", pady=20)

        nombre = Label(self, text="Elija como quiere seleccionar el alumno", font=("Arial", 14), fg="#42f2f5", bg="#241d1d")
        nombre.pack(anchor="n", pady=20)

        opcion1 = Button(self, text="Ver la lista de estudiantes", font=("Arial", 10), fg="#110433", command=listaEstudiantes)
        opcion1.pack(anchor="n", pady=20)

        opcion2 = Button(self, text="Buscar estudiante por ID (Documento) y nombre", font=("Arial", 10), fg="#110433")
        opcion2.pack(anchor="n", pady=20)



        # criterios = ["Nombre", "Materia", "Grupo"]
        # valores = ["Libardo", "Fundamentos", "1"]
        # formulario = FieldFrame(self, "Criterio", criterios, "Valor", valores)
        # formulario.pack()

class AlumnoPorLista(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)

        def eleccionEstudiante(self):
            
            estudiante = combo.get()
            seleccionado = Label(izq, text=estudiante, font=("Arial", 12), bg="red")
            seleccionado.pack(anchor="c", padx=10, pady=10)

        def nombresAlumnos(estudiantes):
            listaNombres = []

            for estudiante in estudiantes:
                listaNombres.append(estudiante.getNombre())

            return listaNombres
        
        izq=Frame(ventana, height=460,width=250, bg="#42f2f5")
        izq.pack(side="left", anchor="e")
        izq.pack_propagate(False)

        desc = Label(izq, text="Elija al estudiante", font=("Arial", 14), bg="red")
        desc.pack(side="top", anchor="c", padx=10, pady=10)

        nombresEstudiantes = nombresAlumnos(Estudiante.getEstudiantes())
        valorPredeterminado = StringVar(value="Elige el estudiante")
        combo = ttk.Combobox(izq, textvariable=valorPredeterminado, values=nombresEstudiantes, state="readonly")
        combo.bind("<<ComboboxSelected>>", eleccionEstudiante)
        combo.pack(fill="x", pady="20", padx="25")

        der=Frame(ventana, height=460,width=615, bg="#3f0b54")
        der.pack(side="right")
        der.pack_propagate(False)
