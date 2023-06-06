# O(n) time,
# O(n) space,
# Approach: hashmap,


def convertToMyNote(note: str, dictionary):
    my_note = []
    
    for word in note.split():
        my_note.append(dictionary[word])
      
    # print(my_note)  
    return my_note



n, m = list(map(int, input().split()))
dictionary = {}
for i in range(m):
    word1, word2 = input().split()
    dictionary[word1] = word2 if len(word2) < len(word1) else word1
    
note = input()
print(*convertToMyNote(note, dictionary))