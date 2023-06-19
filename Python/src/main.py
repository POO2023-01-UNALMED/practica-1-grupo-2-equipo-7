from tkinter import *
from gestorGrafico.ventInicio import VentInicio
from gestorGrafico.ventLog import VentLog
from gestorGrafico.ventPrincipal import VentPrincipal
from gestorGrafico.GenerarHorario import GenerarHorario

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
        self.resizable(0,0)
        self.geometry("865x480")
        self.iconbitmap("Python\src\gestorGrafico\Imagenes\icono.ico")
        
        
        Coordinador.setCoordinadorIngresado(None)
        VentInicio(self)
        #GenerarHorario(self)
        self.mainloop()

    def abrirLog(self):
        self.destroy()         
        VentLog()
    



Deserializador.deserializarDatos()




MainWin()


# Serializador.serializarDatos()

