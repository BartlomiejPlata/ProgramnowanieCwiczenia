from  library import Library

class Book(Library):
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
