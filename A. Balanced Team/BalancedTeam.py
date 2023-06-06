
# O(nlogn) time,
# O(1) space,
# Approach: two pointers, 


n = int(input())
skillpoints = list(map(int, input().split()))

skillpoints.sort()
l, r = 0, 1
max_group = 1

while r < n:
    if skillpoints[r] - skillpoints[l] <= 5:
        r +=1
    else:
        max_group = max(max_group, r-l)
        while skillpoints[r] - skillpoints[l] > 5:
            l +=1
        
max_group = max(max_group, r-l)        

print(max_group)