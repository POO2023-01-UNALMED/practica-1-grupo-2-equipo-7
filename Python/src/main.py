from tkinter import *

from gestorGrafico.ventInicio import VentInicio
from gestorGrafico.ventLog import VentLog

from gestorAplicacion.administracion.Beca import Beca
from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.administracion.Salon import Salon
from gestorAplicacion.usuario.Coordinador import Coordinador
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Profesor import Profesor
from gestorAplicacion.usuario.Usuario import Usuario

from baseDatos.Serializador import Serializador
from baseDatos.Desealizador import Deserializador 

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
Deserializador.deserializarDatos()

# materia = Materia("Calculo diferencial",)




# print(Estudiante.getEstudiantes()[0].getNombre())
# print(Estudiante.getEstudiantes()[1].getNombre())
# Serializador.serializarDatos()

