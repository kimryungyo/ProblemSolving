from sys import stdin
input = lambda: stdin.readline().rstrip()

for _ in range(int(input())):
    points = [list(map(int, input().split())) for _ in range(4)]
    
    distances = []
    for i in range(4):
        for j in range(i+1, 4):
            distance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            distances.append(distance)
    
    if len(set(distances)) == 2 and distances.count(max(distances)) == 2:
        print(1)
    else:
        print(0)