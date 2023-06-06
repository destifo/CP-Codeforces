from typing import *
from collections import deque
 
info = list(map(int, input().split()))
ROWS, COLS = info[0], info[1]
k = info[2]
 
grid = []
for _ in range(ROWS):
    row = list(input())
    grid.append(row)
    
def countEmptyCells(grid) -> int:
    start = None
    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '.':
                if start is None:   start = (row, col)
                count +=1
    
    return count, start
    
def getNbrs(coord: Tuple) -> int:
    nbrs = []
    row, col = coord
    
    if row > 0 and grid[row-1][col] == '.':
        nbrs.append((row-1, col))
    if row < ROWS-1 and grid[row+1][col] == '.':
        nbrs.append((row+1, col))
    if col > 0 and grid[row][col-1] == '.':
        nbrs.append((row, col-1))
    if col < COLS-1 and grid[row][col+1] == '.':
        nbrs.append((row, col+1))
 
    return nbrs
    
empty_cells, start = countEmptyCells(grid)
 
qu = deque()
qu.append(start)
path_len = 0
 
while qu:
    n = len(qu)
    for i in range(n):
        coord = qu.popleft()
        row, col = coord
        if grid[row][col] != '.': continue
        if path_len == (empty_cells-k):
            grid[row][col] = 'X'
        else:
            path_len +=1
            grid[row][col] = '*'
        
        for nb in getNbrs(coord):
            qu.append(nb)
            
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == '*':
            grid[row][col] = '.'
   
for row in grid:
    ans = ''.join(row)
    print(ans)