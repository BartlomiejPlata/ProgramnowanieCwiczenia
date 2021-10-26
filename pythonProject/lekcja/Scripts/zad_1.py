print("\nzadanie 1")

class Student:
    def __init__(self, name, marks ):
        self.name = name
        self.marks = marks

    def is_passed(self)-> bool:
        if (self.marks > 50):
            return True
        else:
            return False



Student1 = Student("Bartek", 66)
Student2 = Student("Roman", 40)

print(Student1.is_passed())
print(Student2.is_passed())







