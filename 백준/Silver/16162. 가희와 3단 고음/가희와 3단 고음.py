N, A, D = map(int, input().split())
notes = list(map(int, input().split()))

expected = A
count = 0
for note in notes:
    if note == expected:
        count += 1
        expected += D
        
print(count)