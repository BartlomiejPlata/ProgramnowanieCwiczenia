class Employee:
    def __init__(self, first_name, last_name,hire_date,birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"\nImie: {self.first_name}, Nazwisko: {self.last_name}, Data zatrunienia: {self.hire_date}, data urodzenia: {self.birth_date} " \
               f"miasto {self.city}, ulica: {self.street}, kod pocztowy, {self.zip_code}, telefon: {self.phone}"



