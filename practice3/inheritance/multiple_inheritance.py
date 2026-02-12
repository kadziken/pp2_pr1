# Пример множественного наследования

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

class Athlete:
    def run(self):
        print(f"{self.firstname} is running!")

class StudentAthlete(Student, Athlete):
    pass

sa = StudentAthlete("Mike", "Olsen", 2019)
# sa.full_name() здесь не работает, потому что StudentAthlete не наследует Student
# Нужно добавить наследование Student с __init__
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduation_year}")

class StudentAthlete(Student, Athlete):
    pass

sa = StudentAthlete("Mike", "Olsen", 2019)
sa.welcome()
sa.run()
