from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorGrafico.FieldFrame import FieldFrame

class AplicarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")
    
        def nombresEst(estudiantes):
            listaNombres = []

            for estudiante in estudiantes:
                listaNombres.append(estudiante.getNombre())

            return listaNombres
        
        def vaciar():
            pass
        def asigBeca():
            pass
    
        titulo = Label(self, text="Aplicar Beca a Estudiante", bg="#cedae0", foreground="#085870", font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")

        textoDesc = ("A continuación, deberá seleccionar de las listas qué estudiante quiere postular y a qué beca quiere que aplique,\n en caso de cumplir con los requisitos, la ayuda económica será asignada y será informado.")
        descripcion = Label(self, text=textoDesc, bg="#cedae0", font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        aplicandoFrame = Frame(self,bg="#cedae0")
        aplicandoFrame.pack()

        becaTit = Label(aplicandoFrame, text = "Becas existentes", bg="#cedae0", font=("Arial", 11, "bold"))
        becaTit.grid(row=0, column=0, padx=10, pady=10)
        estTit = Label(aplicandoFrame, text = "Estudiantes Matriculados", bg="#cedae0", font=("Arial", 11, "bold"))
        estTit.grid(row=1, column=0, padx=10, pady=10)

        becasE = Beca.listaBecas()
        textoDefault = StringVar(aplicandoFrame, value= "Seleccione una beca")
        comboBecas = ttk.Combobox(aplicandoFrame, values=becasE, textvariable= textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)

        estE = nombresEst(Estudiante.getEstudiantes())
        textoPre = StringVar(aplicandoFrame, value= "Seleccione un estudiante")
        comboEst = ttk.Combobox(aplicandoFrame, values=estE, textvariable= textoPre)
        comboEst.grid(row=1, column=1, padx=10, pady=10)

        boton = Button(self, text="Aplicar", command=asigBeca, font=("Arial", 11), fg="white", bg="#085870")
        boton.pack()
