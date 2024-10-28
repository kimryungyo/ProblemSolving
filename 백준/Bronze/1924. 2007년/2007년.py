D=['SUN','MON','TUE','WED','THU','FRI','SAT']
x,y=map(int,input().split())
M=[0,31,28,31,30,31,30,31,31,30,31,30,31]
T=sum(M[:x])+y
print(D[T%7])