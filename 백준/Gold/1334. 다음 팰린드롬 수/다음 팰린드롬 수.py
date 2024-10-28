g=len;N=input();L=g(N);q=quit;i=int;p=print
if set(N)=={'9'}:p(i(N)+2);q()
H=N[:(L+1)//2];c=i(H+H[::-1] if L%2==0 else H+H[-2::-1]);R=str(i(H)+1)
if c>i(N):p(c);q()
if g(R)>g(H):p(i('1'+'0'*(L-1)+'1'));q()
p(i(R+R[::-1]) if L%2==0 else R+R[-2::-1])