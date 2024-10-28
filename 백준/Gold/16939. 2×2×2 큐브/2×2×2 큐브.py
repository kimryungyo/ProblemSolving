arr = list(map(int,input().split()))
preprocessed = [
    [1, 2, 17, 19, 13, 3, 4, 15, 5, 6, 7, 8, 14, 16, 11, 12, 9, 10, 18, 20, 21, 22, 23, 24],
    [1, 2, 14, 16, 13, 15, 9, 10, 11, 12, 17, 19, 3, 4, 18, 20, 21, 22, 23, 24, 5, 6, 7, 8],
    [1, 3, 6, 8, 5, 7, 10, 12, 9, 11, 21, 23, 22, 24, 2, 4, 17, 18, 19, 20, 13, 14, 15, 16],
    [1, 3, 21, 23, 5, 7, 2, 4, 9, 11, 6, 8, 22, 24, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 3, 4, 5, 6, 15, 16, 9, 10, 11, 12, 13, 14, 23, 24, 17, 18, 7, 8, 21, 22, 19, 20],
    [1, 2, 3, 4, 5, 6, 19, 20, 13, 14, 7, 8, 9, 10, 11, 12, 17, 18, 23, 24, 21, 22, 15, 16],
]
 
result = 0
for i in range(6):
    check = preprocessed[i]
    for j in range(6):
        face = list(map(lambda x : x - 1, check[(4 * j):4 * (j + 1)]))
        if not (arr[face[0]] == arr[face[1]] == arr[face[2]] == arr[face[3]]):
            break
    else: result = 1; break
 
print(result)