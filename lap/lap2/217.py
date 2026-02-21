from collections import Counter

n = int(input())
numbers = [input().strip() for _ in range(n)]

freq = Counter(numbers)  

count_three = sum(1 for num, cnt in freq.items() if cnt == 3)

print(count_three)
