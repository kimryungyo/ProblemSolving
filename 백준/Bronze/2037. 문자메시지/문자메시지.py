p, w = map(int, input().split())
now = 0
result = 0
num = [[1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4],
       [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]]
s = input()

for char in s:
    idx = -1
    if 'A' <= char <= 'Z':
        idx = ord(char) - ord('A') + 1
    if char == ' ': idx = 0
    if idx != -1:
        result += num[0][idx] * p
        if now == num[1][idx] and idx != 0:
            result += w
        now = num[1][idx]

print(result)