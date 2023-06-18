from tkinter import *
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.FieldFrame import FieldFrame

class EliminarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def confEliminar():
            pass

        titulo = Label(self, text="Eliminar Beca", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        textoDesc = ("A continuación, deberá seleccionar de la lista de becas existentes\n cuál de estas desea eliminar.")
        descripcion = Label(self, text=textoDesc, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        becaFrame = Frame(self)
        becaFrame.pack()

        becaTit = Label(becaFrame, text = "Becas existentes", font=("Arial", 10))
        becaTit.grid(row=0, column=0, padx=10, pady=10)

        becasE = Beca.listaBecas()
        textoDefault = StringVar(becaFrame, value= "Seleccione una beca")
        comboBecas = ttk.Combobox(becaFrame, values=becasE, textvariable= textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)
        
        boton = Button(self, text="Eliminar", command=confEliminar)
        boton.pack()
