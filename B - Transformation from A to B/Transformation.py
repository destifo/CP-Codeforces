a, b = list(map(int, input().split()))
 
path = [a]
 
def isPathFound(curr: int, target: int) -> bool:
    
    if curr == target:  return True
        
    if curr > target:   return False
    
    nbr1 = curr * 2
    path.append(nbr1)
    if isPathFound(nbr1, target):   return True
    path.pop()
    
    nbr2 = (curr*10) + 1
    path.append(nbr2)
    if isPathFound(nbr2, target):   return True
    path.pop()
    
    return False
    
if isPathFound(a, b):
    print('YES')
    print(len(path))
    print(*path)
else:
    print('NO')