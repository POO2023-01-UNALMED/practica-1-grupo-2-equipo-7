from tkinter import *
from tkinter import messagebox
from gestorGrafico.DesmatricularAlumno import DesmatricularAlumno
from gestorGrafico.MatricularMateria import MatricularMateria
from gestorGrafico.PostulacionBecas import PostulacionBecas
from gestorGrafico.GenerarHorario import GenerarHorario
from gestorGrafico.eliminarAgregarMateria import EliminarAgregarMateria


class VentPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(0, 0)
        self.geometry("865x460")
        self.configure(bg="#cedae0")

        def infoBasica():
            messagebox.showinfo(
                "Informacion de la aplicacion", "Sistema de matricula de materias"
            )

        def salir():
            self.destroy()

        def mostrarAutores():
            autores = (
                "Autores de la aplicacion:\n\n"
                + "Mateo Alvarez Murillo\n\n"
                + "Efrain Gomez Ramirez\n\n"
                + "Ana Sofia Gomez Zapata\n\n"
                + "Libardo Jose Navarro Pedrozo\n\n"
                + "Sebastian Ocampo Galvis"
            )

            messagebox.showinfo("Autores", autores)

        def matricularMateria():
            mataHijos(self)
            MatricularMateria(self).pack()

        def generarHorario():
            mataHijos(self)
            GenerarHorario(self).pack()

        def eliminarAgregarMateria():
            mataHijos(self)
            EliminarAgregarMateria(self).pack()
            

        def desmatricularAlumno():
            mataHijos(self)
            DesmatricularAlumno(self).pack()

        def becas():
            mataHijos(self)
            PostulacionBecas(self).pack()
        
        def mataHijos(ventana):
            for widget in ventana.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()

        menuBar = Menu(self)
        self.option_add("*tearOff",  False)
        self.config(menu=menuBar)

        menu1 = Menu(menuBar)
        menuBar.add_cascade(label="Archivo", menu=menu1)

        menu1.add_cascade(label="Aplicacion", command=infoBasica)
        menu1.add_cascade(label="Salir", command=salir)

        menu2 = Menu(menuBar)
        menuBar.add_cascade(label="Procesos y Consultas", menu=menu2)

        menu2.add_cascade(label="Matricular materia", command=matricularMateria)
        menu2.add_cascade(label="Generar Horario", command=generarHorario)
        menu2.add_cascade(label="Eliminar o agregar Materia / Grupo", command=eliminarAgregarMateria)
        menu2.add_cascade(label="Desmatricular Alumno", command=desmatricularAlumno)
        menu2.add_cascade(label="Busqueda y Postulacion de Becas", command=becas)

        menu3 = Menu(menuBar)
        menuBar.add_cascade(label="Ayuda", menu=menu3)

        menu3.add_cascade(label="Acerca de", command=mostrarAutores)

        frame = Frame(self)
        frame.pack(anchor="center")

        bienvenida_label = Label(frame, text="¡Bienvenido a la ventana principal de S.M.M!", font=("Arial", 14), fg="white", bg="#085870")
        bienvenida_label.pack(padx=10, pady=10)

        simbolo = ("  ____        __  __       __  __ \n"
        + " / ___|      |  \\/  |     |  \\/  |\n"
        + " \\___ \\      | |\\/| |     | |\\/| |\n"
        + "  ___) |  _  | |  | |  _  | |  | |\n"
        + " |____/  (_) |_|  |_| (_) |_|  |_|\n"
        + "                                 ")

        figura = Label(frame, bg="#085870", text=simbolo)
        figura.pack(anchor="center")

        informacion = """
        Esta aplicación te permite gestionar la matrícula de los estudiantes de forma eficiente. Aquí puedes realizar las siguientes acciones:

        1. Matricular Materia: Selecciona y matricula las materias para los estudiantes en el período académico actual.
        2. Generar Horario: Crea automáticamente horarios para los estudiantes, evitando conflictos de horarios entre las materias matriculadas.
        3. Agregar o Eliminar Materia/Grupo: Crea nuevas materias y grupos en la base de datos, para ofrecer más opciones a los estudiantes.
        4. Desmatricular Alumno: Cancela la matrícula de un estudiante y retira todas las materias inscritas o una sola materia de tu eleccion.
        5. Búsqueda y Postulación de Becas: Explora las becas disponibles y ayuda a los estudiantes en el proceso de postulación.

        Para comenzar, selecciona la opción deseada en el menú principal en Procesos y Consultas y sigue las instrucciones que se te presenten.

        ¡Disfruta de la experiencia de matricularte de forma rápida y eficaz!

        """
        
        info_text = Label(frame, text=informacion, font=("Arial", 10), fg="white",bg="#085870")
        info_text.pack(padx=10, pady=10)

        self.mainloop()
