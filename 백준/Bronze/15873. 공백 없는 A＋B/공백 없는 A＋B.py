string = input()
length = len(string)

split = length - 1
if string[split] == "0":
    split -= 1

a, b = int(string[:split]), int(string[split:])
print(a + b)