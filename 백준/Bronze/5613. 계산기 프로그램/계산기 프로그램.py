def simple_calculator():
    import sys
    input = sys.stdin.read
    data = input().split()
    result = int(data[0])

    for i in range(1, len(data), 2):
        operator = data[i]

        if operator == '=':
            print(result)
            return
        
        next_number = int(data[i + 1])

        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number
        elif operator == '*':
            result *= next_number
        elif operator == '/':
            result //= next_number

simple_calculator()