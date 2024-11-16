from .marca import Marca

class TV:
    _numTV = 0

    def __init__(self, marca: Marca, estado: bool, canal: int = 1,
                 precio: int = 500, volumen: int = 1):
        self._marca   = marca
        self._estado  = estado
        self._canal   = canal
        self._precio  = precio
        self._volumen = volumen
        self._control = None
        TV._numTV += 1

    def setMarca(self, nuevaMarca: Marca):
        self._marca = nuevaMarca

    def getMarca(self):
        return self._marca

    def setCanal(self, nuevoCanal: int):
        if self._estado and 1 <= nuevoCanal <= 120:
            self._canal = nuevoCanal

    def getCanal(self):
        return self._canal

    def setPrecio(self, nuevoPrecio: int):
        self._precio = nuevoPrecio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, nuevoVolumen: int):
        if self._estado and 0 <= nuevoVolumen <= 7:
            self._volumen = nuevoVolumen

    def getVolumen(self):
        return self._volumen

    def setControl(self, nuevoControl):
        self._control = nuevoControl

    def getControl(self):
        return self._control

    @classmethod
    def setNumTV(cls, cantidadTV: int):
        cls._numTV = cantidadTV

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def IO(self):
        self._estado = not self._estado

    def turnOn(self):
        if not self._estado: self.IO()

    def turnOff(self):
        if self._estado: self.IO()

    def getEstado(self):
        return self._estado

    def canalUp(self):
        self.setCanal(self.getCanal() + 1)

    def canalDown(self):
        self.setCanal(self.getCanal() - 1)

    def volumenUp(self):
        self.setVolumen(self.getVolumen() + 1)

    def volumenDown(self):
        self.setVolumen(self.getVolumen() - 1)