from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((e, s))
meetings.sort(reverse=True)

count = 1
end_time, _ = meetings.pop()
while meetings:
    end, start = meetings.pop()
    if start >= end_time:
        count += 1
        end_time = end

print(count)