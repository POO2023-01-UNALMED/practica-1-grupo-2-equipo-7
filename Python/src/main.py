from tkinter import *

from gestorGrafico.ventInicio import VentInicio
from gestorGrafico.ventLog import VentLog

# Configuracion de ventana

class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(1,1)
        self.geometry("865x460")
        
        VentInicio(self)
        self.mainloop()

    def abrirLog(self):
        self.destroy()         
        VentLog()
    def abrirInicio(self):          
        VentInicio(self)

MainWin()