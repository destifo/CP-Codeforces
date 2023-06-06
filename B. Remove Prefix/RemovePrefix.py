


def findMinMoves(nums):
    moves = 0
    duplicates = set()
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            duplicates.add(num)
            
    l = 0
    while len(duplicates) > 0:
        moves +=1
        num = nums[l]
        count[num] -=1
        if count[num] < 2 and num in duplicates:
            duplicates.remove(num)
        l +=1
    
    return moves



t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(findMinMoves(nums))