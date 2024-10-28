from math import gcd

class Fraction():
    """나눗셈 오차값 제거를 위한 분수 클래스"""
    def __init__(self, numerator, denominator):
        if denominator == 0: raise ZeroDivisionError()
        
        if denominator < 0: 
            numerator = numerator * -1
            denominator = denominator * -1

        g_c_d = gcd(numerator, denominator)
        self.nume = numerator // g_c_d
        self.deno = denominator // g_c_d

    def __add__(self, other):
        nume = self.nume * other.deno + other.nume * self.deno
        deno = self.deno * other.deno
        return Fraction(nume, deno)

    def __sub__(self, other):
        nume = self.nume * other.deno - other.nume * self.deno
        deno = self.deno * other.deno
        return Fraction(nume, deno)

    def __mul__(self, other):
        nume = self.nume * other.nume
        deno = self.deno * other.deno
        return Fraction(nume, deno)

    def __truediv__(self, other):
        nume = self.nume * other.deno
        deno = self.deno * other.nume
        return Fraction(nume, deno)

    def __eq__(self, other):
        return self.nume * other.deno == other.nume * self.deno

    def __lt__(self, other):
        return self.nume * other.deno < other.nume * self.deno

    def __gt__(self, other):
        return self.nume * other.deno > other.nume * self.deno

    def __str__(self):
        return f"({self.nume}/{self.deno})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nume}, {self.deno})"

    def __hash__(self):
        return hash((self.nume, self.deno))
    
    def float(self):
        return self.nume / self.deno

def is_value_in_ranges(x, ranges):
    """해당 값이 범위 내에 존재하는지 확인하는 함수"""
    for r in ranges:
        if x < r[0] or x > r[1]: return False
    return True

def check_overlap(range1, range2):
    """두 범위가 겹치는지 확인하는 함수"""
    if range1[1] < range2[0]: return False
    if range2[1] < range1[0]: return False
    return True

def find_linear_equation(x1, y1, x2, y2):
    """1차 방정식을 구하는 함수"""
    xd = x2 - x1
    yd = y2 - y1

    slope = yd / xd
    intercept = (y1 - (slope * x1))

    eq_range = sorted([x1, x2])
    equation = ("slope", slope, intercept, eq_range)
    return equation

def solve_linear(equation):
    """1차 방정식의 근이 존재하는지 확인하는 함수
    모든 값이 0인 상수 함수인 경우 True를 반환"""
    a = equation[1]
    b = equation[2]

    if a == Fraction(0, 1): 
        if b == Fraction(0, 1): return True
        else: return None

    solution = (Fraction(-1, 1) * b) / a
    return solution

def get_equation_value(equation, x):
    """함수값을 구하는 함수"""
    if equation[0] == "slope":
        return (equation[1] * x) + equation[2]

# 좌표 입력
x1, y1, x2, y2 = ( Fraction(int(p), 1) for p in input().split() )
x3, y3, x4, y4 = ( Fraction(int(p), 1) for p in input().split() )

# 두 점이 같은 경우
points = { (x1, y1), (x2, y2), (x3, y3), (x4, y4) }
if len(points) < 4:
    print(1)
    quit()

# 수식 구하기
if x1 == x2: eq1 = ("vertical", x1, None, sorted([y1, y2]))
else: eq1 = find_linear_equation(x1, y1, x2, y2)

if x3 == x4: eq2 = ("vertical", x3, None, sorted([y3, y4]))
else: eq2 = find_linear_equation(x3, y3, x4, y4)

# 1번 수식만 수직 함수인 경우
if eq1[0] == "vertical" and eq2[0] == "slope":
    if is_value_in_ranges(eq1[1], [eq2[3]]):
        value = get_equation_value(eq2, eq1[1])
        if is_value_in_ranges(value, [eq1[3]]):
            print(1)
            quit()

# 2번 수식만 수직 함수인 경우
elif eq1[0] == "slope" and eq2[0] == "vertical":
    if is_value_in_ranges(eq2[1], [eq1[3]]):
        value = get_equation_value(eq1, eq2[1])
        if is_value_in_ranges(value, [eq2[3]]):
            print(1)
            quit()

# 둘 다 수직 함수인 경우
elif eq1[0] == "vertical" and eq2[0] == "vertical":
    if eq1[1] == eq2[1]:
        if check_overlap(eq1[3], eq2[3]):
            print(1)
            quit()

# 일반적인 경우
elif eq1[0] == "slope" and eq2[0] == "slope":
    result_equation = ("slope", eq1[1] - eq2[1], eq1[2] - eq2[2], [eq1[3], eq2[3]])
    value = solve_linear(result_equation)

    # 결과값 처리
    if type(value) == Fraction:
        if is_value_in_ranges(value, result_equation[3]):
            print(1)
            quit()

    # 실수 전체에서 0인 경우
    elif value == True:
        if check_overlap(*result_equation[3]):
            print(1)
            quit()

# 위에 해당되지 않는 경우 0 출력
print(0)