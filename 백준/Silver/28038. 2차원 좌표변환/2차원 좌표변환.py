import math
import sys

def format_num(x):
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    else:
        s = f"{x:.8f}".rstrip('0').rstrip('.')
        return s if s else '0'

def read_non_empty_lines(lines):
    for line in lines:
        stripped = line.strip()
        if stripped:
            yield stripped

def cartesian_to_polar(x, y):
    if abs(x) < 1e-9 and abs(y) < 1e-9:
        return 0.0, 0.0
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    if theta < 0:
        theta += 2 * math.pi
    return r, theta

def polar_to_cartesian(r, theta):
    if abs(r) < 1e-9:
        return 0.0, 0.0
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def main():
    input_lines = sys.stdin.read().splitlines()
    lines = read_non_empty_lines(input_lines)
    lines = iter(lines)
    
    try:
        T = int(next(lines))
    except StopIteration:
        T = 0

    for _ in range(T):
        try:
            coord_type = int(next(lines))
            a, b = map(float, next(lines).split())
        except StopIteration:
            break
        
        if coord_type == 1:
            r, theta = cartesian_to_polar(a, b)
            out_r = format_num(r)
            out_theta = format_num(theta)
            print(f"{out_r} {out_theta}")
        elif coord_type == 2:
            x, y = polar_to_cartesian(a, b)
            out_x = format_num(x)
            out_y = format_num(y)
            print(f"{out_x} {out_y}")
        else:
            print("Invalid coordinate type")

if __name__ == "__main__":
    main()