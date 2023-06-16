from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from gestorAplicacion.administracion.Materia import Materia

class GenerarHorario(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.pack()
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
                combo2.config(values=listaNombresMaterias)
                bontonFiltro.config(state="disabled")
                eleccionFil.config(state="disabled")
                valorElecc.set("Filtro")
                eleccionFil.insert(0,valorElecc)
                
        def habilitarBotonFiltro(event):
            bontonFiltro.config(state="normal")
            # print(event.keysym)
            if (len(event.widget.get())==1 or event.widget.get()=="") and event.keysym=="BackSpace":
                bontonFiltro.config(state="disable")
            else:
                bontonFiltro.config(state="normal")
                
            
                
        
        valorDefe = StringVar(value="Elegir Filtro")
        combo = ttk.Combobox(MidIzq, textvariable=valorDefe, values=["Facultad", "Creditos", "Codigo", "Ninguno"], state="readonly")
        combo.bind("<<ComboboxSelected>>", chanOpc)
        combo.pack(side="top", fill="x", pady="10", padx="100")
        
        valorElecc = StringVar(MidIzq,value="Filtro")
        eleccionFil = Entry(MidIzq,textvariable=valorElecc,state="disabled")
        eleccionFil.bind("<Key>",habilitarBotonFiltro)
        eleccionFil.pack(side="top",fill="x",pady=10,padx="100")
        
        
        def genFiltro():
            opcionFiltro = combo.current()
            filtro = eleccionFil.get()
            listaFiltrada=GenerarHorario.generarFiltro(opcionFiltro+1,filtro)
            
            listaNombresMaterias = []
            for pMateria in listaFiltrada:
                listaNombresMaterias.append(pMateria.getNombre())
            
            combo2.config(values=listaNombresMaterias)
            
        
    
        bontonFiltro=Button(MidIzq,text="Filtrar",command=genFiltro,state="disabled")
        bontonFiltro.pack(side="top",pady=20)
        
        listaNombresMaterias = []
        for pMateria in Materia.getMateriasTotales():
            listaNombresMaterias.append(pMateria.getNombre())
            
        def haceAlgo(event):
            pass
        
        valorDefe2 = StringVar(value="Materias")
        combo2 = ttk.Combobox(MidIzq, textvariable=valorDefe2, values=listaNombresMaterias, state="readonly")
        combo2.bind("<<ComboboxSelected>>", haceAlgo)
        combo2.pack(side="top", fill="x", pady="20", padx="100")
        
        
        
    
    @classmethod
    def generarFiltro(cls,opcionFiltro,filtro):
        listaFiltrada = []
        # filtro == 1 == facultad
        if opcionFiltro == 1:
            for pMateria in Materia.getMateriasTotales():
                if pMateria.getFacultad().lower() == filtro.lower():
                    listaFiltrada.append(pMateria)

        # filtro == 2 == Creditos
        elif opcionFiltro == 2:
            for pMateria in Materia.getMateriasTotales():
                if pMateria.getCreditos() == int(filtro):
                    listaFiltrada.append(pMateria)

        # filtro == 3 == Codigo
        elif opcionFiltro == 3:
            for pMateria in Materia.getMateriasTotales():
                if filtro in str(pMateria.getCodigo()):
                    listaFiltrada.append(pMateria)
                    
        return listaFiltrada



        

