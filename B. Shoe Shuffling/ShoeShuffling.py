from collections import Counter


# O(n) time,
# O(1) space,
# Approach: two pointers, cycle rotation
def findPermutation(nums):
    left, right = 0, 0
    ans = []
    
    while right < len(nums):
        
        while right < len(nums)-1 and nums[right] == nums[right+1]:
            right += 1

        if left == right:
            print(-1)
            return
        
        ans.append(right+1)
        for i in range(left, right):
            ans.append(i+1)
        
        right += 1    
        left = right
    
    print(*ans)
    

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    findPermutation(nums)