from tkinter import *
from tkinter import ttk
from gestorGrafico.FieldFrame import FieldFrame

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Agregar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Nombre", "Código", "Descripción", "Créditos", "Facultad"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()

        subFrame = Frame(self)
        subFrame.pack()

        textoP = Label(subFrame, text="Prerrquisitos", font=("Arial", 10))
        textoP.grid(row=0, column=0, padx=10, pady=10)

        boxP = ttk.Combobox(subFrame, values=["Si","No"])
        boxP.grid(row=0, column=1, padx=10, pady=10)
