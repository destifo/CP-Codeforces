

n, m = map(int, input().split())
pb = set()
eb = 0
common = 0
for _ in range(n):
    pb.add(input())
    
for _ in range(m):
    word = input()
    if word in pb:
        common += 1
    
    eb += 1
    
turns = len(pb) + eb - common

pb_calls = len(pb) - (common//2)

if pb_calls > turns//2:
    print('YES')
else:
    print('NO')