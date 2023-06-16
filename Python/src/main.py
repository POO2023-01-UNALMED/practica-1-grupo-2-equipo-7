from tkinter import *
from gestorGrafico.ventInicio import VentInicio
from gestorGrafico.ventLog import VentLog
from gestorGrafico.ventPrincipal import VentPrincipal

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

Deserializador.deserializarDatos()
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
    

MainWin()





# for i in range(0,len(Estudiante.getEstudiantes())):
#     print(Estudiante.getEstudiantes()[i].getNombre())


Serializador.serializarDatos()

print("salio todo bien bro/sis ;D")
