from math import gcd

class CannotConvertToInt(Exception): ...

class Fraction():
    """나눗셈 오차값 제거를 위한 분수 클래스"""
    def __init__(self, numerator, denominator = 1):
        if type(numerator) == Fraction: numerator = numerator.integer()
        if type(denominator) == Fraction: denominator = denominator.integer()

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
    
    def integer(self):
        value = self.nume / self.deno
        if value % 1 != 0: raise CannotConvertToInt()
        return int(value)

class NonVerticalLineError(Exception): ...
class VerticalLineError(Exception): ...

class VerticalLine():
    def __init__(self, p1, p2):
        if p1[0] != p2[0]: raise NonVerticalLineError
        self.x = p1[0]
        self.y_range = sorted([p1[1], p2[1]])

class EquationLine():
    def __init__(self, p1, p2):
        if p1[0] == p2[0]: raise VerticalLineError
        dx, dy = Fraction(p2[0] - p1[0]), Fraction(p2[1] - p1[1])
        self.slope = dy / dx
        self.intercept = Fraction(p1[1]) - (self.slope * Fraction(p1[0]))
        self.x_range = sorted([p1[0], p2[0]])

    def get_value(self, x):
        return (self.slope * x) + self.intercept
    
    def __str__(self):
        return f"(y = {self.slope}x + {self.intercept})"

class Linear():
    def __init__(self, p1, p2):
        if p1[0] == p2[0]: 
            self.type = "vertical"
            self.equation = VerticalLine(p1, p2)
        else:
            self.type = "equation"
            self.equation = EquationLine(p1, p2)

def is_value_in_ranges(x, ranges):
    for r in ranges:
        if x < r[0] or x > r[1]: return False
    return True

def check_overlap(range1, range2):
    if range1[1] < range2[0]: return False
    if range2[1] < range1[0]: return False
    return True

def is_cross_verticals(line1: Linear, line2: Linear):
    if line1.equation.x != line2.equation.x: return False
    if not check_overlap(line1.equation.y_range, line2.equation.y_range): return False
    return True

def is_cross_vertical_and_slope(vertical: Linear, slope: Linear):
    x = vertical.equation.x
    y_range = vertical.equation.y_range
    x_range = slope.equation.x_range

    if not is_value_in_ranges(x, [x_range]): return False
    
    y = slope.equation.get_value(x)
    if not is_value_in_ranges(y, [y_range]): return False

    return True

def is_cross_equations(line1: Linear, line2: Linear):
    a = line1.equation.slope - line2.equation.slope
    b = line1.equation.intercept - line2.equation.intercept
    ranges = [line1.equation.x_range, line2.equation.x_range]

    if a == Fraction(0): 
        if b == Fraction(0):
            if check_overlap(*ranges): return True
            else: return False
        else: return False

    solution = (Fraction(-1) * b) / a
    
    if is_value_in_ranges(solution, ranges): return True
    else: return False

def is_cross_line(line1: Linear, line2: Linear):
    lines = [ line1, line2 ]
    types = [ line.type for line in lines ]
    if types.count("vertical") == 0:
        return is_cross_equations(line1, line2)
    
    if types.count("vertical") == 1:
        vertical = lines.pop(types.index("vertical"))
        slope = lines.pop()
        return is_cross_vertical_and_slope(vertical, slope)
    
    if types.count("vertical") == 2:
        return is_cross_verticals(line1, line2)

p1 = [ Fraction(int(v)) for v in input().split() ]
p2 = [ Fraction(int(v)) for v in input().split() ]
line1 = Linear((p1[0], p1[1]), (p1[2], p1[3]))
line2 = Linear((p2[0], p2[1]), (p2[2], p2[3]))

print(int(is_cross_line(line1, line2)))