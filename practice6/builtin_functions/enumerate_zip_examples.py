
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["John", "Jane", "Doe"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)