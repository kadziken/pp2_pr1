# Функции с возвратом значений

def square(x):
    return x**2

result = square(5)
print("Square:", result)

# Возврат нескольких значений
def min_max(lst):
    return min(lst), max(lst)

numbers = [3, 7, 1, 9]
minimum, maximum = min_max(numbers)
print("Min:", minimum, "Max:", maximum)

