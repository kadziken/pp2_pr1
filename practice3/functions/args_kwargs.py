def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4))  # 10

def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Mike", age=20, city="Astana")

