def octal_to_binary():
    import sys
    input = sys.stdin.read
    
    octal_num = input().strip()
    decimal_num = int(octal_num, 8)

    binary_num = bin(decimal_num)[2:]
    print(binary_num)

octal_to_binary()