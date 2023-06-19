from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.usuario.Coordinador import Coordinador
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def siguiente():
            try:
                nombre = formulario.getValue("Nombre")
                codigo = int(formulario.getValue("Código"))
                descripcion = formulario.getValue("Descripción")
                creditos = int(formulario.getValue("Créditos"))
                nPrer = int(formulario.getValue("Prerrequisitos"))
                if nPrer<0 or nPrer>5:
                    raise CampoInvalido()
                prerrequisitos = []
                facultad = facuE.get()

                if nPrer>0:
                    boxes = []
                    formulario.pack_forget()
                    botonSiguiente.pack_forget()
                    sFrame.pack_forget()

                    subFrame = Frame(self)
                    subFrame.pack()
                    tituloC = Label(subFrame, text="Criterio", font=("Arial", 11))
                    tituloC.grid(row=0, column=0, padx=10, pady=8)

                    tituloV = Label(subFrame, text="Materia", font=("Arial", 11))
                    tituloV.grid(row=0, column=1, padx=10, pady=8)
                    for i in range(nPrer):

                        lCriterio = Label(subFrame, text="Prerrequisito {}".format(str(i+1)), font=("Arial", 11))
                        lCriterio.grid(row=i+1, column=0, padx=10, pady=8)

                        valores = Materia.listaNombresMaterias()
                        prer = ttk.Combobox(subFrame, values=valores, font=("Arial", 11))
                        prer.grid(row=i+1, column=1, padx=10, pady=8)
                        boxes.append(prer)

                    def finalizarP():
                        confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                        if confirmacion:
                            try:
                                for box in boxes:
                                    if not isinstance(Materia.encontrarMateria(box.get()), Materia):
                                        raise CampoVacio()
                                Coordinador.getCoordinadorIngresado().agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                                messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")
                            except:
                                messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

                    bAgregar = Button(self, text="Agregar materia", command=finalizarP)
                    bAgregar.pack()
                else:
                    confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar la materia {} al sistema?".format(nombre))
                    if confirmacion:
                        try:
                            Coordinador.getCoordinadorIngresado().agregarMateria(nombre, codigo, descripcion, creditos, facultad, prerrequisitos)
                            messagebox.showinfo("Materia agregada", "La materia ha sido agregada con éxito al sistema")
                        except:
                            messagebox.showerror("Error", CampoInvalido().mostrarMensaje())
            except:
                messagebox.showerror("Error", CampoVacio().mostrarMensaje())
                
                
        titulo = Label(self, text="Agregar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 11))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Nombre", "Código", "Descripción", "Créditos", "Prerrequisitos"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()

        sFrame = Frame(self)
        sFrame.pack()

        facuL = Label(sFrame, text="     Facultad   ", font=("Arial", 11))
        facuL.grid(row=0, column=0, padx=10, pady=8)
        valores = Coordinador.getFacultades()
        facuE = ttk.Combobox(sFrame, values=valores, font=("Arial", 10))
        facuE.grid(row=0, column=1, padx=10, pady=8)

        botonSiguiente = Button(self, text="Siguiente", command=siguiente)
        botonSiguiente.pack()
