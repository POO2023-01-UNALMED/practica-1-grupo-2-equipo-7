from tkinter import *
from gestorGrafico.CrearBeca import CrearBeca
from gestorGrafico.EliminarBeca import EliminarBeca
from gestorGrafico.FieldFrame import FieldFrame

class PostulacionBecas(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        
        def mostrarBeca():
            self.pack_forget()

        def aplicarBeca():
            self.pack_forget()

        def becaNueva():
            self.pack_forget()
            cBeca = CrearBeca(ventana)
            cBeca.pack()

        def eliminarBeca():
            self.pack_forget()
            eBeca = EliminarBeca(ventana)
            eBeca.pack()
      
         
        tituloenventana = Label(self, text="Eliminar Materia", font=("Arial", 14))
        tituloenventana.pack(side="top", anchor="c")
        textodescriptivo = ("Esta funcionalidad permite:\n1.Ver listado de becas existentes actualmente. \n2.Aplicar beca a estudiante." +
                           "\n3.Crear nueva beca. \n4.Eliminar beca.")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 10), fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        seleccion = Frame(self)
        seleccion.pack()

        mostrarB = Button(seleccion, text="Mostrar listado de becas", command= mostrarBeca)
        mostrarB.pack(padx=20, pady=10)

        aplicarB = Button(seleccion, text="Aplicar beca a estudiante", command= aplicarBeca)
        aplicarB.pack(padx=20, pady=10)

        crearB = Button(seleccion, text="Crear nueva beca", command= becaNueva)
        crearB.pack(padx=20, pady=10)

        eliminarB = Button(seleccion, text="Eliminar beca", command= eliminarBeca)
        eliminarB.pack(padx=20, pady=10)


        