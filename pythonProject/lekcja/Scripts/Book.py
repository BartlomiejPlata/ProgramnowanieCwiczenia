from  Library import Library

class Book(Library):
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = Library()
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka pochodzi z blibioteki {self.library}, została opublikowana {self.publication_date}, jej autorem jest" \
               f"{self.author_surname} {self.author_surname} , i ma {self.number_of_pages}"



lib1 = Library("Warszawa", "ul. Sezamkowa", "12-345", "8:00 - 19:00", "12345677422")
ksiazka = Book(lib1, "21.01.2011", "Janusz", "Nowak", 444)
print(ksiazka)