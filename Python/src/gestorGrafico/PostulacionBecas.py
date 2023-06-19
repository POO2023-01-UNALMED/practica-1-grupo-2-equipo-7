from tkinter import *
from gestorGrafico.CrearBeca import CrearBeca
from gestorGrafico.EliminarBeca import EliminarBeca
from gestorGrafico.AplicarBeca import AplicarBeca
from gestorGrafico.MostrarBeca import MostrarBeca
from gestorGrafico.FieldFrame import FieldFrame

class PostulacionBecas(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")
        
        def mostrarBeca():
            self.pack_forget()
            mBeca = MostrarBeca(ventana)
            mBeca.pack()

        def aplicarBeca():
            self.pack_forget()
            aBeca = AplicarBeca(ventana)
            aBeca.pack()

        def becaNueva():
            self.pack_forget()
            cBeca = CrearBeca(ventana)
            cBeca.pack()

        def eliminarBeca():
            self.pack_forget()
            eBeca = EliminarBeca(ventana)
            eBeca.pack()
      
         
        tituloenventana = Label(self, text="Búsqueda y Postulación de Becas", bg="#cedae0", foreground="#085870", font=("Helvetica", 14, "bold"))
        tituloenventana.pack(side="top", anchor="c")
        textodescriptivo = ("Esta funcionalidad permite:\n1.Ver listado de becas existentes actualmente. \n2.Aplicar beca a estudiante." +
                           "\n3.Crear nueva beca. \n4.Eliminar beca.")
        descripcion = Label(self, text=textodescriptivo, font=("Arial", 11), bg="#cedae0", fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        seleccion = Frame(self,bg="#cedae0")
        seleccion.pack()

        mostrarB = Button(seleccion, text="Mostrar listado de becas", foreground="white",background="#085870",font=("Helvetica", 12), command= mostrarBeca)
        mostrarB.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        aplicarB = Button(seleccion, text="Aplicar beca a estudiante", foreground="white",background="#085870",font=("Helvetica", 12), command= aplicarBeca)
        aplicarB.grid(row=0,column=1,padx=10,pady=10,sticky="w")

        crearB = Button(seleccion, text="Crear nueva beca", foreground="white",background="#085870",font=("Helvetica", 12), command= becaNueva)
        crearB.grid(row=1,column=0,padx=45,pady=10,sticky="w")

        eliminarB = Button(seleccion, text="Eliminar beca", foreground="white",background="#085870",font=("Helvetica", 12), command= eliminarBeca)
        eliminarB.grid(row=1,column=1,padx=50,pady=10,sticky="w")


        
