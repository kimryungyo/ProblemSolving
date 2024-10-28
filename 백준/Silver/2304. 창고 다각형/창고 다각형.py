from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
if n == 1: print(int(input().split()[1])); quit()

pillars = []
for _ in range(n):
    pillar = tuple(map(int, input().split()))
    pillars.append(pillar)
pillars.sort()

area = 0

left_last = None
bef = pillars[0]
for i in range(1, n):
    pillar = pillars[i]
    pos, hei = pillar
    bef_pos, bef_hei = bef
    if hei >= bef_hei:
        area += (pos - bef_pos) * bef_hei
        left_last = pillar
        bef = pillar

right_last = None
bef = pillars[-1]
for i in range(n-2, -1, -1):
    pillar = pillars[i]
    pos, hei = pillar
    bef_pos, bef_hei = bef
    if hei >= bef_hei:
        area += (bef_pos - pos) * bef_hei
        right_last = pillar
        bef = pillar


if right_last is None:
    area += pillars[-1][1]
    
if left_last is None:
    area += pillars[0][1]

if right_last and left_last:
    area += (right_last[0] - left_last[0] + 1) * right_last[1]

print(area)