from tkinter import *

class FieldFrame(Frame):
    def __init__(self, ventana, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(ventana)
        self._criterios = criterios
        self._datos = []
        self._entrysCriterios = []

        tituloC = Label(self, text=tituloCriterios, font=("Arial", 11))
        tituloC.grid(row=0, column=0, padx=10, pady=8)

        tituloV = Label(self, text=tituloValores, font=("Arial", 11))
        tituloV.grid(row=0, column=1, padx=10, pady=8)

        for i in range(1, len(criterios)+1):
            lCriterio = Label(self, text=criterios[i-1], font=("Arial", 11))
            lCriterio.grid(row=i, column=0, padx=10, pady=8)

            valor = Entry(self, font=("Arial", 11))
            self._entrysCriterios.append(valor)

            if valores != None:
                valor.insert(0, valores[i-1])

            if habilitado != None:
                if criterios[i-1] in habilitado:
                    valor.configure(state = "disabled")

            valor.grid(row=i, column=1)

            self._datos.append(valor)


    def getValue(self, criterio):
        i = self._criterios.index(criterio)
        return self._datos[i].get()
    
    def limpiarValues(self):
        for entry in self._entrysCriterios:
            entry.delete(0, last= END)
           
    def crearBotones(self, comando1, texto = "Aceptar", Pady = 50, Column= 0, Padx = 0):
        return Button(self, text=texto, foreground="white",background="#085870",font=("Helvetica", 11), command=comando1).grid(padx = Padx, pady = Pady, column = Column, row = len(self._datos)+1)