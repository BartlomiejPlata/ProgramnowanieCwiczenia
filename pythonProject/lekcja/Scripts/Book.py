from  Library import Library

class Book(Library):
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka pochodzi z blibioteki {self.library}, \nzostała opublikowana {self.publication_date}, jej autorem jest " \
               f"{self.author_surname} {self.author_surname} , i ma {self.number_of_pages} stron"



