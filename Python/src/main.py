from tkinter import *

from gestorGrafico.ventInicio import VentInicio
from gestorGrafico.ventLog import VentLog

# from gestorAplicacion.usuario.Estudiante import Estudiante

# from baseDatos.Serializador import Serializador
# from baseDatos.Desealizador import Deserializador 
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
# Deserializador.deserializarDatos()
# # estudiante = Estudiante(121,"Sofia Jose Mira Ceja","Ingenieria de sistemas e informatica",2,"Facultad de Minas",3,15000)
# Serializador.serializarDatos()

# print(Estudiante.getEstudiantes()[0].getNombre())
# print(Estudiante.getEstudiantes()[1].getNombre())

