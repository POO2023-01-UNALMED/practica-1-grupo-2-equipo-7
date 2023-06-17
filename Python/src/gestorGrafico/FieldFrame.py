from tkinter import *

class FieldFrame(Frame):
    def __init__(self, ventana, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(ventana)
        self._criterios = criterios
        self._datos = []

        tituloC = Label(self, text=tituloCriterios, font=("Arial", 10))
        tituloC.grid(row=0, column=0, padx=10, pady=10)

        tituloV = Label(self, text=tituloValores, font=("Arial", 10))
        tituloV.grid(row=0, column=1, padx=10, pady=10)

        for i in range(1, len(criterios)+1):
            lCriterio = Label(self, text=criterios[i-1], font=("Arial", 10))
            lCriterio.grid(row=i, column=0, padx=10, pady=10)

            valor = Entry(self, font=("Arial", 10))

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