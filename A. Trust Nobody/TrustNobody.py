

from typing import List

# O(n^2) time,
# O(1) space,
# Approach: counting, greedy, 
def findPossibleLiars(l: List[int]) -> int:
    for liars in range(len(l)+1):
        count = 0
        for i in l:
            if liars < i:
                count += 1
            
        if count == liars:
            return count
            
    return -1


test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    l = list(map(int, input().split()))
    
    print(findPossibleLiars(l))