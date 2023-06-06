

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

max_len = 1
nums.sort()

l, r = 0, 0
window = set()
window.add(nums[l])

while r < n:
    r +=1
    if r == n:  break
    if nums[r]/k not in window:
        max_len +=1
        window.add(nums[r])
        
print(max_len)