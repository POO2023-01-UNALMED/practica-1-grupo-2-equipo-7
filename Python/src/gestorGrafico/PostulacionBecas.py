from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.CrearBeca import CrearBeca

class PostulacionBecas(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        
        def becaNueva():
            self.pack_forget()
            cBeca = CrearBeca(ventana)
            cBeca.pack()
        
            

        tituloenventana = Label(self, text="Eliminar Materia", font=("Arial", 14))
        tituloenventana.pack(side="top", anchor="c")
        textodescriptivo = ("Esta funcionalidad permite:\n1.Ver listado de becas existentes actualmente. \n2.Aplicar beca a estudiante." +
                           "\n3.Crear nueva beca. \n4.Eliminar beca.")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 10), fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        seleccion = Frame(self)
        seleccion.pack()

        crearB = Button(seleccion, text="Crear Beca", command= becaNueva)
        crearB.pack(padx=20, pady=10)
        