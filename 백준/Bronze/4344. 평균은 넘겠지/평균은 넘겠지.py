import sys
input = sys.stdin.read

data = input().split()
C = int(data[0])

index = 1
results = []

for _ in range(C):
    N = int(data[index])
    scores = list(map(int, data[index + 1:index + 1 + N]))
    index += (N + 1)

    average = sum(scores) / N
    above_average_count = sum(1 for score in scores if score > average)
    percentage = (above_average_count / N) * 100
    
    results.append(f"{percentage:.3f}%")

for result in results:
    print(result)