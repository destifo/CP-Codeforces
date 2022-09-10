'''
https://codeforces.com/problemset/problem/1342/A
'''


def findMinDollars(x: int, y: int, a: int, b: int) -> int:
    dollars = 0
    x = abs(x)
    y = abs(y)
    min_val = min(x, y)
    diff = abs(x-y)
    
    if b < 2 * a:
        dollars += (a*diff)
        dollars += (min_val*b)
    else:
        dollars = a * (x+y)
        
    return dollars
 
 
 
t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    
    print(findMinDollars(x, y, a, b))