# Пример использования __init__() метода

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.brand} {self.model} ({self.year})"

my_car = Car("Toyota", "Corolla", 2020)
print(my_car.car_info())
