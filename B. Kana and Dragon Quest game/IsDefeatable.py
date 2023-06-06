# O(logn) time,
# O(1) space,
# Approach: greedy, 


t = int(input())
for i in range(t):
    info = list(map(int, input().split()))
    hp = info[0]
    n = info[1]
    m = info[2]
    
    while True:
        if hp <= 0:
            print('yes')
            break
        if m < 1:
            print('no')
            break
        
        if hp > 20 and n > 0:
            hp = (hp//2) + 10
            n -=1
        else:
            hp -=10
            m -=1
        