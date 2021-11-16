import Magazine.utils

class Product:
    def __init__(self, nazwa, cena, opakowanie, jednostkaMiary, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.opakowanie = opakowanie
        self.jednostkaMiary = jednostkaMiary
        self.kategoria = kategoria

    @property
    def _nazwa(self):
        return self._nazwa

    @property
    def _cena(self):
        return self._cena
    @property
    def _opakowanie(self):
        return self._opakowanie
    @property
    def _jednostkaMiary(self):
        return self._jednostkaMiary
    @property
    def _kategoria(self):
        return self._kategoria