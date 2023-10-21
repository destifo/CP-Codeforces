


def findIndex(nums):
    even_count, odd_count = 0, 0
    even_index, odd_index = -1, -1
    
    for i, num in enumerate(nums):
        if num % 2 == 0:
            even_count += 1
            even_index = i+1
        else:
            odd_count += 1
            odd_index = i+1
            
        if even_count > 1 and odd_index != -1:
            return odd_index
        
        if odd_count > 1 and even_index != -1:
            return even_index
            
    return -1


n = int(input())
nums = list(map(int, input().split()))
print(findIndex(nums))