
from collections import Counter

string = input()
count = Counter(string)

chars = [ (char, cnt) for char, cnt in count.items() ]
chars.sort()
ans = chars[-1][0] * chars[-1][1]
print(ans)