from sys import stdin
input = lambda: stdin.readline().rstrip()

def find_factor(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    divisorsList.sort()
    return divisorsList

n = int(input())
teams = list(map(int, input().split()))
limits = {}

for size in teams: 
    for factor in find_factor(size):
        if factor not in limits: 
            limits[factor] = 0
        limits[factor] += 1

max_count = 0
for limit, count in limits.items():
    if count > 1:
        nums = limit * count
        if nums > max_count:
            max_count = nums

print(max_count)