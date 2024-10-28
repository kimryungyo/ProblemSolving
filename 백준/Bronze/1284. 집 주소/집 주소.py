while True:
    num = input()
    if num == '0': break
    
    width = 0
    
    for digit in num:
        if digit == '1': width += 2
        elif digit == '0': width += 4
        else: width += 3
    
    total_width = width + len(num) - 1 + 2
    
    print(total_width)