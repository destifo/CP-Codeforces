


def findMaxHeightSum(past_row, index, tot, row1, row2, memo):
    
    if index == len(row1):
        return tot
    
    
    if (index, past_row) in memo:
        return memo[(index, past_row)]
    
        
    next_row = 1 if past_row == 0 else 0
    toAdd = row1[index] if next_row == 0 else row2[index]
    shift_row = findMaxHeightSum(next_row, index+1, tot+toAdd, row1, row2, memo)
    skip_index = float('-inf')
    if index < len(row1)-1:
        skip_index =  max(findMaxHeightSum(0, index+2, tot+row1[index+1], row1, row2, memo), 
                        findMaxHeightSum(1, index+2, tot+row2[index+1], row1, row2, memo))
    
    memo[(index, past_row)] = max(shift_row, skip_index)
    return memo[(index, past_row)]


n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

memo = {}

perfect_team = max(findMaxHeightSum(0, 1, row1[0], row1, row2, memo), findMaxHeightSum(1, 1, row2[0], row1, row2, memo))
print(perfect_team)