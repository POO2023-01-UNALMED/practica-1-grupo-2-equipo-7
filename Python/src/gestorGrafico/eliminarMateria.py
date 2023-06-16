from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador
import sys
import os

#sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/administracion/"))
#from Materia import Materia


class eliminarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def botEliminar():
            confirmacion = messagebox.askokcancel("Confirmación de eliminación", "¿Está seguro que desea eliminar la materia {} del sistema?".format(box.get()))
            if confirmacion:
                mate = Materia.encontrarMateria(str(box.get()))

                Coordinador.eliminarMateria(mate)
                messagebox.showinfo("Materia eliminada", "La materia ha sido eliminada con éxito del sistema")

        titulo = Label(self, text="Eliminar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n una materia que esté registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        subFrame = Frame(self)
        subFrame.pack()

        tituloC = Label(subFrame, text="Criterio", font=("Arial", 10))
        tituloC.grid(row=0, column=0, padx=10, pady=10)

        tituloV = Label(subFrame, text="Valor", font=("Arial", 10))
        tituloV.grid(row=0, column=1, padx=10, pady=10)

        textoM = Label(subFrame, text="Materia", font=("Arial", 10))
        textoM.grid(row=1, column=0, padx=10, pady=10)

        valores = Materia.listaNombresMaterias()
        texto = StringVar(subFrame, value="Seleccione una materia")
        box = ttk.Combobox(subFrame, values=valores, textvariable=texto)
        box.grid(row=1, column=1, padx=10, pady=10)

        botonElimiar = Button(self, text="Eliminar", command=botEliminar)
        botonElimiar.pack()
