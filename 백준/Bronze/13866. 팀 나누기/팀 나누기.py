A,B,C,D=map(int,input().split())
print(min(abs(A+B-C-D),abs(A+C-B-D),abs(A+D-B-C)))