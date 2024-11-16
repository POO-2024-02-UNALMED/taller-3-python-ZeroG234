from .tv import TV

class Control:
    def __init__(self, tv: TV = None):
        self._tv = tv

    def turnOn(self):
        if isinstance(self._tv, TV): self._TV.turnOn()

    def turnOff(self):
        if isinstance(self._tv, TV): self._TV.turnOff()
    
    def canalUp(self):
        if isinstance(self._tv, TV): self._TV.canalUp()

    def canalDown(self):
        if isinstance(self._tv, TV): self._TV.canalDown()

    def volumenUp(self):
        if isinstance(self._tv, TV): self._TV.volumenUp()

    def volumenDown(self):
        if isinstance(self._TV, TV): self._TV.volumenDown()

    def setCanal(self, nuevoCanal: int):
        if isinstance(self._tv, TV): self._TV.setCanal(nuevoCanal)

    def setVolumen(self, nuevoVolumen: int):
        if isinstance(self._tv, TV): self._TV.setVolumen(nuevoVolumen)

    def enlazar(self, nuevoTV: TV):
        if isinstance(nuevoTV, TV):    
            self._tv = nuevoTV
            nuevoTV.setControl(self)

    def setTV(self, nuevoTV):
        self.enlazar(nuevoTV)

    def getTV(self):
        return self._tv