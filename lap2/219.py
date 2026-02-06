n = int(input())
episodes = {}  

for _ in range(n):
    line = input().split()
    name = line[0]
    count = int(line[1])
    
    if name in episodes:
        episodes[name] += count
    else:
        episodes[name] = count

for name in sorted(episodes):
    print(name, episodes[name])
