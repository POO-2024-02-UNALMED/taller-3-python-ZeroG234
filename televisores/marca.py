class Marca:
    def __init__(self, nombre: str = ''):
        self._nombre = nombre

    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre

    def getNombre(self):
        return self._nombre