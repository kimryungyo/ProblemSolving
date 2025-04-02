from fractions import Fraction
from collections import defaultdict
from math import copysign
from sys import stdin
input = stdin.readline

def required_speed_hash(x, y, target_x, target_y):
    if target_y >= y: return None # 흐즈로보다 높은 곳에 있는 공은 맞출 수 없음
    speed = Fraction((target_x - x) ** 2, 2 * (y - target_y))
    speed *= copysign(1024, target_x - x)
    return speed

# 같은 속도로 맞출 수 있는 공의 개수가 가장 많은 경우를 찾으면 된다.
x, y = map(int, input().split())
n = int(input())
targets = [ tuple(map(int, input().split())) for _ in range(n) ]
counts = defaultdict(int)

for target in targets:
    speed = required_speed_hash(x, y, *target)
    if speed: counts[speed] += 1

print(max(counts.values()) if counts.values() else 0)