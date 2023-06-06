


def findMaxBeauty(word: str, tokens: int, chosen_char: str) -> int:
    print(chosen_char)
    left, right = 0, 0
    str_len = len(word)
    first_longst = 0
    
    while right < len(word):
        if tokens == 0 and left == right and word[left] != chosen_char:
            left += 1
            right += 1
            continue
        
        if word[right] != chosen_char:
            first_longst = max(first_longst, right-left)
            if tokens > 0:
                tokens -= 1
                right += 1
            else:
                while tokens < 0 and left < right:
                    if word[left] != chosen_char:
                        tokens +=1
                    left +=1
        else:
            right +=1
            
    first_longst = max(first_longst, right-left)
    
    return first_longst




string_length, tokens = map(int, input().split())
string = input()
answer = max(findMaxBeauty(string, tokens, 'a'), findMaxBeauty(string, tokens, 'b'))
print(answer)