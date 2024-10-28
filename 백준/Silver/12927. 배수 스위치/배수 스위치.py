from sys import stdin
input = lambda: stdin.readline().rstrip()

lights = [ light == "Y" for light in input() ]
count = 0
for i in range(len(lights)):
    if lights[i]:
        count += 1
        term = i + 1
        for num in range(term, len(lights) + 1, term):
            lights[num - 1] = not lights[num - 1]

print(count)