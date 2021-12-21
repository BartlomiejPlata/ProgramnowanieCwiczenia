from osoba import Osoba


class Pacjent(Osoba):
    def __init__(self, name: str, last_name: str, address: str, contact: str, pesel: str):
        super().__init__(name, last_name, address, contact)
        self._pesel = pesel

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def address(self):
        return self._address

    @property
    def contact(self):
        return self._contact

    @property
    def pesel(self):
        return self._pesel

    def __str__(self):
        return super().__str__() + f'  pesel: {self._pesel}'
