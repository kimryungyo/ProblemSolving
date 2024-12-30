from collections import Counter

string = input()
counter = Counter(string)
n = len(string)

def backtrack(path_length, last_char, counter):
    if path_length == n: 
        return 1

    total = 0

    for char in counter:
        if counter[char] > 0 and char != last_char:
            counter[char] -= 1
            total += backtrack(path_length + 1, char, counter)
            counter[char] += 1
    return total

answer = backtrack(0, None, counter)
print(answer)