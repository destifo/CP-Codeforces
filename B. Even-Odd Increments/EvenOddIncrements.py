

test_cases = int(input())
for _ in range(test_cases):
    arr_length, queries = map(int, input().split())
    arr = list(map(int, input().split()))
    tot = sum(arr)
    odds, evens = 0, 0
    for num in arr:
        if num%2 == 0:  evens +=1
        else:   odds +=1
    
    for i in range(queries):
        parity, val = map(int, input().split())
        if parity == 0:
            tot += (evens * val)
            if val%2 != 0:
                odds += evens
                evens = 0
        else:
            tot += (odds * val)
            if val%2 != 0:
                evens += odds
                odds = 0
    print('-----', tot)