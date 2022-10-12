import sys, threading
    
 
def main():
    
    def spreadRumor(curr, vstd):
        if curr in vstd:  return
        vstd.add(curr)
        
        for nb in graph[curr]:
            spreadRumor(nb, vstd)
    
    characters, friendships = list(map(int, input().split()))
    costs_input = input().split()
    costs = []
    
    for i in range(characters):
        costs.append((int(costs_input[i]), i))
    
    graph = [set() for _ in range(characters)]
    for i in range(friendships):
        friend1, friend2 = list(map(int, input().split()))
        graph[friend1-1].add(friend2-1)
        graph[friend2-1].add(friend1-1)   
    
    costs.sort()
    vstd = set()
    tot_cost = 0
    
    for cost, person in costs:
        if person in vstd:   continue
        tot_cost +=cost
        spreadRumor(person, vstd)
    
    print(tot_cost)
 
threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()