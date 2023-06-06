
rows = 5
cols = 5
matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))
 
coord = None   
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
            coord = (i, j)
            break
        
mid_coord = (2, 2)
moves = abs(coord[0]-mid_coord[0]) + abs(coord[1]-mid_coord[1])
print(moves)