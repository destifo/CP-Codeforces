'''
https://codeforces.com/problemset/problem/1520/C
'''


from typing import List



# O(n^2) time,
# O(n^2) space,
# Approach: matrix, math
def buildMatrix(n: int) -> List[List[int]]:
    if n == 2:  return [[-1]]
    
    matrix = [[0 for i in range(n)] for j in range(n)]
    
    num = 1
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                matrix[i][j] = num
                num +=1
                
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 != 0:
                matrix[i][j] = num
                num +=1
                
    return matrix
    
    
t = int(input())
for i in range(t):
    n = int(input())
    mat = buildMatrix(n)
    for row in mat:
        print(*row)