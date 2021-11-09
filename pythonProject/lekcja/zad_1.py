class Magazyn:
    def __init__(self, city, street, owner, size, number_of_employee):
        self.city = city
        self.street = street
        self.owner = owner
        self.size = size
        self. number_of_employee = number_of_employee

    @property
    def _city(self):
        return self._city

    @city.setter
    def _city(self, nazwa):
        self._city = nazwa

    @property
    def _street(self):
        return self._street

    @street.setter
    def _street(self, nazwa):
        self._street = nazwa

    @property
    def _owner(self):
        return self._owner

    @owner.setter
    def _marka(self, nazwa):
        self._owner = nazwa

    @property
    def _size(self):
        return self._size

    @owner.setter
    def _size(self, nazwa):
        self._size = nazwa

    def __str__(self):
        return f"Magazyn znajduje się w {self.city} na {self.street}. Jest to {self.size} magazyn, " \
               f"jego właściceleme jest {self.owner} i zatrudnia {self.number_of_employee} pracowników  "

class Produkt:
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


    def __str__(self):
        return f"{self.nazwa} jest w cenie {self.cena}, jest wyrażony w {self._jednostkaMiary} i jest zapakowany w {self.opakowanie}" \
               f"Produkt ten jest z kategori {self.kategoria} "




class Człowiek :
    def __init__(self, first_name, last_name, birth_date, addres, ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, nazwa):
        self.first_name = nazwa

    @property
    def last_name(self):
        return self.first_name

    @first_name.setter
    def last_name(self, nazwa):
        self.last_name = nazwa

    @property
    def birth_date(self):
        return self.first_name

    @birth_date.setter
    def birth_date(self, nazwa):
        self.birth_date = nazwa

    @property
    def adress(self):
        return self.first_name

    @adress.setter
    def adress(self, nazwa):
        self.adress = nazwa









class KlientDetaliczny (Człowiek):
    def __init__(self, czlowiek , NIP):
        Czlowiek.__init__(self)
        self.NIP = NIP

    @property
    def NIP(self):
        return self.NIP

    @NIP.setter
    def NIP(self, nazwa):
        self.NIP = nazwa

    def __str__(self):
        return f" To jest klient detaliczny {self.first_name}, {self.last_name}, identyfikuje się numerem NIP: {self.NIP}"

class KlientBiznesowy(Człowiek):
    def __init__(self, , nazwaFirmy):
        Czlowiek.__init__(self)
        self.nazwaFirmy = nazwaFirmy

    @property
    def _Nazwafirmy(self):
        return self.NIP

    @Nazwafirmy.setter
    def _Nazwafirmy(self, nazwa):
        self._Nazwafirmy = nazwa

    def __str__(self):
        return f" To jest klient biznesowy {self.first_name}, {self.last_name}, reprezentuje on firmę : {self.NazwaFirmy}"



class Zamowienie (Magazyn, KlientDetaliczny, Produkt):
    def __init__(self, magazyn: Magazyn, produkt: Produkt, klient: klientDetaliczny, data_zamowienia, ilosc):
        Magazyn.__init__(self)
        Produkt.__init__(self)
        KlientDetaliczny.__init__(self)
        self.produkt = produkt
        self.magazyn = magazyn
        self.data_zamowienia = data_zamowienia
        self. ilosc = ilosc


    def wartosc() -> float:
        wartosc = round(Produkt.cena * self.ilosc)

    def adresDostawy(adress)->str:
        return f"adres dostawy {self.adress}"


prod1 = Produkt("sok",6.50, "karton","litr", "napoje")
mag1 = Magazyn("Katowice", "szkolna", "Tymbark", "Duzy", 14)
per1 = Człowiek("Jacek","Nowak", )
klient = KlientDetaliczny(per1, '98765432123')

zam = Zamowienie(mag1,prod1,klient, "13.11.2021",10)

print(zam)


#zabrakło mi czasu i dlatego wiekszość jest niedokończona,