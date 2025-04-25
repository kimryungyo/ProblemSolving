N = int(input())
A = list(map(int, input().split()))

ops = []
for i in range(N):
    target = i + 1
    if A[i] == target: continue
        
    j = A.index(target, i)
    ops.append((i + 1, j + 1))
    A[i : j + 1] = reversed(A[i : j + 1])
    
if len(ops) > 100: print(-1)
else:
    print(len(ops))
    for l, r in ops:
        print(l, r)