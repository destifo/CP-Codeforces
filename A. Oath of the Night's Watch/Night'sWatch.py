from collections import Counter


n = int(input())
stewards = list(map(int, input().split()))

count = Counter(stewards)
sorted_stewards = sorted(count.keys())

m = len(sorted_stewards)
ans = 0
for i in range(1, m-1):
    st = sorted_stewards[i]
    ans += count[st]
    
print(ans)