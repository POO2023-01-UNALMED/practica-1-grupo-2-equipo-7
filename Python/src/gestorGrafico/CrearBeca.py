from tkinter import *
from tkinter import ttk
from gestorGrafico.FieldFrame import FieldFrame

class CrearBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")

        def crear():
            cupos = int(cuposE.get())
            convenio = nombreE.get()
            promedio = float(promedioE.get())
            pass

        titulo = Label(self, text="Crear Beca", bg="#cedae0", foreground="#085870", font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva beca que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 11), bg="#cedae0")
        descripcion.pack(anchor="n")

        creandoBeca = Frame(self, bg="#cedae0")
        creandoBeca.pack()
        
        crit = Label(creandoBeca, text="Criterios", font=("Arial", 11, "bold"), fg="#085870", bg="#cedae0")
        crit.grid(row=0, column=0, padx=10, pady=10)

        val = Label(creandoBeca, text="Valores", font=("Arial", 11, "bold"), fg="#085870", bg="#cedae0")
        val.grid(row=0, column=1, padx=10, pady=5)

        cuposL = Label(creandoBeca, text="Cupos", font=("Arial", 11), fg="#085870", bg="#cedae0")
        cuposL.grid(row=1, column=0, padx=10, pady=5)
        cuposE = Entry(creandoBeca, font=("Arial", 11))
        cuposE.grid(row=1, column=1, padx=10, pady=5)
        
        nombreL = Label(creandoBeca, text="Nombre", font=("Arial", 11), fg="#085870", bg="#cedae0")
        nombreL.grid(row=2, column=0, padx=10, pady=10)
        nombreE = Entry(creandoBeca, font=("Arial", 11))
        nombreE.grid(row=2, column=1, padx=10, pady=5)

        promedioL = Label(creandoBeca, text="Promedio requerido", font=("Arial", 11), fg="#085870", bg="#cedae0")
        promedioL.grid(row=3, column=0, padx=10, pady=5)
        promedioE = Entry(creandoBeca, font=("Arial", 11))
        promedioE.grid(row=3, column=1, padx=10, pady=5)

        avanceL = Label(creandoBeca, text="Avance requerido", font=("Arial", 11), fg="#085870", bg="#cedae0")
        avanceL.grid(row=4, column=0, padx=10, pady=5)
        avanceE = Entry(creandoBeca, font=("Arial", 11))
        avanceE.grid(row=4, column=1, padx=10, pady=5)

        estratoL = Label(creandoBeca, text="Estrato máximo\n para aplicar", font=("Arial", 11), fg="#085870", bg="#cedae0")
        estratoL.grid(row=5, column=0, padx=10, pady=5)
        estratoE = Entry(creandoBeca, font=("Arial", 11))
        estratoE.grid(row=5, column=1, padx=10, pady=5)

        creditosL = Label(creandoBeca, text="Creditos inscritos\n requeridos", font=("Arial", 11), fg="#085870", bg="#cedae0")
        creditosL.grid(row=6, column=0, padx=10, pady=5)
        creditosE = Entry(creandoBeca, font=("Arial", 11))
        creditosE.grid(row=6, column=1, padx=10, pady=5)

        ayudaL = Label(creandoBeca, text="Ayuda económica", font=("Arial", 11), fg="#085870", bg="#cedae0")
        ayudaL.grid(row=7, column=0, padx=10, pady=5)
        ayudaE = Entry(creandoBeca, font=("Arial", 11))
        ayudaE.grid(row=7, column=1, padx=10, pady=5)

        recomendacionB = Label(creandoBeca, text="¿La beca necesita\nrecomendación?", font=("Arial", 11), fg="#085870", bg="#cedae0")
        recomendacionB.grid(row=8, column=0, padx=10)
        combo = ttk.Combobox(creandoBeca, values=["Sí.","No."])
        combo.grid(row=8, column=1, padx=10)

        boton =  boton = Button(self, text="Crear Beca", command=crear, font=("Arial", 11, "bold"), fg="white", bg="#085870")
        boton.pack()


