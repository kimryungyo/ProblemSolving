def m():
 if (N:=int(input()))<131:print(str(int("ttyzfznhlwhikqzhe4rqie0j8rizzhkwvrwrcjzocfd923abt40aotsytgmhlkx4jbclu5iv0zm1ckxnib9",36))[N-1]);quit()
 h,t,y={1},{},{};b,k=1,2
 while b<=N:b+=k*4-3;h.add(b);k+=1
 t=h;y={x+y for x in t for y in t};print(1 if N in t else 2 if N in y else 3 if any(N-x in y for x in t) else 4)
m()