class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date