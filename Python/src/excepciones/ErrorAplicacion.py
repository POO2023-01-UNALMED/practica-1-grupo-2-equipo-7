class ErrorAplicacion(Exception):
    def __init__(self, error):
        self._error = "Manejo de errores de la Aplicación: " + error
    
    def mostrarMensaje(self):
        return self._error
      