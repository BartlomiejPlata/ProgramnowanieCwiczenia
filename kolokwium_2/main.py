from osoba import Osoba
from Dietetyk import Dietetyk
from Pacjent import Pacjent
from Dieta import Dieta
from Zamowienie import Zamowienie


dieta1 = Dieta("Masa", 3000, 300, "mięsna")
dieta2 = Dieta("jedz i chudnij", 1700, 200, "wegańska")
pacjent1 = Pacjent("Natalia", "Nowak", "Katowice, ul.Kamienna 12", 123456765 , 99999999999)
dietetyk1 = Dietetyk("Roman", "Duda", "Katowice, ul.Brzozowa 12", 12343212 , 4.1)

zamowienie = Zamowienie()

zamowienie.id = 1
zamowienie.diety = [dieta1, dieta2]
zamowienie.pacjent = pacjent1
zamowienie.dietetyk = dietetyk1

print(zamowienie)