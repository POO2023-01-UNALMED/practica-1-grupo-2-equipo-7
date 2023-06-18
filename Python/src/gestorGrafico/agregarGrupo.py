from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.administracion.Salon import Salon
from gestorAplicacion.usuario.Profesor import Profesor

class agregarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        def siguiente():
            mNombre = mateC.get()
            materia = Materia.encontrarMateria(mNombre)
            nProfe = profeC.get()
            profesor = Profesor.encontrarProfe(nProfe)
            cupos = int(cuposE.get())
            nSalon = salonC.get()
            salon = Salon.encontrarSalon(nSalon)
            sesiones = int(sesionesE.get())
            horario = []

            sFrame.pack_forget()
            botonSiguiente.pack_forget()
            subFrame = Frame(self)
            subFrame.pack()
            diaL = Label(subFrame, text="Día", font=("Arial", 10))
            diaL.grid(row=0, column=0, padx=10, pady=10)

            hiL = Label(subFrame, text="Hora Inicio", font=("Arial", 10))
            hiL.grid(row=0, column=1, padx=10, pady=10)

            hfL = Label(subFrame, text="Hora Final", font=("Arial", 10))
            hfL.grid(row=0, column=2, padx=10, pady=10)

            dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            horas = ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
            vDias = {"Lunes":1, "Martes":2, "Miércoles":3, "Jueves":4, "Viernes":5, "Sábado":6, "Domingo":7}
            diasBoxes = []
            hiBoxes = []
            hfBoxes = []
            for i in range(sesiones):
                dia = ttk.Combobox(subFrame, values=dias)
                dia.grid(row=i+1, column=0, padx=10, pady=10)
                diasBoxes.append(dia)

                hi = ttk.Combobox(subFrame, values=horas)
                hi.grid(row=i+1, column=1, padx=10, pady=10)
                hiBoxes.append(hi)
                
                hf = ttk.Combobox(subFrame, values=horas)
                hf.grid(row=i+1, column=2, padx=10, pady=10)
                hfBoxes.append(hf)

            def agregar():
                confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar este grupo a {}?".format(mNombre))
                if confirmacion:
                    for i in range(sesiones):
                        d = diasBoxes[i].get()
                        formato = str(vDias[d])+"-"+hiBoxes[i].get()[:2:]+"-"+hfBoxes[i].get()[:2:]
                        horario.append(formato)
                    numero = len(Materia.getMateriasTotales())+1
                    materia.agregarGrupo(numero, profesor, horario, cupos, salon)
                    messagebox.showinfo("Grupo agregado", "El grupo ha sido agregado con éxito a la materia")

            bAgregar = Button(self, text="Agregar grupo", command=agregar)
            bAgregar.pack()
                
        def filtrarProfes(event):
            mate = mateC.get()
            lProfes = Profesor.nombresProfesDeMateria(mate)
            profeC["values"] = lProfes

        titulo = Label(self, text="Agregar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para agregar\n un grupo a una materia registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        sFrame = Frame(self)
        sFrame.pack()

        mateL = Label(sFrame, text="Materia", font=("Arial", 10))
        mateL.grid(row=0, column=0, padx=10, pady=10)
        vMates = Materia.listaNombresMaterias()
        mateC = ttk.Combobox(sFrame, values=vMates)
        mateC.grid(row=0, column=1, padx=10, pady=10)
        mateC.bind("<<ComboboxSelected>>", filtrarProfes)

        profeL = Label(sFrame, text="Profesor", font=("Arial", 10))
        profeL.grid(row=1, column=0, padx=10, pady=10)
        profeC = ttk.Combobox(sFrame)
        profeC.grid(row=1, column=1, padx=10, pady=10)

        cuposL = Label(sFrame, text="Cupos", font=("Arial", 10))
        cuposL.grid(row=2, column=0, padx=10, pady=10)
        cuposE = Entry(sFrame, font=("Arial", 10))
        cuposE.grid(row=2, column=1, padx=10, pady=10)

        salonL = Label(sFrame, text="Salón", font=("Arial", 10))
        salonL.grid(row=3, column=0, padx=10, pady=10)
        vSalones = Salon.nombresSalones()
        salonC = ttk.Combobox(sFrame, values=vSalones)
        salonC.grid(row=3, column=1, padx=10, pady=10)

        sesionesL = Label(sFrame, text="Sesiones de clase", font=("Arial", 10))
        sesionesL.grid(row=4, column=0, padx=10, pady=10)
        sesionesE = Entry(sFrame, font=("Arial", 10))
        sesionesE.grid(row=4, column=1, padx=10, pady=10)

        botonSiguiente = Button(self, text="Siguiente", command=siguiente)
        botonSiguiente.pack()
