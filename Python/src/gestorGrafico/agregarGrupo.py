from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.administracion.Salon import Salon
from gestorAplicacion.usuario.Profesor import Profesor
from excepciones.ErrorManejo import *
from excepciones.ObjetoInexistente import *

class agregarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        def limpiar1():
            mateC.delete(0, last= END)
            profeC.delete(0, last= END)
            cuposE.delete(0, last= END)
            salonC.delete(0, last= END)
            sesionesE.delete(0, last= END)

        def siguiente():
            try:
                mNombre = mateC.get()
                materia = Materia.encontrarMateria(mNombre)
                nProfe = profeC.get()
                profesor = Profesor.encontrarProfe(nProfe)
                cupos = int(cuposE.get())
                nSalon = salonC.get()
                salon = Salon.encontrarSalon(nSalon)
                sesiones = int(sesionesE.get())
                horario = []

                if sesiones<=0 or sesiones>7:
                    raise CampoInvalido()

                sFrame.pack_forget()
                botonSiguiente.pack_forget()
                subFrame = Frame(self, bg="#cedae0")
                subFrame.pack(padx=5, pady=5)
                diaL = Label(subFrame, text="Día", font=("Arial", 11), fg="white", bg="#085870")
                diaL.grid(row=0, column=0, padx=10, pady=8)

                hiL = Label(subFrame, text="Hora Inicio", font=("Arial", 11), fg="white", bg="#085870")
                hiL.grid(row=0, column=1, padx=10, pady=8)

                hfL = Label(subFrame, text="Hora Final", font=("Arial", 11), fg="white", bg="#085870")
                hfL.grid(row=0, column=2, padx=10, pady=8)

                dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
                horas = ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
                vDias = {"Lunes":1, "Martes":2, "Miércoles":3, "Jueves":4, "Viernes":5, "Sábado":6, "Domingo":7}
                diasBoxes = []
                hiBoxes = []
                hfBoxes = []
                for i in range(sesiones):
                    dia = ttk.Combobox(subFrame, values=dias, font=("Arial", 10))
                    dia.grid(row=i+1, column=0, padx=10, pady=8)
                    diasBoxes.append(dia)

                    horI = ttk.Combobox(subFrame, values=horas, font=("Arial", 10))
                    horI.grid(row=i+1, column=1, padx=10, pady=8)
                    hiBoxes.append(horI)
                    
                    horF = ttk.Combobox(subFrame, values=horas, font=("Arial", 10))
                    horF.grid(row=i+1, column=2, padx=10, pady=8)
                    hfBoxes.append(horF)

                def agregar():
                    confirmacion = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea agregar este grupo a {}?".format(mNombre))
                    if confirmacion:
                        try:
                            for i in range(sesiones):                                
                                d = diasBoxes[i].get()
                                hi = hiBoxes[i].get()
                                hf = hfBoxes[i].get()

                                if d not in dias or hi not in horas or hf not in horas or int(hi[:2:])>=int(hf[:2:]):
                                    raise CampoInvalido()
                                
                                formato = str(vDias[d])+"-"+hi[:2:]+"-"+hf[:2:]
                                horario.append(formato)
                            copia = horario
                            for i in range (len(horario)-1):
                                for hor in horario:
                                    if copia[i]==hor and horario.index(hor)!=i:
                                        raise CampoInvalido()
                            numero = len(Materia.getMateriasTotales())+1
                            materia.agregarGrupo(numero, profesor, horario, cupos, salon)
                            messagebox.showinfo("Grupo agregado", "El grupo ha sido agregado con éxito a la materia")
                        except GrupoNoAgregado:
                            messagebox.showerror("Error", GrupoNoAgregado().mostrarMensaje())
                        except:
                            messagebox.showerror("Error", CampoInvalido().mostrarMensaje())
                def limpiar2():
                    for i in range(sesiones):
                        diasBoxes[i].delete(0, last= END)
                        hiBoxes[i].delete(0, last= END)
                        hfBoxes[i].delete(0, last= END)

                otroFrame = Frame(self, bg="#cedae0")
                otroFrame.pack(padx=5, pady=5)

                bAgregar = Button(otroFrame, text="Agregar grupo", command=agregar, font=("Arial", 11), fg="white", bg="#085870")
                bAgregar.grid(row=sesiones+1, column=0, padx=10, pady=10, sticky='e')

                bLimpiar = Button(otroFrame, text="Limpiar", command=limpiar2, font=("Arial", 11), fg="white", bg="#085870")
                bLimpiar.grid(row=sesiones+1, column=1, padx=10, pady=10)
            except:
                messagebox.showerror("Error", CampoInvalido().mostrarMensaje())

                
        def filtrarProfes(event):
            mate = mateC.get()
            lProfes = Profesor.nombresProfesDeMateria(mate)
            profeC["values"] = lProfes

        titulo = Label(self, text="Agregar Grupo", font=("Arial", 14),  fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c", padx=5, pady=5)

        texto = ("A continuación, deberá ingresar la información necesaria para agregar\n un grupo a una materia registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20, padx=5)

        sFrame = Frame(self, bg="#cedae0")
        sFrame.pack(padx=5, pady=5)

        tituloC = Label(sFrame, text="Criterios", font=("Arial", 11), fg="white", bg="#085870")
        tituloC.grid(row=0, column=0, padx=10, pady=8)

        tituloV = Label(sFrame, text="Valores", font=("Arial", 11), fg="white", bg="#085870")
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        mateL = Label(sFrame, text="Materia", font=("Arial", 11), fg="white", bg="#085870")
        mateL.grid(row=1, column=0, padx=10, pady=8)
        vMates = Materia.listaNombresMaterias()
        mateC = ttk.Combobox(sFrame, values=vMates, font=("Arial", 10))
        mateC.grid(row=1, column=1, padx=10, pady=8)
        mateC.bind("<<ComboboxSelected>>", filtrarProfes)

        profeL = Label(sFrame, text="Profesor", font=("Arial", 11), fg="white", bg="#085870")
        profeL.grid(row=2, column=0, padx=10, pady=8)
        profeC = ttk.Combobox(sFrame, font=("Arial", 10))
        profeC.grid(row=2, column=1, padx=10, pady=8)

        cuposL = Label(sFrame, text="Cupos", font=("Arial", 11), fg="white", bg="#085870")
        cuposL.grid(row=3, column=0, padx=10, pady=8)
        cuposE = Entry(sFrame, font=("Arial", 11))
        cuposE.grid(row=3, column=1, padx=10, pady=8)

        salonL = Label(sFrame, text="Salón", font=("Arial", 11), fg="white", bg="#085870")
        salonL.grid(row=4, column=0, padx=10, pady=8)
        vSalones = Salon.nombresSalones()
        salonC = ttk.Combobox(sFrame, values=vSalones, font=("Arial", 10))
        salonC.grid(row=4, column=1, padx=10, pady=8)

        sesionesL = Label(sFrame, text="# Sesiones de clase", font=("Arial", 11), fg="white", bg="#085870")
        sesionesL.grid(row=5, column=0, padx=10, pady=8)
        sesionesE = Entry(sFrame, font=("Arial", 11))
        sesionesE.grid(row=5, column=1, padx=10, pady=8)

        botonSiguiente = Button(sFrame, text="Siguiente", command=siguiente, font=("Arial", 11), fg="white", bg="#085870")
        botonSiguiente.grid(row=6, column=0, padx=10, pady=10, sticky='e')

        botonLimpiar = Button(sFrame, text="Limpiar", command=limpiar1, font=("Arial", 11), fg="white", bg="#085870")
        botonLimpiar.grid(row=6, column=1, padx=10, pady=10)
