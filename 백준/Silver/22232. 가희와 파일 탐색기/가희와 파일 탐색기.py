from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

files = []
for _ in range(N):
    s = input()
    filename, extension = s.split('.')
    files.append((filename, extension, s))

recognized = set(input().strip() for _ in range(M))

files.sort(key=lambda file: (file[0], 0 if file[1] in recognized else 1, file[1]))

for _, _, s in files:
    print(s)