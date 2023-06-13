from tkinter import *
from tkinter import Tk

class VentLog(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(1,1)
        self.geometry("865x460")
        
        frame = Frame(self, width=400, height=200)
        frame.pack(expand=True)
        
        usuar = Label(frame,text="Usuario")
        entrada1 = Entry(frame)
        cont = Label(frame,text="Contraseña")
        entrada2 = Entry(frame)
        boton_confirmar = Button(frame,text="Confirmar")
        boton_limpiar = Button(frame,text="Limpiar")
        
        usuar.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        entrada1.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
        cont.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        entrada2.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
        boton_confirmar.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        boton_limpiar.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        self.mainloop()
        
    
        
       
        
