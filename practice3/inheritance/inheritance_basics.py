# Базовое наследование классов

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    pass

s1 = Student("Mike", "Olsen")
print(s1.full_name())  # Mike Olsen
