from dataclasses import dataclass
from functools import cmp_to_key
from math import isclose

EPSILON = 1e-12

@dataclass
class Point:
    x: float
    y: float
    z: float
    
    def __sub__(self, other):
        return Point(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __truediv__(self, other):
        return Point(
            self.x / other.x if other.x != 0 else float('inf'),
            self.y / other.y if other.y != 0 else float('inf'),
            self.z / other.z if other.z != 0 else float('inf')
        )

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (
            isclose(self.x, other.x, abs_tol=EPSILON) and
            isclose(self.y, other.y, abs_tol=EPSILON)
        )

def cross_product(a, b):
    return a.x * b.y - a.y * b.x

def project_point(origin, target):
    adjustment = Point(-EPSILON, -EPSILON, -EPSILON)
    direction = target - origin - adjustment

    ratio = target / direction
    return Point(
        direction.x * (ratio.x - ratio.z),
        direction.y * (ratio.y - ratio.z),
        0
    )

def calculate_ccw(a, b, c):
    return cross_product(a, b) + cross_product(b, c) + cross_product(c, a)

def have_two_coordinates_same(a, b):
    return (
        (isclose(a.x, b.x, abs_tol=EPSILON) and isclose(a.y, b.y, abs_tol=EPSILON)) or
        (isclose(a.y, b.y, abs_tol=EPSILON) and isclose(a.z, b.z, abs_tol=EPSILON)) or
        (isclose(a.z, b.z, abs_tol=EPSILON) and isclose(a.x, b.x, abs_tol=EPSILON))
    )

def compare_primary(a, b):
    if isclose(a.y, b.y, abs_tol=EPSILON):
        return a.x < b.x
    return a.y < b.y

def compare_counter_clockwise(a, b):
    orientation = calculate_ccw(origin_point, a, b)
    if not isclose(orientation, 0.0, abs_tol=EPSILON):
        return orientation > 0
    
    return compare_primary(b, a)

def contains_point(points, target):
    return any(p == target for p in points)

origin_point = Point(0.0, 0.0, 0.0)

def compute_convex_hull(points):
    if not points: return []
    
    points.sort(key=cmp_to_key(lambda a, b: -1 if compare_primary(a, b) else (1 if a != b else 0)))
    
    global origin_point
    origin_point = points[0]
    
    sorted_points = sorted(points[1:], key=cmp_to_key(lambda a, b: -1 if compare_counter_clockwise(a, b) else 1))
    points[1:] = sorted_points
    
    convex_hull = [points[0], points[1]]
    
    for point in points[2:]:
        while len(convex_hull) > 1 and calculate_ccw(convex_hull[-1], convex_hull[-2], point) >= 0:
            convex_hull.pop()
        convex_hull.append(point)
    
    while len(convex_hull) > 2 and calculate_ccw(convex_hull[-1], convex_hull[-2], convex_hull[0]) >= 0:
        convex_hull.pop()
    
    return convex_hull

def main():
    tree = list(map(float, input().split()))
    point1 = Point(tree[0], tree[1], tree[2])
    point2 = Point(tree[3], tree[4], tree[5])
        
    light = list(map(float, input().split()))
    proj_vec = Point(light[0], light[1], light[2])
    
    if have_two_coordinates_same(point1, point2):
        return 0
    
    elif proj_vec.z <= point1.z or proj_vec.z <= point2.z:
        return -1
    
    else:
        corners = []
        for i in range(8):
            x = point1.x if (i & 4) == 0 else point2.x
            y = point1.y if (i & 2) == 0 else point2.y
            z = point1.z if (i & 1) == 0 else point2.z
            corner = Point(x, y, z)
            
            projected = project_point(proj_vec, corner)
            
            if not contains_point(corners, projected):
                corners.append(projected)
        
        convex_hull = compute_convex_hull(corners)
        
        area = 0
        if len(convex_hull) < 3:
            return 0
        
        for i in range(1, len(convex_hull) - 1):
            triangle_orientation = calculate_ccw(convex_hull[0], convex_hull[i], convex_hull[i + 1])
            area += abs(triangle_orientation)
        
        return area / 2

print(main())