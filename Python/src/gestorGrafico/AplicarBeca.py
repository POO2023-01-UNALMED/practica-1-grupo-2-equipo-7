from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorAplicacion.usuario.Estudiante import Estudiante
from gestorAplicacion.usuario.Coordinador import Coordinador
from excepciones.ErrorManejo import *
from gestorGrafico.FieldFrame import FieldFrame

class AplicarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)
    
        estudiantesBeneficiados = []

        def nombresEst(estudiantes):
            listaNombres = []
            for estudiante in estudiantes:
                listaNombres.append(estudiante.getNombre())
            return listaNombres
        
        def asigBeca():
            try:
                confirmar = messagebox.askokcancel("Confirmar acción", f"¿Está seguro que aplicar la beca: {comboBecas.get()} al estudiante: {comboEst.get()} del sistema?\n Esta acción será permanente.")
                if confirmar:
                    estA = ""
                    becA = ""

                    for est in Estudiante.getEstudiantes():
                        if str(comboEst.get()) == est.getNombre():
                            estA = est
                            break
                    for bec in Beca.getBecas():
                        if str(comboBecas.get()) == bec.getConvenio():
                            becA = bec
                            break
                    
                    if (estA.getNombre()) in estudiantesBeneficiados:
                        messagebox.showerror("Error", "El estudiante ya ha aplicado exitosamente a una beca, no puede aplicar a otra durante el semestre académico actual.")
                    
                    if (becA.getCupos()) == 0:
                        messagebox.showerror("Error", "La beca seleccionada no cuenta con más cupos para este semestre.")
                    else:
                        if Coordinador.candidatoABeca(estA, becA):
                            becA.setCupos(becA.getCupos()-1)
                            estudiantesBeneficiados.append(estA.getNombre())
                            estA.setSueldo(estA.getSueldo() + becA.getAyudaEconomica())
                            messagebox.showinfo("Beca aplicada", f"El estudiante {estA.getNombre()} cumple con los requisitos de la beca: {becA.getConvenio()} y se le ha sido cargada la ayuda económica correspondiente.")
                        else:
                            messagebox.showerror("Error", f"El estudiante {estA.getNombre()} no cumple con los requisitos de la beca: {becA.getConvenio()}. Lo invitamos a intentar nuevamente el próximo semestre.")
            
            except:
                messagebox.showerror("Error", "Debe seleccionar una beca y un estudiante de los listados para poder continuar.")
                    
    
        titulo = Label(self, text="Aplicar Beca a Estudiante", bg="#cedae0", foreground="#085870", font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")

        textoDesc = ("A continuación, deberá seleccionar de las listas qué estudiante quiere postular y a qué beca quiere que aplique,\n en caso de cumplir con los requisitos, la ayuda económica será asignada y será informado.")
        descripcion = Label(self, text=textoDesc, bg="#cedae0", font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        aplicandoFrame = Frame(self,bg="#cedae0")
        aplicandoFrame.pack()

        becaTit = Label(aplicandoFrame, text = "Becas existentes", bg="#cedae0", font=("Arial", 11, "bold"))
        becaTit.grid(row=0, column=0, padx=10, pady=10)
        estTit = Label(aplicandoFrame, text = "Estudiantes matriculados", bg="#cedae0", font=("Arial", 11, "bold"))
        estTit.grid(row=1, column=0, padx=10, pady=10)

        becasE = Beca.listaBecas()
        textoDefault = StringVar(aplicandoFrame, value= "Seleccione una beca")
        comboBecas = ttk.Combobox(aplicandoFrame, values=becasE, textvariable= textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)

        estE = nombresEst(Estudiante.getEstudiantes())
        textoPre = StringVar(aplicandoFrame, value= "Seleccione un estudiante")
        comboEst = ttk.Combobox(aplicandoFrame, values=estE, textvariable= textoPre)
        comboEst.grid(row=1, column=1, padx=10, pady=10)

        boton = Button(self, text="Aplicar Beca", command=asigBeca, font=("Arial", 11, "bold"), fg="white", bg="#085870")
        boton.pack()
