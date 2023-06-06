# O(logn) time,
# O(1) space,
# Approach: greedy, math


t = int(input())
for i in range(t):
    n = int(input())
    moves = 0
    
    while n != 1:
        if n % 3 != 0:
            print(-1)
            quit()
        
        if n % 2 == 0:
            n //=6
        else:
            n *=2
        moves +=1
            
    print(moves)  