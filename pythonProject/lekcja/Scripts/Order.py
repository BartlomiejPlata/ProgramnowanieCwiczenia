from Employee import Employee
from Book import Book

class Order(Employee):
    def __init__(self, employee: Employee, student , books: Book, order_date):
        employee.__init__(self)
        books.__init__(self)
        self.student = student
        self.order_date = order_date

    def __str__(self):
        return "Pracownik" + employee + f" albo student {self.student}, kupił książke" + books + "którą zamówił " + self.order_date


pracownik = Employee("Jacek", "Kowalski", '14-12-2021', '13-02.1999', "Katowice", "ul.Czekoladowa", "34-343", '736453628')


order1 = Order(pracownik, student, )