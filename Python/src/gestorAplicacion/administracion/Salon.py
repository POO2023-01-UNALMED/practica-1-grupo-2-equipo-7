from gestorAplicacion.administracion.Horario import Horario


class Salon:
    _salones = []

    def __init__(self, lugar, aforo):
        self._lugar = lugar
        self._aforo = aforo
        self._horario = Horario()  # no estoy segura de como hacer eso aca
        Salon._salones.append(self)

    # METODOS

    @classmethod
    def mostrarSalones(cls):
        retorno = ""
        i = 1
        for salon in Salon._salones:
            i += 1
            retorno += str(i) + ". " + salon._lugar + ".\n"
        return retorno
    
    @classmethod
    def nombresSalones(cls):
        nombres = []
        for salon in Salon._salones:
            nombres.append(salon.getLugar())
        return nombres
    
    @classmethod
    def encontrarSalon(cls, salon):
        for s in Salon._salones:
            if s.getLugar()==salon:
                return s

    # Setters y Getters

    def getLugar(self):
        return self._lugar

    def setLugar(self, lugar):
        self._lugar = lugar

    def getAforo(self):
        return self._aforo

    def setLugar(self, aforo):
        self._aforo = aforo

    def getLugar(self):
        return self._lugar

    def setLugar(self, lugar):
        self._lugar = lugar

    def getHorario(self):
        return self._horario

    def setHorario(self, horario):
        self._horario = horario

    @classmethod
    def getSalones(cls):
        return cls._salones

    @classmethod
    def setSalones(cls, salones):
        cls._salones = salones
