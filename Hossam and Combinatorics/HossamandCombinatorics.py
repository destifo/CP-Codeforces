

from collections import Counter


def countMinMax(min_val, max_val, nums):
    min_count, max_count = 0, 0
    
    for num in nums:
        if num == min_val:
            min_count += 1
        if num == max_val:
            max_count += 1
            
    return min_count, max_count


def findMinMax(nums):
    min_val, max_val = float('inf'), float('-inf')
    for num in nums:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        
    return min_val, max_val


def findPairs(nums):
    min_val, max_val = findMinMax(nums)
    min_count, max_count = countMinMax(min_val, max_val, nums)
    
    return min_count * max_count * 2
    
    
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    pairs = findPairs(nums)
    print(pairs)