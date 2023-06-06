from collections import deque

nodes, edges = map(int, input().split())

graph = [ set() for _ in range(nodes)]
for _ in range(edges):
    nod1, nod2 = map(int, input().split())
    graph[nod1-1].add(nod2-1)
    graph[nod2-1].add(nod1-1)
    
nod_colors = [-1 for _ in range(nodes)]

possible = True

for i in range(nodes):
    if nod_colors[i] != -1:   continue
    qu = deque()
    qu.append(i)
    color = 0
    while qu:
        qu_len = len(qu)
        for _ in range(qu_len):
            nod = qu.popleft()
            if nod_colors[nod] != -1 and nod_colors[nod] == color:
               continue
           
            if nod_colors[nod] != -1 and nod_colors[nod] != color:
                possible = False
                break
            nod_colors[nod] = color
            for nb in graph[nod]:
                qu.append(nb)
                
        if not possible:    break
        color = 0 if color == 1 else 1
    
if not possible:
    print(-1)
else:
    color1 = []
    color2 = []
    
    for nod, nod_color in enumerate(nod_colors):
        if nod_color == 0:  color1.append(nod+1)
        else:   color2.append(nod+1)
    
    print(len(color1))
    print(*color1)
    print(len(color2))
    print(*color2)