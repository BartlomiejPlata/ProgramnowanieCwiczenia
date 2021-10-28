

class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość znajduje się w {self.area}, posiada {self.rooms} pokoi  i znajduje się w {self.address}. Ksztuje {self.price}."


prop = Property("przedmieście", 3, 200000, 'ul, Koralowa 10, Katowice')
