class Beca:
    _becas = []

    def __init__(
        self,
        cupos,
        convenio,
        promedioRequerido,
        avanceRequerido,
        estratoMinimo,
        creditosInscritosRequeridos,
        ayudaEconomica,
        necesitaRecomendacion,
    ):
        self._cupos = cupos
        self._convenio = convenio
        self._promedioRequerido = promedioRequerido
        self._avanceRequerido = avanceRequerido
        self._estratoMinimo = estratoMinimo
        self._creditosInscritosRequeridos = creditosInscritosRequeridos
        self._ayudaEconomica = ayudaEconomica
        self._necesitaRecomendacion = necesitaRecomendacion
        Beca._becas.append(self)

    # METODOS

    @classmethod
    def eliminarBeca(cls, beca):
        cls._becas.remove(beca)
    
    @staticmethod
    def listaBecas():
        lista = []
        for beca in Beca._becas:
            lista.append(beca.getConvenio())
        return lista
    
    @staticmethod
    def buscandoBeca(becaSel):
        beca = None
        for becas in Beca._becas:
            if becas.getConvenio() == becaSel:
                beca = becas
        return beca


    # Setters y Getters

    def getCupos(self):
        return self._cupos

    def setCupos(self, nuevos_cupos):
        self._cupos = nuevos_cupos

    def getConvenio(self):
        return self._convenio

    def setConvenio(self, nuevo_convenio):
        self._convenio = nuevo_convenio

    def getPromedioRequerido(self):
        return self._promedioRequerido

    def setPromedioRequerido(self, nuevo_promedio):
        self._promedioRequerido = nuevo_promedio

    def getAvanceRequerido(self):
        return self._avanceRequerido

    def setAvanceRequerido(self, nuevo_avance):
        self._avanceRequerido = nuevo_avance

    def getEstratoMinimo(self):
        return self._estratoMinimo

    def setEstratoMinimo(self, nuevo_estrato):
        self._estratoMinimo = nuevo_estrato

    def getCreditosInscritosRequeridos(self):
        return self._creditosInscritosRequeridos

    def setCreditosInscritosRequeridos(self, nuevos_creditos):
        self._creditosInscritosRequeridos = nuevos_creditos

    def getAyudaEconomica(self):
        return self._ayudaEconomica

    def setAyudaEconomica(self, nueva_ayuda):
        self._ayudaEconomica = nueva_ayuda

    def getNecesitaRecomendacion(self):
        return self._necesitaRecomendacion

    def setNecesitaRecomendacion(self, necesita_recomendacion):
        self._necesitaRecomendacion = necesita_recomendacion

    @classmethod
    def getBecas(cls):
        return cls._becas

    @classmethod
    def setBecas(cls, becas):
        cls._becas = becas
