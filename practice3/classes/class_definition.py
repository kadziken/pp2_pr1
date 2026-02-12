# Простейшее определение класса и создание объектов

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

# Создание объектов
p1 = Person("John", "Doe")
p2 = Person("Alice", "Smith")

print(p1.full_name())  # John Doe
print(p2.full_name())  # Alice Smith

