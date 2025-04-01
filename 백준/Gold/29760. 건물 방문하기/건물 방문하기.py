from sys import stdin
input = stdin.readline

N, H, W = map(int, input().split())
floor_dict = {}
for _ in range(N):
    x, y = map(int, input().split())
    if x not in floor_dict:
        floor_dict[x] = [y, y]
    else:
        floor_dict[x][0] = min(floor_dict[x][0], y)
        floor_dict[x][1] = max(floor_dict[x][1], y)

floors = sorted(floor_dict.keys())

dp = [[0,0] for _ in range(len(floors))]

f = floors[0]
L, R = floor_dict[f]
d = R - L

vertical_cost = (f - 1) * 100

cost_to_left = min(abs(1 - R) + d, abs(1 - L) + 2 * d)
cost_to_right = min(abs(1 - L) + d, abs(1 - R) + 2 * d)
dp[0][0] = vertical_cost + cost_to_left
dp[0][1] = vertical_cost + cost_to_right

prev_floor = f

for i in range(1, len(floors)):
    f = floors[i]
    L, R = floor_dict[f]
    d = R - L
    
    vertical_cost = (f - prev_floor) * 100
    
    new_left = new_right = 10 ** 18
    
    for prev_pos, prev_cost in [(floor_dict[floors[i-1]][0], dp[i-1][0]), (floor_dict[floors[i-1]][1], dp[i-1][1])]:
        cost_left = min(abs(prev_pos - R) + d, abs(prev_pos - L) + 2 * d)
        new_left = min(new_left, prev_cost + vertical_cost + cost_left)
        
        cost_right = min(abs(prev_pos - L) + d, abs(prev_pos - R) + 2 * d)
        new_right = min(new_right, prev_cost + vertical_cost + cost_right)
        
    dp[i][0] = new_left
    dp[i][1] = new_right
    prev_floor = f

ans = min(dp[-1][0], dp[-1][1])
print(ans)