T = int(input())

for _ in range(T):
    PS = input()
    count = 0
    
    for p in PS:
        if p == '(': count += 1
        else: count -= 1
        
        if count < 0:
            print("NO")
            break
    else:
        if count == 0: print("YES")
        else: print("NO")