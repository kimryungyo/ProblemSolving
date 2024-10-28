from collections import deque

words = open(0).read().split()
for i in range(len(words) // 2):
    s, t = words[i * 2], words[i * 2 + 1]
    chars = deque(s)

    char = chars[0]
    for j in range(len(t)):
        if t[j] == char:
            chars.popleft()
            if not chars: break
            char = chars[0]

    print("Yes" if not chars else "No")