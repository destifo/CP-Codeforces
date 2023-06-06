n = int(input())
relations = list(map(int, input().split()))
 
def f(plane):
    return relations[plane-1]
    
isThereTriangle = False
for plane in range(1, n+1):
    if n < 3:   break
    
    snd_plane = f(plane)
    if snd_plane == plane:  continue
    thrd_plane = f(snd_plane)
    if f(thrd_plane) == plane:
        print('yes')
        isThereTriangle = True
        break
        
    
if not isThereTriangle: print('no')