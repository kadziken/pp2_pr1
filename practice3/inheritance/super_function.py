# Использование super() для наследования __init__

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduation_year}")

s1 = Student("Anna", "Smith", 2022)
s1.welcome()

