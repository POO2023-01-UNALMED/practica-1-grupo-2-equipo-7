from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.agregarMateria import agregarMateria
from gestorGrafico.eliminarMateria import eliminarMateria
from gestorGrafico.agregarGrupo import agregarGrupo
from gestorGrafico.eliminarGrupo import eliminarGrupo


class EliminarAgregarMateria(Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")

        def agMateria():
            self.pack_forget()
            agM = agregarMateria(ventana)
            agM.pack()

        def elMateria():
            self.pack_forget()
            elM = eliminarMateria(ventana)
            elM.pack()

        def agGrupo():
            self.pack_forget()
            agG = agregarGrupo(ventana)
            agG.pack()

        def elGrupo():
            self.pack_forget()
            elM = eliminarGrupo(ventana)
            elM.pack()

        titulo = Label(self, text="Agregar/Eliminar Materia/Grupo", font=("Arial", 14), fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c")

        texto = ("Esta funcionalidad permite:\n1. Agregar una nueva materia al sistema. 3. Agregar un grupo a una materia existente."+
                 "\n2. Eliminar una materia existente del sistema. 4. Eliminar un grupo existente en alguna materia.")
        descripcion = Label(self, text=texto, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20)

        opciones = Frame(self, bg="#cedae0")
        opciones.pack()

        agMat = Button(opciones, text="Agregar Materia", font=("Arial", 11), command=agMateria, fg="white", bg="#085870")
        agMat.pack(padx=20, pady=10)
        elMat = Button(opciones, text="Eliminar Materia", font=("Arial", 11), command=elMateria, fg="white", bg="#085870")
        elMat.pack(padx=20, pady=10)
        agGrup = Button(opciones, text="Agregar Grupo", font=("Arial", 11), command=agGrupo, fg="white", bg="#085870")
        agGrup.pack(padx=20, pady=10)
        elGrup = Button(opciones, text="Eliminar Grupo", font=("Arial", 11), command=elGrupo, fg="white", bg="#085870")
        elGrup.pack(padx=20, pady=10)

#vent = Tk()
#vent.title("Szs")
#vent.geometry("600x350")

#eliminarAgregarMateria(vent).pack()
#vent.mainloop()
