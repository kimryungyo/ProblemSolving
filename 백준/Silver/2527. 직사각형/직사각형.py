from sys import stdin
input = lambda: stdin.readline().rstrip()

def check_overlap(x1, y1, p1, q1, x2, y2, p2, q2):
    if x1 > p2 or y1 > q2 or x2 > p1 or y2 > q1: 
        return "d"
    elif (x1 == p2 and y1 == q2) or (x2 == p1 and y2 == q1) or (x1 == p2 and q1 == y2) or (x2 == p1 and q2 == y1):
        return "c"
    elif x1 == p2 or y1 == q2 or x2 == p1 or y2 == q1:
        return "b"
    else:
        return "a"

for i in range(4):
    result = check_overlap(*map(int, input().split()))
    print(result)