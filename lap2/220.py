n = int(input())
doc = {}  

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        key = cmd[1]
        value = cmd[2]
        doc[key] = value  
    elif cmd[0] == "get":
        key = cmd[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
