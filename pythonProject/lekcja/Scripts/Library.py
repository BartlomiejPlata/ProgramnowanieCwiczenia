class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Miasto: {self.city} \nulica:  {self.street} \nkod pocztowy: {self.zip_code} \ngodziny otwarcia: {self.open_hours} \ntelefon: {self.phone}'


lib1 = Library("Warszawa", "ul. Sezamkowa", "12-345", "8:00 - 19:00", "12345677422")
lib2 = Library("Katowice", "ul. Sokolska", "12-345", "8:00 - 19:00", "33333333333")
print(lib1, lib2)