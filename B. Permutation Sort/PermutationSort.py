from typing import *


def findMinMoves(nums: List[int], n: int) -> int:
    min_val = nums[0]
    max_val = nums[0]
    isSorted = True
    
    for i in range(n-1):
        num = nums[i]
        if num > nums[i+1]:
            isSorted = False
            
        min_val = min(min_val, num)
        max_val = max(max_val, num)
        
    min_val = min(min_val, nums[n-1])
    max_val = max(max_val, nums[n-1])
    
    if isSorted:    return 0
    if min_val == nums[0] or max_val == nums[n-1]:
        return 1
        
    if min_val == nums[n-1] and max_val == nums[0]:
        return 3
        
    return 2


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(findMinMoves(nums, n))