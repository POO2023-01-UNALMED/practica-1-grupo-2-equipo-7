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
        self.geometry("865x460")
        
        VentInicio(self)   
        #GenerarHorario(self)
        self.mainloop()

    def abrirLog(self):
        self.destroy()         
        VentLog()
    



Deserializador.deserializarDatos()

    
# for pHorario in Horario.getHorariosTotales():
#     print(pHorario.getGrupoContenidos())
# #     print("\n")

# for pMateria in Materia.getMateriasTotales():
#     print(pMateria.getGrupos())

# MainWin()



# c1234 = Estudiante(1234,"Libardo Jose Navarro Pedrozo","Ingenieria de Sistemas e Informatica",3,"Facultad de minas",2,97530865,[c02022_3010438,c102022_3010435,c12022_1000004,c12022_1000005,c22022_1000008,c32022_1000003,c122022_3010334,c182022_1000089,])
for pEsutiante in Estudiante.getEstudiantes():
    # grupos = pEsutiante.getMaterias()
    # materias = pEsutiante.getGruposVistos()
    
    # pEsutiante.setGruposVistos(grupos)
    # pEsutiante.setMaterias(materias)
    # if len(grupos)>=1:
    #     pEsutiante.calcularAvance()
    #     pEsutiante.calcularPromedio()
    
    print(pEsutiante.getNombre())
    print("tiene un promedio de: "+str(pEsutiante.getPromedio())+" y un avance de: "+str(pEsutiante.getAvance()))
    print(pEsutiante.getMaterias())
    print(pEsutiante.getGruposVistos())
    print("\n")

# Serializador.serializarDatos()

# Pruebas desmatricularAlumno
# for grupo in Estudiante.getEstudiantes()[0].getGrupos():
#     print(grupo.getMateria().getNombre())
# print("Estudiantes")
# for estudiante in Materia.getMateriasTotales()[0].getGrupos()[0].getEstudiantes():
#     print(estudiante.getNombre())   

# print("salio todo bien bro/sis/helicoptero apache? ;D")
