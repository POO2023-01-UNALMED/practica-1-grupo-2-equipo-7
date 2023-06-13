from tkinter import *


class MatricularMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Matricular Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = """Primero debe seleccionar al estudiante al cual se le matriculará
la materia deseada, luego se deberá seleccionar la materia
teniendo en cuenta los créditos y situación del estudiante y
por último se debe seleccionar el grupo de la materia, teniendo en
cuenta la disponibilidad del estudiante


Luego continúo :b"""
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)
