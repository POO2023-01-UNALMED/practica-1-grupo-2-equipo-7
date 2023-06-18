from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from gestorAplicacion.usuario.Usuario import Usuario
from gestorGrafico.ventPrincipal import VentPrincipal

class VentLog(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Matricula de Materias")
        self.resizable(0,0)
        self.geometry("865x460")

        frame = Frame(self, width=400, height=200)
        frame.pack(expand=True)

        def mostrarContraseña():
            if entrada2.cget('show') == '*':
                entrada2.config(show='')
            else:
                entrada2.config(show='*')

        def limpiar():
            entrada1.delete(0, last= END)
            entrada2.delete(0, last= END)

        def cambiarVentana():
            self.destroy()
            VentPrincipal()

        def verificar():
            exist = False
            pw = False
            
            for usuario in Usuario.getUsuariosTotales():
                if usuario.getId() == int(entrada1.get()):
                    exist = True
                    break

            if exist:
                if str(usuario.getPw()) == entrada2.get():
                    pw = True
                else:
                    return messagebox.showwarning("Error", "La contrasena es incorrecta. Intentelo nuevamente")
            else:
                return messagebox.showwarning("Error", "El id ingresado no corresponde a ningún usuario")
            if pw:
                cambiarVentana()
             
        usuar = Label(frame,text="Usuario")
        entrada1 = Entry(frame)
        cont = Label(frame,text="Contraseña")
        entrada2 = Entry(frame, show="*")
        boton_ingresar = Button(frame, text="Iniciar Sesion", command= verificar)
        boton_limpiar = Button(frame, text="Limpiar", command= limpiar)
        revisar = Checkbutton(frame, text="Mostrar contraseña", command= mostrarContraseña)        
        
        usuar.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        entrada1.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
        cont.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        entrada2.grid(row=1,column=1,columnspan=2,padx=10,pady=10) 
        boton_ingresar.grid(row=3,column=0, columnspan=2, padx=10,pady=10,sticky="w")
        boton_limpiar.grid(row=3,column=1, columnspan=2, padx=10,pady=10,sticky="w")
        revisar.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        
        self.mainloop()
        
    
        
       
        