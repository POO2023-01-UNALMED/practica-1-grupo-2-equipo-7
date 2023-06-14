from tkinter import *
from FieldFrame import FieldFrame

class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Materia", "Grupo"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()
