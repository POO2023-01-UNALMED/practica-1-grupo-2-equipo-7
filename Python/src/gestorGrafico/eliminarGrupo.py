from tkinter import *
#from gestorGrafico.FieldFrame import FieldFrame
from tkinter import ttk
from tkinter import messagebox
import sys
import os

from gestorAplicacion.administracion.Materia import Materia

class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def botEliminar():
            confirmacion = messagebox.askokcancel("Confirmación de eliminación", "¿Está seguro que desea eliminar el grupo {} de la materia {}?".format(entGrupo.get(), box.get()))
            if confirmacion:
                mate = Materia.encontrarMateria(str(box.get()))
                try:
                    mate.eliminarGrupo(int(entGrupo.get()))
                    messagebox.showinfo("Grupo eliminado", "El grupo ha sido eliminado con éxito de la materia")
                except IndexError:
                    messagebox.showerror("Error", "El número ingresado no corresponde a ningún grupo registrado en la materia")

                    

        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada.")
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

        textoM = Label(subFrame, text="Grupo", font=("Arial", 10))
        textoM.grid(row=2, column=0, padx=10, pady=10)

        entGrupo = Entry(subFrame, font=("Arial", 10))
        entGrupo.grid(row=2, column=1, padx=10, pady=10)

        botonEliminar = Button(self, text="Eliminar", command=botEliminar)
        botonEliminar.pack()
