from tkinter import *
from tkinter import ttk
from gestorGrafico.FieldFrame import FieldFrame

class CrearBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Crear Beca", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva beca que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n")

        criteriosB = ["Cupos", "Nombre", "Promedio Requerido", "Avance Requerido", "Estrato máximo", "Créditos Inscritos Requeridos", "Ayuda Económica"]
        datosB = FieldFrame(self, "Criterio", criteriosB, "Valor", None)
        datosB.pack(anchor="n")

        extra = Frame(self)
        extra.pack()

        recomendacionB = Label(extra, text="¿La beca necesita recomendación?", font=("Arial", 10))
        recomendacionB.grid(row=0, column=0, padx=10)

        combo = ttk.Combobox(extra, values=["Sí.","No."])
        combo.grid(row=0, column=1, padx=10)


