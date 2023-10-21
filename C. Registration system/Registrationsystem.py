

names = {}

n = int(input())
for _ in range(n):
    name = input()
    
    if name in names:
        count = names[name]
        names[name] += 1
        print(f"{name}{count}")
    else:
        names[name] = 1
        print("OK")