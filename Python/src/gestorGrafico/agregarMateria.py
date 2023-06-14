from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Agregar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Nombre", "Código", "Descripción", "Créditos", "Facultad", "Prerrequisitos"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()
