from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *
import sys
import os

#sys.path.append(os.path.join(os.path.dirname(__file__), "../gestorAplicacion/administracion/"))
#from Materia import Materia


class eliminarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")

        def botEliminar():
            confirmacion = messagebox.askokcancel("Confirmación de eliminación", "¿Está seguro que desea eliminar la materia {} del sistema?".format(box.get()))
            if confirmacion:
                mate = Materia.encontrarMateria(str(box.get()))
                try:
                    Coordinador.getUsuarioIngresado().eliminarMateria(mate)
                    messagebox.showinfo("Materia eliminada", "La materia ha sido eliminada con éxito del sistema")
                except:
                    messagebox.showerror("Error", CampoVacio().mostrarMensaje())

        def limpiar():
            box.delete(0, last= END)

        titulo = Label(self, text="Eliminar Materia", font=("Arial", 14),  fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n una materia que esté registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20)

        subFrame = Frame(self, bg="#cedae0")
        subFrame.pack()

        tituloC = Label(subFrame, text="Criterio", font=("Arial", 11), fg="white", bg="#085870")
        tituloC.grid(row=0, column=0, padx=10, pady=10)

        tituloV = Label(subFrame, text="Valor", font=("Arial", 11), fg="white", bg="#085870")
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        textoM = Label(subFrame, text="Materia", font=("Arial", 11), fg="white", bg="#085870")
        textoM.grid(row=1, column=0, padx=10, pady=8)

        valores = Materia.listaNombresMaterias()
        #texto = StringVar(subFrame, value="Seleccione una materia")
        box = ttk.Combobox(subFrame, values=valores, font=("Arial", 10))
        box.grid(row=1, column=1, padx=10, pady=8)

        botonEliminar = Button(subFrame, text="Eliminar", command=botEliminar, font=("Arial", 11), fg="white", bg="#085870")
        botonEliminar.grid(row=2, column=0, padx=10, pady=10)

        botonLimpiar = Button(subFrame, text="Limpiar", command=limpiar, font=("Arial", 11), fg="white", bg="#085870")
        botonLimpiar.grid(row=2, column=1, padx=10, pady=10)
