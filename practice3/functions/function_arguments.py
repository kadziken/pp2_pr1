# Позиционные аргументы
def add(a, b):
    return a + b

print(add(2, 3))

# Аргументы по умолчанию
def power(x, y=2):
    return x ** y

print(power(3))    # 9
print(power(3, 3)) # 27
