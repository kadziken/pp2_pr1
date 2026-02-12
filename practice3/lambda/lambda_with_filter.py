nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4, 6]

# Отбираем имена длиннее 3 букв
names = ["Bob", "Alice", "Tom", "John"]
long_names = list(filter(lambda n: len(n) > 3, names))
print(long_names)
