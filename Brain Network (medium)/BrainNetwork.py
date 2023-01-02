from collections import defaultdict
import sys, threading
 
 
def main():
    def findLongest(node, graph, visited):
        visited.add(node)
        
        longest_node = node
        longest_dist = 0
        for nbr in graph[node]:
            if nbr in visited:  continue
            
            dist, other_node = findLongest(nbr, graph, visited)
            if dist > longest_dist:
                longest_dist = dist
                longest_node = other_node
        
        return longest_dist+1, longest_node
    
    
    nodes, edges = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(edges):
        nod1, nod2 = map(int, input().split())
        graph[nod1].append(nod2)
        graph[nod2].append(nod1)
        
    for node in graph:
        break
    
    _, other = findLongest(node, graph, set())
    dist, _ = findLongest(other, graph, set())
    print(dist-1)
 
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()