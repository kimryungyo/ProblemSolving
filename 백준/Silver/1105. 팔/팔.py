A, B = input().split()
A = A.zfill(len(B))

count = 0
for i in range(len(A)):
    if A[i] == B[i] == "8": count += 1
    elif A[i] != B[i]: break

print(count)