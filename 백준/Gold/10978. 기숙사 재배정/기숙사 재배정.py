DP = [0] * (21)
DP[2] = 1

for i in range(18): 
    DP[i+3] = ((i+2) * (DP[i+2]+DP[i+1]))

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N]) 