string = input()
length = len(string)

strings = []
for i in range(length - 2):
    for j in range(i + 1, length - 1):
        a = string[0:i+1][::-1]
        b = string[i+1:j+1][::-1]
        c = string[j+1:length][::-1]
        r = a + b + c
        strings.append(r)

print(min(strings))