from tkinter import *
from tkinter import messagebox
from gestorGrafico.DesmatricularAlumno import DesmatricularAlumno
from gestorGrafico.MatricularMateria import MatricularMateria
from gestorGrafico.GenerarHorario import GenerarHorario


class VentPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(1, 1)
        self.geometry("865x460")

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
            pass

        def eliminarAgregarMateria():
            mataHijos(self)
            pass

        def desmatricularAlumno():
            mataHijos(self)
            DesmatricularAlumno(self).pack()

        def becas():
            mataHijos(self)
            pass
        
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
        menu2.add_cascade(
            label="Eliminar o agregar Materia / Grupo", command=eliminarAgregarMateria
        )
        menu2.add_cascade(label="Desmatricular Alumno", command=desmatricularAlumno)
        menu2.add_cascade(label="Busqueda y Postulacion de Becas", command=becas)

        menu3 = Menu(menuBar)
        menuBar.add_cascade(label="Ayuda", menu=menu3)

        menu3.add_cascade(label="Acerca de", command=mostrarAutores)

        self.mainloop()


if __name__ == "__main__":
    VentPrincipal()
