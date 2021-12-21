from osoba import Osoba
from Dietetyk import Dietetyk
from Pacjent import Pacjent
from Dieta import Dieta


class Zamowienie:
    _id: int
    _diety: list
    _dietetyk: Dietetyk
    _pacjent: Pacjent

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def diety(self):
        return self._diety

    @diety.setter
    def diety(self, value):
        self._diety = value

    @property
    def dietetyk(self):
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value):
        self._dietetyk = value

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value):
        self._pacjent = value

    def obliczWartosc(self):
        wartosc = 0
        for d in self.diety:
            wartosc += d._cena
        return round(wartosc, 2)

    def liczbaKalori(self):
        kalorie = 0
        for d in self.diety:
            kalorie += d._l_kalori
        return round(kalorie, 2)

    def __str__(self):
        return f"""
                    Zamowienie nr: {self._id}
                    Pacjent: {self._pacjent}           
                    Dietetyk: {self._dietetyk}
                    Wartość zamowienia: {self.obliczWartosc()} zł 
                    Liczba kalorii: {self.liczbaKalori()} kcal
                     """
