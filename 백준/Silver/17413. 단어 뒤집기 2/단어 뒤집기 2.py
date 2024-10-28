def reverse_words(s):
    result = []
    word = []
    in_tag = False
    
    for char in s:
        if char == '<':
            result.extend(reversed(word))
            word = []
            in_tag = True
            result.append(char)

        elif char == '>':
            in_tag = False
            result.append(char)

        elif char == ' ' and not in_tag:
            result.extend(reversed(word))
            word = []
            result.append(char)

        elif in_tag: result.append(char)

        else: word.append(char)
    
    result.extend(reversed(word))
    return ''.join(result)

s = input().strip()
print(reverse_words(s))