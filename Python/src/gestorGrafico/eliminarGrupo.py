from tkinter import *
#from gestorGrafico.FieldFrame import FieldFrame
from tkinter import ttk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/administracion/"))
from Materia import Materia

class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        subFrame = Frame(self)
        subFrame.pack()

        tituloC = Label(subFrame, text="Criterio", font=("Arial", 10))
        tituloC.grid(row=0, column=0, padx=10, pady=10)

        tituloV = Label(subFrame, text="Valor", font=("Arial", 10))
        tituloV.grid(row=0, column=1, padx=10, pady=10)

        textoM = Label(subFrame, text="Materia", font=("Arial", 10))
        textoM.grid(row=1, column=0, padx=10, pady=10)

        valores = Materia.mostrarMaterias()
        texto = StringVar(subFrame, value="Seleccione una materia")
        box = ttk.Combobox(subFrame, values=valores, textvariable=texto)
        box.grid(row=1, column=1, padx=10, pady=10)

        textoM = Label(subFrame, text="Grupo", font=("Arial", 10))
        textoM.grid(row=2, column=0, padx=10, pady=10)
