n = int(input())

non_zeros = set()
letters = {}
for _ in range(n):
    alphabet = input()

    non_zeros.add(alphabet[0])

    for idx, char in enumerate(alphabet[::-1]):
        if char not in letters: letters[char] = 0
        letters[char] += 10 ** idx

sorted_char = sorted(letters, key=lambda x: letters[x], reverse=True)

if len(letters) == 10:
    for char in sorted_char[::-1]:
        if char not in non_zeros:
            sorted_char.remove(char)
            break

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for char in sorted_char:
    sum += letters[char] * numbers.pop()

print(sum)