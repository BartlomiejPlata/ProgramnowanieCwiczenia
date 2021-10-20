print("\nzadanie 1")
def my_function(name: str, surname: str) -> str:
    return (f"Cześć {name} {surname}")

wynik = my_function("Bartek", "Plata")
print(wynik)

print("\nzadanie 2")

def mnozenie(liczba1: int, liczba2: int)->int:
    return (liczba1*liczba2)

x = mnozenie(44,12)
print(x)

print("\nzadanie 3")

def liczby_parzyste(liczba: int) -> bool:
    if liczba % 2 != 0:
        return False
    else:
        return True


y= liczby_parzyste(3)
if y == True:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")

print("\nzadanie 4")
def sprawdz_sume(x: int, y: int, z:int)->bool:
    if x+y>=z:
        return True
    else:
        return False

x = sprawdz_sume(3,6,67)
print(x)

print("\nzadanie 5")
def sprawdz_liste(lista: list, liczba: int):
    check = 0
    for x in lista:
        if x == liczba:
            check = 1
            print(f"liczba {x} znajduje się na liśćie")

    if check != 1:
        print(f"Nie ma liczby {liczba} na liście")

x = sprawdz_liste([3,5,1,5,4],4)

print("\nzadanie 6")

def zlacz_listy(lista1: list, lista2: list)->list:
    connectlist = list(set(lista1+lista2))
    new_list = [x**3 for x in connectlist]

    return (new_list)


x = zlacz_listy([1,2,3,4], [3,4,5,6])
print(f"nowa lista: {x}")

print("\nzadanie 7")
