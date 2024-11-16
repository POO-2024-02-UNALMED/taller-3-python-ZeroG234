class Marca:
    def __int__(self, nombre: str):
        self._nombre = nombre

    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getNombre(self):
        return self._nombre