# O(nlogn) time, can be done in O(n) times
# O(n) space,
# Approach: sorting,


n = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(" ".join(list(map(str, nums))))