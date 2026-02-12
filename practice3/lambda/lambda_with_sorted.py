names = ["John", "Alice", "Bob"]
sorted_by_length = sorted(names, key=lambda n: len(n))
print(sorted_by_length)  # ['Bob', 'John', 'Alice']

numbers = [5, 2, 9, 1]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  # [9, 5, 2, 1]
