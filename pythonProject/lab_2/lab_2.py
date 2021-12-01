
#zad 2 
def list_printer(namelist):
    for name in namelist:
        print(name)

name_list  = ["Jasiu", "Zosia", "Jacek", "Tomek", "Roman"]

list_printer(name_list)

 #zad 2 b
'''
def number_adder(numberlist):
    new_list = []
    for number in numberlist:
        new_list.append(number * 2)
    print(f'Lista początkowa {numberlist}  lista po zmianach: {new_list}')

number_list = [1,2,3,4,5]

number_adder(number_list)

'''

'''
def number_adder(numberlist):
    new_list = [number * 2 for number in numberlist]

    print(f'Lista początkowa {numberlist}  lista po zmianach: {new_list}')


number_list = [7,2,3,54,5]

number_adder(number_list)
'''
# zad 3 c
'''
for number in range(10):
    if number%2 != 1:
        print(number)
'''
# zad 3 d
list = list(range(0,10))

i = 1
while i < len(list):
    print(list[i])
    i+=2
