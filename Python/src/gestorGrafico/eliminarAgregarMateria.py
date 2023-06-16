from tkinter import *
from gestorGrafico.FieldFrame import FieldFrame
from gestorGrafico.agregarMateria import agregarMateria
from gestorGrafico.eliminarMateria import eliminarMateria
from gestorGrafico.agregarGrupo import agregarGrupo
from gestorGrafico.eliminarGrupo import eliminarGrupo

class eliminarAgregarMateria(Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

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

        titulo = Label(self, text="Agregar/Eliminar Materia/Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("Esta funcionalidad permite:\n1. Agregar una nueva materia al sistema. 3. Agregar un grupo a una materia existente."+
                 "\n2. Eliminar una materia existente del sistema. 4. Eliminar un grupo existente en alguna materia.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        opciones = Frame(self)
        opciones.pack()

        agMat = Button(opciones, text="Agregar Materia", command=agMateria)
        agMat.pack(padx=20, pady=10)
        elMat = Button(opciones, text="Eliminar Materia", command=elMateria)
        elMat.pack(padx=20, pady=10)
        agGrup = Button(opciones, text="Agregar Grupo", command=agGrupo)
        agGrup.pack(padx=20, pady=10)
        elGrup = Button(opciones, text="Eliminar Grupo", command=elGrupo)
        elGrup.pack(padx=20, pady=10)

# vent = Tk()
# vent.title("Szs")
# vent.geometry("600x350")

# freim = eliminarAgregarMateria(vent)
# freim.pack()
# vent.mainloop()