
# warriors, minutes = map(int, input().split())

# strengths = list(map(int, input().split()))
# arrows = list(map(int, input().split()))
warriors, minutes = 4, 4

strengths = [1, 2, 3, 4]
arrows = [9, 1, 10, 6]

strength_pfsum = [0]
tot = 0
for strength in strengths:
    tot += strength
    strength_pfsum.append(tot)
    

def binarySearch(lo, hi, target, pf_start_index) -> int:
    ans = hi
    
    while lo <= hi:
        mid = lo + (hi-lo)//2
        
        if (strength_pfsum[mid] - strength_pfsum[pf_start_index]) < target:
            lo = mid+1
        else:
            ans = mid
            hi = mid-1
            
    return ans


start_index = 0
last_round_remaining = 0
for arrow in arrows:
    arrow += last_round_remaining
    last_round_remaining = 0
    last_down = binarySearch(start_index+1, warriors, arrow, start_index)
    if (strength_pfsum[last_down]-strength_pfsum[start_index]) > arrow:
        last_round_remaining = arrow - (strength_pfsum[last_down-1]-strength_pfsum[start_index])
        last_down-=1
    
    rem_warriors = warriors-last_down
    if rem_warriors == 0:
        last_round_remaining = 0
        # print(warriors)
        start_index = 0
    else:
        # print(rem_warriors)
        start_index = last_down