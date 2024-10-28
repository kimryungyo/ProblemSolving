strings = [ "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "OPERATOR" ]
keys = {}

for i, string in enumerate(strings):
    num = i + 3

    for char in string:
        if char not in keys: keys[char] = set()
        keys[char].add(num)

for key in keys:
    keys[key] = sorted(keys[key])

number = input()
time = 0
for char in number:
    time += keys[char][0]

print(time)