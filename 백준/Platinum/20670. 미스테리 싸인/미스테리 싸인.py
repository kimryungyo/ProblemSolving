from sys import stdin
input = stdin.readline

def read_pairs(count):
    data = []
    while len(data) < 2 * count:
        data += list(map(int, input().split()))
    return [(data[i], data[i + 1]) for i in range(0, 2 * count, 2)]

def cross_product(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

def is_inside_convex(polygon, point):
    n = len(polygon)
    anchor = polygon[0]
    
    if cross_product(anchor, polygon[1], point) < 0:
        return False
    
    if cross_product(anchor, polygon[-1], point) > 0:
        return False
    
    left, right = 1, n - 1
    while right - left > 1:
        mid = (left + right) // 2
        if cross_product(anchor, polygon[mid], point) >= 0:
            left = mid
        else:
            right = mid
    
    return cross_product(polygon[left], polygon[left + 1], point) > 0

def main():
    N, M, K = map(int, input().split())

    polygon_A = read_pairs(N)
    polygon_B = read_pairs(M)
    sign_points = read_pairs(K)

    violations = 0
    for point in sign_points:
        inside_A = is_inside_convex(polygon_A, point)
        inside_B = is_inside_convex(polygon_B, point)
        
        if not inside_A or inside_B:
            violations += 1

    print("YES" if violations == 0 else violations)

main()