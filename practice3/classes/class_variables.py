# Различие между class и instance переменными

class Dog:
    species = "Canis familiaris"  # class variable

    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)

# Изменяем class variable
Dog.species = "Dog"
print(dog1.species)
print(dog2.species)

