from sys import stdin
input = lambda: stdin.readline().rstrip()

string = input()
leng = len(string)
for length in range(1, 4):
    A = int(string[:length])
    
    num = A
    idx = 0
    while idx < leng:
        num_str = str(num)
        if string[idx:idx+len(num_str)] != num_str: break
        idx += len(num_str)
        num += 1
    
    if idx == leng: 
        print(A, num - 1)
        break