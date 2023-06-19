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
        self.geometry("865x480")
        self.configure(bg="#cedae0")
        self.pack_propagate(False)
        self.iconbitmap("Python\src\gestorGrafico\Imagenes\icono.ico")

        def infoBasica():
            texto = """Bienvenido a nuestra aplicación de Matrícula de Materias.

Nuestra aplicación te permite gestionar de manera eficiente y sencilla el proceso de matrícula de materias en tu institución educativa. Con nuestra aplicación, podrás realizar las siguientes acciones:

1. Matricular materia: Selecciona al estudiante la materias que desea cursar en el próximo período académico y confirma su inscripción.

2. Generar horario: Crea automáticamente un horario de clases basado en las materias que selecciones al estudiante, teniendo en cuenta los horarios disponibles y las restricciones establecidas.

3. Agregar o eliminar materia/grupo: Realiza cambios en la base de datos de materias, ya sea para agregar nuevas materias o eliminar aquellas que ya no deseas que esten en el sistema.

4. Desmatricular alumno: En caso de que necesites cancelar una matrícula en su totalidad, puedes utilizar esta opción para desmatricular de todas las materias inscritas.

5. Búsqueda y postulación de becas: Explora las becas disponibles y postula estudiantes que cumplan con sus requisitos y objetivos académicos.

Estamos comprometidos con brindarte una experiencia fácil de usar y confiable. Si tienes alguna pregunta o necesitas ayuda, no dudes en contactar a nuestro equipo de soporte técnico.

¡Esperamos que disfrutes de nuestra aplicación y tengas un exitoso período académico!
            """
            messagebox.showinfo(
                "Informacion de la aplicacion", texto
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
        frame.pack(anchor="center",expand=True)
        # frame.pack_propagate(False)

        bienvenida_label = Label(frame, text="¡Bienvenido a la ventana principal de S.M.M!", font=("Arial", 14), fg="white", bg="#085870")
        bienvenida_label.pack(padx=10, pady=10)

        simbolo = ("  ____        __  __       __  __ \n"
        + " / ___|      |  \\/  |     |  \\/  |\n"
        + " \\___ \\      | |\\/| |     | |\\/| |\n"
        + "  ___) |  _  | |  | |  _  | |  | |\n"
        + " |____/  (_) |_|  |_| (_) |_|  |_|\n"
        + "                                 ")

        self.imagen = PhotoImage(file="Python\src\gestorGrafico\Imagenes\imgVentPrincipal.png")
        figura = Label(frame,height=108,width=192,image=self.imagen)
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
