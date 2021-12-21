class Osoba:
    def __init__(self, name: str, last_name: str, address: str, contact: str):
        self._contact = contact
        self._address = address
        self._last_name = last_name
        self._name = name

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

    def __str__(self):
        return f" Imie: {self.name}  Nazwisko: {self.last_name} adres: {self.address}  kontakt: {self.contact} "


