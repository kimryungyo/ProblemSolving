i=0;k=lambda q,p,o,e=1:print(f"Triangle #{i}\n"+(f"{q} = {r**.5:.3f}" if (r:=p*p-o*o*e)>0 else "Impossible.")+"\n")
while i:=i+1:
 a,b,c=map(int,input().split())
 if a==0:break
 if a<0:k("a",c,b)
 if b<0:k("b",c,a)
 if c<0:k("c",a,b,-1)