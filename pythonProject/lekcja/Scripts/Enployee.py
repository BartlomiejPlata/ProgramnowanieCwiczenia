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



pracownik = Employee("Jacek", "Kowalski", '14-12-2021', '13-02.1999', "Katowice", "ul.Czekoladowa", "34-343", '736453628')
pracownik2 = Employee("Monika", "Kot", '14-12-2021', '13-02.1999', "Poznań ", "ul.Malinowa", "34-343", '736453628')
pracownik3 = Employee("Adam", "Wilk", '14-12-2021', '13-02.1999', "Toruń", "ul.Czekoladowa", "34-343", '736453628')
print(pracownik, pracownik2, pracownik3)