from Property import Property

class House(Property):
    def __init__(self, plot: int, property: Property):
        self.plot = plot
        self.property = prop

    def __str__(self):
        return f"Dom w {self.property.area} z {self.property.rooms} pokojami ,  o powierzchni działki {self.plot}, kosztuje {self.property.price}"


prop = Property("przedmieście",3, 200000,'ul, Koralowa 10, Katowice'  )
house = House(160, prop)

print(house)