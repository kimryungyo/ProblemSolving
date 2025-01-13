import math

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if cross > 1e-12: return 1
    elif cross < -1e-12: return -1
    else: return 0

def is_cross(seg1, seg2):
    p1, p2 = seg1
    p3, p4 = seg2
    ccw1 = ccw(p1, p2, p3)
    ccw2 = ccw(p1, p2, p4)
    ccw3 = ccw(p3, p4, p1)
    ccw4 = ccw(p3, p4, p2)
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True
    return False

def is_cross_in_lines(seg, lines):
    for line in lines:
        if is_cross(seg, line):
            return True
    return False

def is_point_in_polygon(point, polygon):
    n = len(polygon)

    x, y = point
    inside = False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        if (y1 > y) != (y2 > y):
            x_cross = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_cross:
                inside = not inside

    return inside

def rotate_point(point, angle):
    rad = math.radians(angle)
    x, y = point
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return (x_new, y_new)

def rotate_polygon(polygon, angle):
    return [rotate_point(p, angle) for p in polygon]

def get_edges(polygon):
    edges = []
    n = len(polygon)
    for i in range(n):
        edges.append((polygon[i], polygon[(i+1) % n]))
    return edges

def can_fit_inside(object_polygon, container_polygon):
    obj_edges = get_edges(object_polygon)
    ctr_edges = get_edges(container_polygon)

    for e in obj_edges:
        if is_cross_in_lines(e, ctr_edges):
            return False
        
    for pt in object_polygon:
        if not is_point_in_polygon(pt, container_polygon):
            return False
        
    return True

N, M = map(int, input().split())

object_points = [ tuple(map(float, input().split())) for _ in range(N) ]
container_points = [ tuple(map(float, input().split())) for _ in range(M) ]

for angle in range(360):
    rotated_object = rotate_polygon(object_points, angle)
    if can_fit_inside(rotated_object, container_points):
        print(angle)
        quit()

print("impossible")