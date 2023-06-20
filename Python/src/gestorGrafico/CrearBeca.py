from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.administracion.Beca import Beca
from excepciones.ErrorManejo import *
from gestorGrafico.FieldFrame import FieldFrame

class CrearBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        nombres = []
        for beca in Beca._becas:
            nom = beca.getConvenio()
            nombres.append(nom)

        def crear():
            cupos = int(cuposE.get())
            convenio = nombreE.get()
            promedio = float(promedioE.get())
            avance = int(avanceE.get())
            estrato = int(estratoE.get())
            creditos = int(creditosE.get())
            ayudaEco = int(ayudaE.get())
            necesitaR = combo.get()

            confirmar = messagebox.askokcancel("Confirmación", f"¿Está seguro de que desea agregar la beca: {convenio} al sistema?")
            if confirmar:
                if cupos<0 or avance<0 or estrato<0 or creditos<0 or ayudaEco<0 or promedio<0:
                    return messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
                
                for n in nombres:
                    if n == convenio:
                        return messagebox.showerror("Error",BecaExistente().mostrarMensaje())
                    
                if necesitaR == "":
                    return messagebox.showerror("Error",CampoVacio().mostrarMensaje())
                
                if necesitaR == "Si":
                    necesitaR = True
                else:
                    if necesitaR == "No":
                        necesitaR = False

                if cupos>0 and avance>0 and estrato>0 and creditos>0 and ayudaEco>0 and promedio>0:
                    nuevaBeca = (cupos, convenio, promedio, avance, estrato, creditos, ayudaEco, necesitaR)
                    return messagebox.showinfo("Beca agregada", "La beca ha sido agregada con éxito al sistema.")
                

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
        combo = ttk.Combobox(creandoBeca, values=["Si.","No."])
        combo.grid(row=8, column=1, padx=10)

        boton =  boton = Button(self, text="Crear Beca", command=crear, font=("Arial", 11, "bold"), fg="white", bg="#085870")
        boton.pack()


