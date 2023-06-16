from tkinter import *
from tkinter import StringVar
from tkinter import ttk

class GenerarHorario(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        # self.pack_propagate(False)
        

        titulo = Label(self, text="Generar Horario", font=("Arial", 14))
        titulo.pack(side="top", fill="x",padx=5,pady=10)

        texto = """Esta opcion le permitira generar un horario en base a unas materias seleccionadas, para luego poder asignarselo a algun estudiante o descartarlo"""
        descripcion = Label(self, text=texto, font=("Arial", 10),wraplength=400)
        descripcion.pack(side="top", fill="x",padx=5)
        
       
        FrameCont = Frame(self,bg="green",width=855,height=380)
        FrameCont.pack(side="top",padx=5,pady=5)
        FrameCont.grid_propagate(False)
        
        MidIzq=Frame(FrameCont,height=340,width=418,bg="red")
        MidIzq.grid(row=0,column=0,padx=5,pady=5)
        MidIzq.pack_propagate(False)
        
        MidDer=Frame(FrameCont,height=340,width=418,bg="blue")
        MidDer.grid(row=0,column=1,padx=5,pady=5)
        
        def chanOpc(event):
            if combo.get()!="Ninguno":
                eleccionFil.config(state="normal")
                valorElecc.set("")
            else:
                eleccionFil.config(state="disabled")
                valorElecc.set("Filtro")
                eleccionFil.insert(0,valorElecc)
                
        valorDefecto = StringVar(value="Filtro")
        combo = ttk.Combobox(MidIzq,values=["Facultad","Codigo","Creditos","Ninguno"],textvariable=valorDefecto,state="readonly")
        combo.bind("<<ComboboxSelected>>",chanOpc)
        combo.pack(side="top",fill="x",pady="10",padx="20")
        
        
        valorElecc = StringVar(MidIzq,value="Filtro")
        eleccionFil = Entry(MidIzq,textvariable=valorElecc,state="disabled")
        eleccionFil.pack(side="top",fill="x",pady=10,padx="20")
        
        



        

