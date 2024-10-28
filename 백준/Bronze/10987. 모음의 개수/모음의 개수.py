word = input()
sum = 0
for char in ['a', 'e', 'i', 'o', 'u']:
    sum += word.count(char)
print(sum)