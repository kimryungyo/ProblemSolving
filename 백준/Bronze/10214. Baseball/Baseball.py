for _ in range(int(input())):
    yonsei_total = 0
    korea_total = 0
    
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei_total += y
        korea_total += k
        
    if yonsei_total > korea_total:
        print("Yonsei")
    elif korea_total > yonsei_total:
        print("Korea")
    else:
        print("Draw")
