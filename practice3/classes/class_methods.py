# Методы класса и экземпляра

class Circle:
    pi = 3.14159  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

    # instance method
    def area(self):
        return Circle.pi * self.radius ** 2

    # class method
    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi

c1 = Circle(5)
print(c1.area())  # 78.53975

Circle.set_pi(3.14)
print(c1.area())  # 78.5
