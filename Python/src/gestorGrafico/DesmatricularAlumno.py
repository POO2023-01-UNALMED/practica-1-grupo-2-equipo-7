from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame

class DesmatricularAlumno(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        
        nombre = Label(self, text="Desmatricular Alumno", font=("Arial", 14), fg="#42f2f5", bg="#241d1d",)
        nombre.pack(side="top", anchor="c")

        textDescripcion = ("Esta funcionalidad permite:\n1. Desmatricular a un estudiante del grupo " +
                           "y/o materia que usted desee.\n2. Desmatricular estudiante del sistema.")

        descripcion = Button(self, text=textDescripcion, font=("Arial", 10), fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        # criterios = ["Nombre", "Materia", "Grupo"]
        # valores = ["Libardo", "Fundamentos", "1"]
        # formulario = FieldFrame(self, "Criterio", criterios, "Valor", valores)
        # formulario.pack()