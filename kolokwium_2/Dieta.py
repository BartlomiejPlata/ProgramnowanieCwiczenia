class Dieta:
    def __init__(self, nazwa: str, l_kalori: int, cena: int, rodzaj: str):
        self._rodzaj = rodzaj
        self._cena = cena
        self._l_kalori = l_kalori
        self._nazwa = nazwa

        @property
        def rodzaj(self):
            return self._rodzaj

        @property
        def l_kalori(self):
            return self._l_kalori

        @property
        def cena(self):
            return self._cena

        @property
        def rodzaj(self):
            return self._rodzaj

    def __str__(self):
        return f"nazwa: {self._nazwa}, rodzaj: {self._rodzaj} liczba kalori: {self._l_kalori} cena: {self._cena}"
