'''
https://codeforces.com/problemset/problem/1353/C
'''


# O(n) time,
# O(1) space,
# Approach: simulation, greedy



def findBoardMoves(n: int) -> int:
    moves = 0
    
    while n > 1:
        edge_cells = 2 * n + 2 * (n-2)
        move_to_center = n // 2
        moves += (edge_cells * move_to_center)
        n -=2
        
    return moves
    
    
t = int(input())
for i in range(t):
    n = int(input())
    print(findBoardMoves(n))