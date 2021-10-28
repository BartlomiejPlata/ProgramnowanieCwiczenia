from Employee import Employee
from Book import Book
from Library import Library
from zad_1 import Student

class Order(Employee, Student, Book):
    def __init__(self, employee: Employee, student , books: Book, order_date):
        self.employee = employee
        self.books = books
        self.student = student
        self.order_date = order_date

    def __str__(self):
        return f"Pracownik: {self.employee.first_name} {self.employee.last_name}  albo student {self.student.name}, kupił książke  autorstwa  {self.books.author_name}  {self.books.author_surname} którą zamówił   {self.order_date}"


pracownik = Employee("Jacek", "Kowalski", '14-12-2021', '13-02.1999', "Katowice", "ul.Czekoladowa", "34-343", '736453628')
pracownik2 = Employee("Monika", "Kot", '14-12-2021', '13-02.1999', "Poznań ", "ul.Malinowa", "34-343", '736453628')
pracownik3 = Employee("Adam", "Wilk", '14-12-2021', '13-02.1999', "Toruń", "ul.Czekoladowa", "34-343", '736453628')

lib1 = Library("Warszawa", "ul. Sezamkowa", "12-345", "8:00 - 19:00", "12345677422")
lib2 = Library("Katowice", "ul. Sokolska", "12-345", "8:00 - 19:00", "33333333333")

book1 = Book(lib1, "21.01.2011", "Janusz", "Nowak", 444)
book2 = Book(lib1, "21.01.2011", "Agam", "Gran", 444)
book3 = Book(lib1, "21.01.2011", "John", "Brawo", 444)
book4 = Book(lib1, "21.01.2011", "Janusz", "Nowak", 444)
book5 = Book(lib1, "21.01.2011", "Janusz", "Nowak", 444)

Student1 = Student("Bartek", 66)
Student2 = Student("Roman", 40)


order1 = Order(pracownik, Student1, book1 , '21.10.2021' )
order2 = Order(pracownik2, Student2, book4 , '26.11.2021' )


print(order1, '\n' ,order2)