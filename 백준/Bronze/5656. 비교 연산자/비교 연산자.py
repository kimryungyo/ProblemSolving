import sys
input = sys.stdin.read

data = input().strip().split('\n')
case_number = 1

for line in data:
    if line.strip() == '':
        continue

    a, op, b = line.split()
    a = int(a)
    b = int(b)

    if op == "E":
        break

    if op == ">":
        result = a > b

    elif op == ">=":
        result = a >= b

    elif op == "<":
        result = a < b

    elif op == "<=":
        result = a <= b

    elif op == "==":
        result = a == b

    elif op == "!=":
        result = a != b


    print(f"Case {case_number}: {'true' if result else 'false'}")
    case_number += 1

