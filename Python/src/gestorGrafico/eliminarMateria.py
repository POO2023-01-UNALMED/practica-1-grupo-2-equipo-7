from tkinter import *
from tkinter import ttk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/administracion/"))
from Materia import Materia


class eliminarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Eliminar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n una materia que esté registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        valores = Materia.mostrarMaterias()
        texto = StringVar(self, value="Seleccione una materia")
        box = ttk.Combobox(self, values=valores, textvariable=texto)
        box.pack()
