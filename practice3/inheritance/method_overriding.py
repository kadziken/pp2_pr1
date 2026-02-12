# Переопределение метода родителя

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def full_name(self):  # override
        return f"Student: {self.firstname} {self.lastname}"

s1 = Student("John", "Doe")
print(s1.full_name())  # Student: John Doe
