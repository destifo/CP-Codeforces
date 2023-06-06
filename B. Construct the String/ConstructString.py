# O(a) time,
# O(n) space,
# Approach: string manipulation, math


def constructString(n:int, a:int, b:int) -> str:

    sub_str = []
    for i in range(b):
        sub_str.append(chr(97+i))
        
    while len(sub_str) < a:
        sub_str.append(sub_str[0])
        
    rem = n % a
    sub_str = ''.join(sub_str)
    ans = sub_str * (n//a)
    if rem != 0:
        ans += sub_str[:rem]
        
    return ans



t = int(input())
for i in range(t):
    info = list(map(int, input().split()))
    n = info[0]
    a = info[1]
    b = info[2]
    
    print(constructString(n, a, b))