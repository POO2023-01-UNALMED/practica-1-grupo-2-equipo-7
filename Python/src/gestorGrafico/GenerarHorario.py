from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from gestorAplicacion.administracion.Horario import Horario
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.administracion.Materia import Materia
from gestorAplicacion.usuario.Coordinador import Coordinador

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
        
        RecoleccionDat(self)

class RecoleccionDat(Frame):
    def __init__(self,ventana):
            super().__init__(ventana)
            self.pack()
       
            FrameCont = Frame(self,bg="green",width=855,height=380)
            FrameCont.pack(side="top",padx=5,pady=5)
            FrameCont.grid_propagate(False)
            
            MidIzq=Frame(FrameCont,height=340,width=268,bg="red")
            MidIzq.grid(row=0,column=0,padx=5,pady=5)
            MidIzq.pack_propagate(False)
            
            MidDer=Frame(FrameCont,height=340,width=568,bg="blue")
            MidDer.grid(row=0,column=1,padx=5,pady=5)
            MidDer.pack_propagate(False)
            
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
            combo.pack(side="top", fill="x", pady="10", padx="25")
            
            valorElecc = StringVar(MidIzq,value="Filtro")
            eleccionFil = Entry(MidIzq,textvariable=valorElecc,state="disabled")
            eleccionFil.bind("<Key>",habilitarBotonFiltro)
            eleccionFil.pack(side="top",fill="x",pady=10,padx="25")
            
            
            def genFiltro():
                opcionFiltro = combo.current()
                filtro = eleccionFil.get()
                global listaFiltrada
                listaFiltrada=RecoleccionDat.generarFiltro(opcionFiltro+1,filtro)
                
                listaNombresMaterias = []
                for pMateria in listaFiltrada:
                    listaNombresMaterias.append(pMateria.getNombre())
                
                combo2.config(values=listaNombresMaterias)
                
            
        
            bontonFiltro=Button(MidIzq,text="Filtrar",command=genFiltro,state="disabled")
            bontonFiltro.pack(side="top",pady=20)
            
            listaNombresMaterias = []
            for pMateria in Materia.getMateriasTotales():
                listaNombresMaterias.append(pMateria.getNombre())
            
            self.listaAMostrar =[]
            def agregarMtaeria(event):
                # global listaAMostrar
                # listaAMostrar = []
                materia = combo2.get()
                for pMateria in Materia.getMateriasTotales():
                    if pMateria.getNombre() == materia:
                        if pMateria not in self.listaAMostrar:
                            self.listaAMostrar.append(pMateria)
                            break
                        else:
                            messagebox.showinfo("!Ya esta¡","La materia que quieres agregar ya esta en la lista")
                            break
                
                
                # print(self.listaAMostrar)
                txt = self.mostrarLista(self.listaAMostrar)
                materiasText.delete(1.0,"end")
                materiasText.insert(1.0,txt)
            
            valorDefe2 = StringVar(value="Materias")
            combo2 = ttk.Combobox(MidIzq, textvariable=valorDefe2, values=listaNombresMaterias, state="readonly")
            combo2.bind("<<ComboboxSelected>>", agregarMtaeria)
            combo2.pack(side="top", fill="x", pady="20", padx="25")
            
            
            materiasText = scrolledtext.ScrolledText(MidDer,height=10,width=100)
            materiasText.pack(side="top",pady=10,padx=10)
            materiasText.insert(1.0,("%-3s %-40s %-10s %-10s" % ("Num", "Nombre", "Facultad", "Codigo"))+"\n")
            
            fraBotones=Frame(MidDer,bg="purple")
            fraBotones.pack(side="top",padx=10,pady=10)
            
            def eliminarUltima():
                if len(self.listaAMostrar)>=1:
                    self.listaAMostrar.pop()
                    txt = self.mostrarLista(self.listaAMostrar)
                    materiasText.delete(1.0,"end")
                    materiasText.insert("end",txt)
                    
            def eliminarTodas():
                self.listaAMostrar=[]
                materiasText.delete(2.0,"end")
                
            def generar():
                if len(self.listaAMostrar)>=1:
                    generacion = Coordinador.crearHorario(self.listaAMostrar)
                    if generacion[0]:
                        horarioGenerado(ventana,generacion[1])
                        self.destroy()
            
                    else:
                        messagebox.showinfo("Horario no logrado","No fue posible generar el horario, ya que "+generacion[2].getNombre()+" es un obstaculo")
                else:
                    messagebox.showinfo("Vacio","No hay nada que generar :/")
                
            bottEliminarUltima = Button(fraBotones,text="Eliminar Ultima",command=eliminarUltima)
            bottEliminarUltima.pack(side="left",padx=10,pady=10)
            
            bottLimpiar = Button(fraBotones,text="Eliminar todas",command=eliminarTodas)
            bottLimpiar.pack(side="left",padx=10,pady=10)
        
            bottGenerar = Button(fraBotones,text="Generar",command=generar)
            bottGenerar.pack(side="left",padx=10,pady=10)
            
            
            
    
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
    
    @classmethod
    def mostrarLista(cls,ListaAMostrar):
        txt = ""
        con = 1
        txt+=("%-3s %-40s %-10s %-10s" % ("Num", "Nombre", "Facultad", "Codigo"))+"\n"

        
        for pMateria in ListaAMostrar:
            facultad = pMateria.getFacultad()
            # print(facultad)
            if facultad == "Facultad de ciencias humanas y economicas":
                facultad = "FCHE"
            elif facultad=="Sede":
                pass
            else:
                facultad = (pMateria.getFacultad()[12:])
                facultad = facultad.capitalize()
            txt+=("%-3d %-40s %-10s %-10d" % (con, pMateria.getNombre(), facultad, pMateria.getCodigo()))+"\n"
            con += 1
        
        return txt



        
class horarioGenerado(Frame):
    def __init__(self,ventana,horarioAMostrar):
        super().__init__(ventana)
        self.pack()

        FrameCont2 = Frame(self,bg="green",width=855,height=310)
        FrameCont2.pack(side="top",padx=5,pady=5)
        FrameCont2.pack_propagate(False)
        
        horario=horarioAMostrar.mostrarHorario2()
        
        horarioText = Text(FrameCont2,width=855,height=100)
        horarioText.pack(side="top",fill="x")
        horarioText.insert(1.0,horario)
        
        
        fraBotones=Frame(self,bg="purple",height=60)
        fraBotones.pack(side="top",fill="both",padx=5,pady=(0,5))
        fraBotones.pack_propagate(False)
        
        def descartar():
            self.destroy()
            RecoleccionDat(ventana)
        
        # def conservarAsignar():
        self.listaEstudiantes=[]
        listaNombresEstu=[]
        for pEstudiante in Estudiante.getEstudiantes():
            if (pEstudiante.isMatriculaPagada()):
                listaNombresEstu.append(pEstudiante.getNombre())
                self.listaEstudiantes.append(pEstudiante) 
            
        def asignar():
            estudianteElegido = self.listaEstudiantes[combo3.current()]
            tempHorario = estudianteElegido.getHorario()
            estudianteElegido.setHorario(Horario())
            
            flag = True
            for pGrupo in horarioAMostrar.getGrupoContenidos():
                if not Materia.puedeVerMateria(estudianteElegido, pGrupo):
                    flag = False
                    break
                
            mens = False
            nMateria = ""
            for pGrupo in estudianteElegido.getGruposVistos():
                for pGrupo1 in horarioAMostrar.getGrupoContenidos():
                    if pGrupo.getMateria().getCodigo() == pGrupo1.getMateria().getCodigo():
                        flag = False
                        mens = True
                        nMateria = pGrupo.getMateria().getNombre()
                        break
            
            if flag:
                estudianteElegido.setHorario(horarioAMostrar)
                estudianteElegido.desmatricularMaterias()
                for pGrupo in horarioAMostrar.getGrupoContenidos():
                    horarioGenerado.matricularMateriaParte4(estudianteElegido, pGrupo)
                mesExito="Horario asignado con éxito al estudiante " + estudianteElegido.getNombre()
                messagebox.showinfo("",mesExito)
                self.destroy()
                RecoleccionDat(ventana)
            else:
                estudianteElegido.setHorario(tempHorario)
                mesFrac="No es posible asignar el horario, el estudiante " + estudianteElegido.getNombre() + " no cumple los Pre-requisitos"
                if mens:
                    mesFrac+=" o ya vio y aprobó una materia, dicha materia puede ser: " + nMateria
                
                messagebox.showinfo("",mesFrac)

            


            
        
        bottDescartar = Button(fraBotones,text="Descartar",command=descartar)
        bottDescartar.pack(side="left",padx=10,pady=1)        

        bottConservar = Button(fraBotones,text="Asignar",command=asignar)
        bottConservar.pack(side="right",padx=10,pady=1)

        combo3 = ttk.Combobox(fraBotones, textvariable=StringVar(value="Estudiantes habilitados"), values=listaNombresEstu, state="readonly")
        combo3.pack(side="right", fill="x", pady="1", padx="1")
        
        textAsig = Label(fraBotones,text="Conservar y asignar a: ")
        textAsig.pack(side="right",padx=10,pady=1)

    @classmethod
    def matricularMateriaParte4(cls,estudiante,grupo):
        materiasInscritas = estudiante.getMaterias().copy()
        materiasInscritas.append(grupo.getMateria())
        grupo.agregarEstudiante(estudiante)
        grupo.getMateria().setCupos(grupo.getMateria().getCupos() - 1)
        grupo.setCupos(grupo.getCupos() - 1)
        gruposInscritos = estudiante.getGrupos().copy()
        gruposInscritos.append(grupo)
        estudiante.setGrupos(gruposInscritos)
        estudiante.setCreditos(estudiante.getCreditos() + grupo.getMateria().getCreditos())
        estudiante.setMaterias(materiasInscritas)

        
        
