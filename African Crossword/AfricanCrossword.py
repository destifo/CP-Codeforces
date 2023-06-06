from collections import defaultdict
 
 
ROWS, COLS = map(int, input().split())
grid = []
for row in range(ROWS):
    grid.append([ch for ch in input()])
rows = [defaultdict(int) for _ in range(ROWS)]
cols = [defaultdict(int) for _ in range(COLS)]
 
for row in range(ROWS):
    for col in range(COLS):
        ch = grid[row][col]
        rows[row][ch] += 1
        cols[col][ch] += 1
      
ans = []  
for row in range(ROWS):
    for col in range(COLS):
        ch = grid[row][col]
        if rows[row][ch] > 1 or cols[col][ch] > 1:
            continue
        ans.append(ch)
        
ans = "".join(ans)
print(ans)