from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame

class EliminarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Aplicar Beca a Estudiante", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva beca que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Cupos", "Nombre", "Promedio Requerido", "Avance Requerido", "Estrato máximo", "Créditos Inscritos Requeridos", "Ayuda Económica", "¿La beca necesita recomendación?"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()