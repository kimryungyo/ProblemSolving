from sys import stdin
input = lambda: stdin.readline().rstrip()

for _ in range(int(input())):
    value, unit = input().split()
    value = float(value)
    
    if unit == 'kg':
        convert = value * 2.2046
        convert_unit = 'lb'
    elif unit == 'lb':
        convert = value * 0.4536
        convert_unit = 'kg'
    elif unit == 'l':
        convert = value * 0.2642
        convert_unit = 'g'
    elif unit == 'g':
        convert = value * 3.7854
        convert_unit = 'l'
    
    print(f'{convert:.4f} {convert_unit}')