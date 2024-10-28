while True:
    N, *numbers = map(int, input().split())
    
    if N == 0: break
    
    bef = None
    for num in numbers:
        if num != bef:
            print(num, end = " ")
            bef = num
    
    print('$')