from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.MatricularMateria import MatricularMateria
from gestorGrafico.FieldFrame import FieldFrame

class MostrarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def mosBeca():
            infoBecas = ""
            i = 1
            for beca in Beca._becas():
                a = beca.getConvenio() 
                infoBecas += f"{str(i)}. {str(a)}.\n    Cupos disponibles: {beca.getCupos()}\n     Estrato maximo para acceder: {beca.getEstratoMinimo()}.\n    Creditos inscritos requeridos: {beca.getCreditosInscritosRequeridos()}."
            return infoBecas


        tituloenventana = Label(self, text="Mostrar Becas Existentes", foreground="#085870", font=("Helvetica", 14, "bold"))
        tituloenventana.pack(side="top", anchor="c")
        textodescriptivo = ("A continuacón puede conocer información básica sobre las becas activas actualmente.  ")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 11), fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        contenedor = Frame(self)
        contenedor.pack() 

        lista = Text(contenedor, border=False, font=("Arial", 11))
        lista.pack()
        lista.configure(height=35)
        MatricularMateria.mostrar_texto(mosBeca, lista)


