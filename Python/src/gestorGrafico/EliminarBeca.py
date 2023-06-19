from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from gestorAplicacion.administracion.Beca import Beca
from gestorGrafico.FieldFrame import FieldFrame

class EliminarBeca(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#cedae0")

        def confEliminar():
            quest = messagebox.askokcancel("Confirmar acción", f"¿Está seguro que desea eliminar la beca {comboBecas.get()} del sistema?\n Esta acción será permanente.")
            if quest:
                bec = Beca.buscandoBeca(str(comboBecas.get()))
                try:
                    Beca.eliminarBeca(bec)
                    messagebox.showinfo("Beca eliminada", f"La beca {comboBecas.get()} ha sido eliminada con éxito del sistema")
                except:
                    messagebox.showerror("Error", "Debe seleccionar una beca del listado para poder continuar.")

                

        titulo = Label(self, text="Eliminar Beca", bg="#cedae0", foreground="#085870", font=("Helvetica", 14, "bold"))
        titulo.pack(side="top", anchor="c")

        textoDesc = ("A continuación, deberá seleccionar de la lista de becas existentes\n cuál de estas desea eliminar.")
        descripcion = Label(self, text=textoDesc, bg="#cedae0", font=("Arial", 11), fg="#110433")
        descripcion.pack(anchor="n", pady=20)

        becaFrame = Frame(self,bg="#cedae0")
        becaFrame.pack()

        becaTit = Label(becaFrame, text = "Becas existentes", bg="#cedae0", font=("Arial", 11, "bold"))
        becaTit.grid(row=0, column=0, padx=10, pady=10)

        becasE = Beca.listaBecas()
        textoDefault = StringVar(becaFrame, value= "Seleccione una beca")
        comboBecas = ttk.Combobox(becaFrame, values=becasE, textvariable= textoDefault)
        comboBecas.grid(row=0, column=1, padx=10, pady=10)
        
        boton = Button(self, text="Eliminar", command=confEliminar, font=("Arial", 11), fg="white", bg="#085870")
        boton.pack()
