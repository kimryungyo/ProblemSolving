from sys import stdin
input = lambda: stdin.readline().rstrip()

from fractions import Fraction

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if key(arr[mid]):
            if mid == len(arr) - 1 or not key(arr[mid + 1]):
                return mid
            else:
                left = mid + 1
        else:
            right = mid - 1
    
    return -1

n = int(input())
lines = {}

for _ in range(n):
    a, b, c, d = map(int, input().split() )

    try:
        dx = c - a
        dy = d - b
        if dx == 0: raise ZeroDivisionError()

        slope = Fraction(dy, dx)
        intercept = b - (a * slope)

        key = (slope, intercept)
        value = sorted([a, c])

    except ZeroDivisionError:
        slope = "inf"
        intercept = a

        key = (slope, intercept)
        value = sorted([b, d])

    if key not in lines: lines[key] = []
    lines[key].append(value)

total = 0
for ranges in lines.values():
    
    events = []
    for start, end in ranges:
        events.append((start, 'start'))
        events.append((end, 'end'))
    
    events.sort(key=lambda x: (x[0], x[1] == 'start'))
    
    overlap_count = 0
    active_intervals = 0
    
    for event in events:
        if event[1] == 'start':
            overlap_count += active_intervals
            active_intervals += 1
        else:
            active_intervals -= 1
    
    total += overlap_count

print(total)