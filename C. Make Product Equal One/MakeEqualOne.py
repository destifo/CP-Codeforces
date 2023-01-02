


n = int(input())
nums = list(map(int, input().split()))

# nums = [-5, -3, 5, 3, 0]

zeros = 0
positives = []
negatives = []

for num in nums:
    if num > 0:
        positives.append(num)
    elif num == 0:
        zeros+=1
    else:
        negatives.append(num)
        
coins = 0

if len(negatives) % 2 != 0:
    if zeros:
        coins +=1
        zeros -=1
    else:
        negatives.sort()
        curr = -negatives.pop()
        diff = curr + 1
        coins += diff
        
coins += zeros
for num in negatives:
    coins += abs(num+1)

for num in positives:
    coins += (num-1)
    
print(coins)