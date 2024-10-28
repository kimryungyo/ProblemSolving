a, b, c = map(int, input().split())

if a == 0: print(c ** 2 - b); quit()
if b == 0: print(c ** 2 - a); quit()
if c == 0: print(int((a + b) ** 0.5))