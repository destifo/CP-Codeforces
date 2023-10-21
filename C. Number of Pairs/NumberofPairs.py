


def binarySearchLowerBound(target, hi, nums):
    ans = hi+1
    lo = 0
    
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] >= target:
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
            
    return ans
    
    

def binarySearchUpperBound(target, hi, nums):
    ans = -1
    lo = 0
    
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] <= target:
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
        
    return ans


def findPairs(lo, hi, nums):
    pairs = 0
    nums.sort()
    
    for i in range(1, len(nums)):
        num = nums[i]
        curr_lo = lo-num
        curr_hi = hi-num
        start = binarySearchLowerBound(curr_lo, i-1, nums)
        end = binarySearchUpperBound(curr_hi, i-1, nums)
        if (start <= end):
            pairs += (end-start+1)
        
    return pairs



test_cases = int(input())
for _ in range(test_cases):
    n, l, r = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    print(findPairs(l, r, nums))