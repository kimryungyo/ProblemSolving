from math import sin
A, B, C = map(int, input().split())

def function(x):
    return A * x + B * sin(x) - C

def binary_search():
    left, right = 0, 100000
    while right - left > 1e-9:
        mid = (left + right) / 2
        if function(mid) > 0:
            right = mid
        else:
            left = mid
    return left

print(binary_search())