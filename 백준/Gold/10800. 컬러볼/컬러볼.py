from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
balls = []
colors = {}
sizes = []

for _ in range(n):
    color, size = map(int, input().split())
    balls.append((color, size))
    if color not in colors: colors[color] = []
    colors[color].append(size)
    sizes.append(size)

def get_sums_dp(arr):
    arr.sort()
    sums = {}
    check = arr[0]
    sum = 0
    for num in arr:
        if check != num:
            sums[num] = sum
            check = num
        sum += num
    return sums

size_sums = get_sums_dp(sizes)
color_sums = {}
for color in colors.keys():
    color_sums[color] = get_sums_dp(colors[color])

for color, size in balls:
    print(size_sums.get(size, 0) - color_sums[color].get(size, 0))