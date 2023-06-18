from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def siguiente():
            nombre = formulario.getValue("Nombre")
            codigo = int(formulario.getValue("Código"))
            descripcion = formulario.getValue("Descripción")
            creditos = int(formulario.getValue("Créditos"))
            nPrer = int(formulario.getValue("Prerrequisitos"))
            prerrequisitos = []
            facultad = facuE.get()
            if nPrer>0:
                boxes = []
                formulario.pack_forget()
                botonSiguiente.pack_forget()
                subFrame = Frame(self)
                subFrame.pack()
                tituloC = Label(subFrame, text="Criterio", font=("Arial", 10))
                tituloC.grid(row=0, column=0, padx=10, pady=10)

                tituloV = Label(subFrame, text="Materia", font=("Arial", 10))
                tituloV.grid(row=0, column=1, padx=10, pady=10)
                for i in range(nPrer):

                    lCriterio = Label(subFrame, text="Prerrequisito {}".format(str(i+1)), font=("Arial", 10))
                    lCriterio.grid(row=i+1, column=0, padx=10, pady=10)

                    valores = Materia.listaNombresMaterias()
                    prer = ttk.Combobox(subFrame, values=valores)
                    prer.grid(row=i+1, column=1, padx=10, pady=10)
                    boxes.append(prer)

                def finalizarP():
                    for box in boxes:
                        prerrequisitos.append(box.get())
                    confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                    if confirmacion:
                        Coordinador.agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                        messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")

                bAgregar = Button(self, text="Agregar materia", command=finalizarP)
                bAgregar.pack()
            else:
                confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                if confirmacion:
                    Coordinador.agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                    messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")
                
                
        titulo = Label(self, text="Agregar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Nombre", "Código", "Descripción", "Créditos", "Prerrequisitos"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()

        subFrame = Frame(self)
        subFrame.pack()

        facuL = Label(subFrame, text="     Facultad  ", font=("Arial", 10))
        facuL.grid(row=0, column=0, padx=10, pady=10)
        valores = Coordinador.getFacultades()
        facuE = ttk.Combobox(subFrame, values=valores)
        facuE.grid(row=0, column=1, padx=10, pady=10)

        botonSiguiente = Button(self, text="Siguiente", command=siguiente)
        botonSiguiente.pack()
