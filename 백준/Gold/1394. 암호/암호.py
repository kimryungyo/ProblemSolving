mod = 900528
chars = { v: i for i, v in enumerate(input()) }
password = list(reversed(input()))

count = 0
for idx, char in enumerate(password):
    count += pow(len(chars), idx, mod) * (chars[char] + 1)
    count %= mod
print(count)