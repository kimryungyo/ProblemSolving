from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
coordinates = [ list(map(int, input().split())) for _ in range(n) ]

count = 0

for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            
            side1 = (coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2
            side2 = (coordinates[b][0] - coordinates[c][0])**2 + (coordinates[b][1] - coordinates[c][1])**2
            side3 = (coordinates[c][0] - coordinates[a][0])**2 + (coordinates[c][1] - coordinates[a][1])**2
            
            if side1 + side2 - side3 == 0 or side1 + side3 - side2 == 0 or side2 + side3 - side1 == 0: 
                count += 1

print(count)