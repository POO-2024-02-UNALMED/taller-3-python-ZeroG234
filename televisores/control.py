from .tv import TV

class Control:
    def __init__(self, tv: TV = None):
        self._tv = tv

    def turnOn(self):
        if isinstance(self._tv, TV): self._tv.turnOn()

    def turnOff(self):
        if isinstance(self._tv, TV): self._tv.turnOff()
    
    def canalUp(self):
        if isinstance(self._tv, TV): self._tv.canalUp()

    def canalDown(self):
        if isinstance(self._tv, TV): self._tv.canalDown()

    def volumenUp(self):
        if isinstance(self._tv, TV): self._tv.volumenUp()

    def volumenDown(self):
        if isinstance(self._tv, TV): self._tv.volumenDown()

    def setCanal(self, nuevoCanal: int):
        if isinstance(self._tv, TV): self._tv.setCanal(nuevoCanal)

    def setVolumen(self, nuevoVolumen: int):
        if isinstance(self._tv, TV): self._tv.setVolumen(nuevoVolumen)

    def enlazar(self, nuevoTV: TV):
        if isinstance(nuevoTV, TV):
            self._tv = nuevoTV
            nuevoTV.setControl(self)

    def setTv(self, nuevoTV):
        self.enlazar(nuevoTV)

    def getTv(self):
        return self._tv