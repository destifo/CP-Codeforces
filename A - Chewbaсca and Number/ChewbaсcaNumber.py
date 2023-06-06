num = list(input())
 
for index,digit in enumerate(num):
    if int(digit) > 4:
        digit = int(digit)
        if index == 0 and digit == 9:
            continue
        digit = 9-digit
        num[index] = str(digit)
        
num = ''.join(num)
print(int(num))