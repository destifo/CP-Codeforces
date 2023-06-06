
import heapq


s, n = map(int, input().split())

heap = []
for _ in range(n):
    dragon_strength, gain = map(int, input().split())
    heapq.heappush(heap, (dragon_strength, -gain))
    
pass_level = True
while heap:
    if heap[0][0] >= s:
        pass_level = False
        break
    
    curr_gain = -heapq.heappop(heap)[1] 
    s += curr_gain
    
if pass_level:
    print("YES")
else:
    print("NO")