from tkinter import *
#from gestorGrafico.FieldFrame import FieldFrame
from tkinter import ttk
from tkinter import messagebox
import sys
import os
from excepciones.ErrorManejo import *
from gestorAplicacion.administracion.Materia import Materia


class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def botEliminar():
            confirmacion = messagebox.askokcancel("Confirmación de eliminación", "¿Está seguro que desea eliminar el grupo {} de la materia {}?".format(entGrupo.get(), box.get()))
            if confirmacion:
                try:
                    mate = Materia.encontrarMateria(str(box.get()))
                    mate.eliminarGrupo(int(entGrupo.get()))
                    messagebox.showinfo("Grupo eliminado", "El grupo ha sido eliminado con éxito de la materia")
                except:
                    messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

                    

        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada.")
        descripcion = Label(self, text=texto, font=("Arial", 11))
        descripcion.pack(anchor="n", pady=20)

        subFrame = Frame(self)
        subFrame.pack()

        tituloC = Label(subFrame, text="Criterio", font=("Arial", 11))
        tituloC.grid(row=0, column=0, padx=10, pady=8)

        tituloV = Label(subFrame, text="Valor", font=("Arial", 11))
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        textoM = Label(subFrame, text="Materia", font=("Arial", 11))
        textoM.grid(row=1, column=0, padx=10, pady=8)

        valores = Materia.listaNombresMaterias()
        #texto = StringVar(subFrame, value="Seleccione una materia")
        box = ttk.Combobox(subFrame, values=valores, font=("Arial", 10))
        box.grid(row=1, column=1, padx=10, pady=8)

        textoM = Label(subFrame, text="Grupo", font=("Arial", 11))
        textoM.grid(row=2, column=0, padx=10, pady=8)

        entGrupo = Entry(subFrame, font=("Arial", 11))
        entGrupo.grid(row=2, column=1, padx=10, pady=8)

        botonEliminar = Button(self, text="Eliminar", command=botEliminar)
        botonEliminar.pack()
