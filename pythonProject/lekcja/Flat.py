from Property import Property

class Flat(Property):
    def __init__(self, floor, property: Property):
        self.floor = floor
        self.property = property


    def __str__(self):
        return f"Mieszkanie w {self.property.area} z {self.property.rooms},  na {self.floor} piętrze, kosztuje {self.property.price}"





prop = Property("przedmieście",3, 200000,'ul, Koralowa 10, Katowice'  )
    #house = House(160)

flat = Flat(4, prop)
print(flat)


