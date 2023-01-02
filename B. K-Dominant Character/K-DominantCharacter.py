

s = input()

def isThereDominant(s: str, k: int) -> bool:
    # checking_queue = deque()
    # time = 0
    
    count = {}
    
    n = len(s)
    l, r = 0, k-1
    window = {}
    for i in range(k):
        ch = s[i]
        window[s[i]] = window.get(s[i], 0) + 1
        # checking_queue.append(s[i])
        count[ch] = True
       
    # print(count) 
    while r < n:
        r +=1
        if r == n:  break
        left_ch = s[l]
        window[left_ch] -=1
        l +=1
        right_ch = s[r]
        window[right_ch] = window.get(right_ch, 0) + 1
        for ch in count.keys():
            if window[ch] < 1:
                count[ch] = False
            
    # print(count)
    for val in count.values():
        if val:
            return True
            
    return False
    
    
def findMinK(lo: int, hi: int, s: str) -> int:
    ans = hi
    # if isThereDominant(s, lo):
    #     return lo
        
    while lo <= hi:
        mid = (hi+lo)//2
        if isThereDominant(s, mid):
            ans = min(ans, mid)
            hi = mid-1
        else:
            lo = mid+1
            
    return ans
    

print(findMinK(1, len(s), s))