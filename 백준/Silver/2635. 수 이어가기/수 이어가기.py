N = int(input())

max_sequence = []
for i in range(1, N + 1):
    sequence = [N, i]

    idx = 1
    while True:
        num = sequence[idx - 1] - sequence[idx]
        if num < 0: break
        sequence.append(num)
        idx += 1

    if len(max_sequence) < len(sequence):
        max_sequence = sequence

print(len(max_sequence))
print(" ".join(map(str, max_sequence)))