
from collections import defaultdict

# rooms = int(input())
# costs = list(map(int, input().split()))
# # graph = defaultdict(set)
# next_room = list(map(int, input().split()))
rooms = 5
costs = [1, 2, 3, 2, 10]
# graph = defaultdict(set)
next_room = [1, 3, 4, 3, 3]
# incomings = defaultdict(int)
# for room in range(rooms):
#     if room == next_room[room]: continue
#     graph[room+1].add(next_room[room])
#     incomings[next_room[room] +=1


def placeTrap(room: int, trapped_rooms, vstd, cycle, min_cost_room) -> None:
    if room in trapped_rooms:   return

    if room in cycle:
        trapped_rooms.append(min_cost_room)
        return
    
    vstd.add(room)
    
    nxt = next_room[room-1]
    
    if nxt != room:
        if nxt in vstd:
            cycle.add(room)
            
            if min_cost_room is None or costs[min_cost_room-1] > costs[room-1]:
                min_cost_room = room
                
        print(room, nxt)
        placeTrap(nxt, trapped_rooms, vstd, cycle, min_cost_room)
    else:
        trapped_rooms.add(room)
    

trapped_rooms = set()
vstd = set()
for room in range(1, rooms+1):
    if room in vstd:    continue
    placeTrap(room, trapped_rooms, vstd, set(), None)
    
print(trapped_rooms)