inputs = list(map(int, open(0).read().split()))
N = inputs[0]
S = inputs[1:N+1]
X, Y = inputs[N+1:N+3]

relative = int(N * X / 100)
absolute = 0

for score in S:
    if score >= Y:
        absolute += 1

print(relative, absolute)