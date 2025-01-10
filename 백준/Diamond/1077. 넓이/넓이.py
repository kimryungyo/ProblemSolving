import math
import sys
input = sys.stdin.readline

def get_angle(point_1, point_2):
    """
    두 점 사이의 각도를 계산하는 함수
    """
    return math.atan2(point_2[1] - point_1[1], point_2[0] - point_1[0])

def sort_points_ccw(points):
    """
    점들을 반시계 방향으로 정렬하는 함수
    """
    base_point = min(points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(points, key=lambda point: (get_angle(base_point, point), point[1], point[0]))
    return sorted_points

def get_ccw(p1, p2, p3):
    """
    세 점의 방향성을 계산하는 함수 (Counter Clock Wise)
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return ccw

def polygon_area(points):
    """
    다각형의 면적을 계산하는 함수 (Shoelace formula)
    """
    n = len(points)
    coors = points.copy()
    coors.append(coors[0])
    area = 0
    for i in range(n):
        area += (coors[i][0] * coors[i+1][1])
        area -= (coors[i][1] * coors[i+1][0])
    area = abs(area / 2)
    return area

def get_ccw_sign(p1, p2, p3):
    """
    세 점의 CCW 방향성을 부호로 반환하는 함수
    """
    ccw_sign = math.copysign(1, get_ccw(p1, p2, p3))
    return ccw_sign

def is_intersect(line_1, line_2):
    """
    두 선분이 교차하는지 여부를 판단하는 함수
    """
    o1 = get_ccw_sign(*line_1, line_2[0])
    o2 = get_ccw_sign(*line_1, line_2[1])
    o3 = get_ccw_sign(*line_2, line_1[0])
    o4 = get_ccw_sign(*line_2, line_1[1])
    
    if o1 != o2 and o3 != o4: return True
    return False

def find_intersect(line_1, lines):
    """
    주어진 선분과 교차하는 선분을 찾는 함수
    """
    for line in lines:
        if is_intersect(line_1, line):
            return line
    return None

def is_point_in_convex(point, convex):
    """
    점이 컨벡스헐 내부에 있는지 확인하는 함수
    """
    sign = None

    convex_1 = convex[0]
    for i in range(1, len(convex)):
        convex_2 = convex[i]
        ccw_sign = get_ccw_sign(convex_1, convex_2, point)
        if sign is None: sign = ccw_sign
        elif sign != ccw_sign: return False
        convex_1 = convex_2

    ccw_sign = get_ccw_sign(convex[-1], convex[0], point)
    if sign != ccw_sign: return False

    return True

def get_points_in_convex(points, convex):
    """
    컨벡스헐 내의 점들과 교차하는 선분을 찾는 함수
    """
    point_count = len(points)

    is_in_points = [ False ] * point_count
    for idx in range(point_count):
        point = points[idx]
        is_in = is_point_in_convex(point, convex)
        if is_in: is_in_points[idx] = True

    in_points = [ points[idx] for idx in range(point_count) if is_in_points[idx] ]

    cross_lines = []
    for idx in range(point_count - 1):
        if is_in_points[idx] != is_in_points[idx + 1]:
            cross_lines.append( (points[idx], points[idx+1]) )

    if is_in_points[-1] != is_in_points[0]:
        cross_lines.append( (points[-1], points[0]) )

    return in_points, cross_lines

def get_cross_point(line_1, line_2):
    """
    두 선분의 교차점을 계산하는 함수
    """
    x1, y1 = line_1[0]
    x2, y2 = line_1[1]
    x3, y3 = line_2[0]
    x4, y4 = line_2[1]

    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1

    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3

    determinant = a1 * b2 - a2 * b1

    intersect_x = (b2 * c1 - b1 * c2) / determinant
    intersect_y = (a1 * c2 - a2 * c1) / determinant

    return (intersect_x, intersect_y)

def get_cross_point_in_convex(line, convex):
    """
    선분과 컨벡스헐의 교차점을 찾는 함수
    """
    convex_lines = [ (convex[i], convex[i+1]) for i in range(len(convex) - 1) ]
    convex_lines.append((convex[-1], convex[0]))
                    
    cross_line = find_intersect(line, convex_lines)
    cross_point = get_cross_point(line, cross_line)

    return cross_point

def find_cross_points(convex_1, convex_2):
    """
    두 컨벡스헐 사이의 모든 교차점을 찾는 함수
    """
    convex_1_lines = [ (convex_1[i], convex_1[i+1]) for i in range(len(convex_1) - 1) ]
    convex_1_lines.append((convex_1[-1], convex_1[0]))
    
    convex_2_lines = [ (convex_2[i], convex_2[i+1]) for i in range(len(convex_2) - 1) ]
    convex_2_lines.append((convex_2[-1], convex_2[0]))

    cross_points = []
    for convex_1_line in convex_1_lines:
        for convex_2_line in convex_2_lines:
            if is_intersect(convex_1_line, convex_2_line):
                cross_point = get_cross_point(convex_1_line, convex_2_line)
                cross_points.append(cross_point)

    return cross_points

# 입력 받기
N, M = map(int, input().split())
convex_1 = [ tuple(map(int, input().split())) for _ in range(N) ]
convex_2 = [ tuple(map(int, input().split())) for _ in range(M) ]

# 컨벡스헐 내부의 점들과 교차 선분 찾기
in_points_1, cross_lines_1 = get_points_in_convex(convex_1, convex_2)
cross_points_1 = [ get_cross_point_in_convex(line, convex_2) for line in cross_lines_1 ]

in_points_2, cross_lines_2 = get_points_in_convex(convex_2, convex_1)
cross_points_2 = [ get_cross_point_in_convex(line, convex_1) for line in cross_lines_2 ]

# 두 컨벡스헐 간의 교차점 찾기
cross_points = find_cross_points(convex_1, convex_2)

# 교차점과 내부 점들을 합쳐 새로운 컨벡스헐을 생성
convex_points = in_points_1 + cross_points_1 + in_points_2 + cross_points_2 + cross_points
convex_points = set(convex_points)
if len(convex_points) < 3: 
    print(0)
    quit()

# 점들을 반시계 방향으로 정렬
sorted_convex_points = sort_points_ccw(convex_points)

# 컨벡스헐의 면적 계산
convex_area = polygon_area(sorted_convex_points)
print(f"{convex_area:.10f}")

# 디버깅 
if __name__ == "__debugging__":

    # 교차 컨벡스헐의 점들을 출력
    print(sorted_convex_points)

    def visualization(convex_1, convex_2, inter_convex):
        """
        컨벡스헐과 교차 컨벡스헐을 시각화하는 함수
        matplotlib 라이브러리 설치 필요
        """
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon

        polygon1 = convex_1
        polygon2 = convex_2
        polygon3 = inter_convex

        fig, ax = plt.subplots()

        poly1 = Polygon(polygon1, edgecolor='red', facecolor='red', alpha=0.5)
        ax.add_patch(poly1)

        poly2 = Polygon(polygon2, edgecolor='blue', facecolor='blue', alpha=0.5)
        ax.add_patch(poly2)

        poly3 = Polygon(polygon3, edgecolor='green', facecolor='green', alpha=0.5)
        ax.add_patch(poly3)

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        plt.show()

    # 두 컨벡스헐과 교차 컨벡스헐을 시각화
    visualization(convex_1, convex_2, sorted_convex_points)
