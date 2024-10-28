import math

def max_n(S):
    return math.floor((-1 + math.sqrt(1 + 8*S)) / 2)

S = int(input())
print(max_n(S))