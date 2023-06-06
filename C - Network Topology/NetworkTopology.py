nodes, edges = list(map(int, input().split()))
 
graph = [ set() for _ in range(nodes)]
 
for i in range(edges):
    edge = list(map(int, input().split()))
    nod1, nod2 = edge
    
    graph[nod1-1].add(nod2-1)
    graph[nod2-1].add(nod1-1)
    
one_degree_nodes = 0
two_degree_nodes = 0
above_two_degree_nodes = 0
 
for node_neighbours in graph:
    n = len(node_neighbours)
    if n == 1:  one_degree_nodes +=1
    if n == 2:  two_degree_nodes +=1
    if n > 2:   above_two_degree_nodes +=1
    
if two_degree_nodes == nodes-2 and one_degree_nodes == 2 and above_two_degree_nodes == 0:
    print('bus topology')
elif two_degree_nodes == nodes:
    print('ring topology')
elif above_two_degree_nodes == 1 and one_degree_nodes == nodes-1:
    print('star topology')
else:
    print('unknown topology')