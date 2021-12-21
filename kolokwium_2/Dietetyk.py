from osoba import Osoba


class Dietetyk(Osoba):
    def __init__(self, name: str, last_name: str, address: str, contact: str, ocena_google: str):
        super().__init__(name, last_name, address, contact)
        self._ocena_google = ocena_google

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
    def ocena_google(self):
        return self._ocena_google

    def __str__(self):
        return super().__str__() + f'  Ocena na Googlu: {self._ocena_google}'
