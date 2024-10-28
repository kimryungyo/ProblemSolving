from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
v = [tuple(map(int, input().split())) for _ in range(n)]

class slope:
    def __init__(self, a, b):
        self.r = 0
        self.a = a
        self.b = b

    def rotate(self):
        self.r = (self.r + 1) % 4
        temp = self.a
        self.a = self.b
        self.b = -temp

    def __lt__(self, other):
        return self.b * other.a < self.a * other.b

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

count = [0] * 4
ans = 0

for i in range(n):
    slope_list = []
    for j in range(n):
        if i == j: continue
        x = slope(v[j][0] - v[i][0], v[j][1] - v[i][1])
        while not (x.a > 0 and x.b >= 0): x.rotate()
        slope_list.append(x)

    slope_list.sort()
    j = 0
    while j < len(slope_list):
        count = [0] * 4
        k = j
        while k < len(slope_list) and slope_list[j] == slope_list[k]:
            count[slope_list[k].r] += 1
            k += 1
        ans += count[0] * count[1]
        ans += count[1] * count[2]
        ans += count[2] * count[3]
        ans += count[3] * count[0]
        j = k

print(ans)