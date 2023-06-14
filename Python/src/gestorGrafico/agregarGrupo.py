from tkinter import *
from FieldFrame import FieldFrame

class agregarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Agregar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para agregar\n un grupo a una materia registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Materia", "Profesor", "Cupos", "Salón", "Horario"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()
