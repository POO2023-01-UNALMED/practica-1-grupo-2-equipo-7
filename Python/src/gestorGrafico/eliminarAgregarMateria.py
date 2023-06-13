from tkinter import *
from FieldFrame import FieldFrame

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

class agregarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Agregar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para crear\n una nueva materia que será registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

        criterios = ["Nombre", "Código", "Descripción", "Créditos", "Facultad", "Prerrequisitos"]
        formulario = FieldFrame(self, "Criterio", criterios, "Valor", None)
        formulario.pack()

class eliminarMateria(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Eliminar Materia", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n una materia que esté registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

class agregarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Agregar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para agregar\n un grupo a una materia registrada en el sistema.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

class eliminarGrupo(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        titulo = Label(self, text="Eliminar Grupo", font=("Arial", 14))
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para eliminar\n un grupo que pertenezca a una materia registrada.")
        descripcion = Label(self, text=texto, font=("Arial", 10))
        descripcion.pack(anchor="n", pady=20)

vent = Tk()
vent.title("Szs")
vent.geometry("600x350")

freim = eliminarAgregarMateria(vent)
freim.pack()
vent.mainloop()