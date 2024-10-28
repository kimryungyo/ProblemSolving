table = [ [1] * i for i in range(1, 31) ]

for i in range(2, 30):
    for j in range(1, i):
        table[i][j] = table[i-1][j-1] + table[i-1][j]

n, k = map(int, input().split())
print(table[n-1][k-1])