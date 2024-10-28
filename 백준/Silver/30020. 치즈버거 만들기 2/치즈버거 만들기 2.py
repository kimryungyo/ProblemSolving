def m():
 P,C=map(int,input().split())
 p=print
 B=P-C
 if 0<B<=C:
  p("YES",B,sep="\n")
  S=B-1
  p("aba\n"*S,end="")
  p("ab"*(C-S),"a",sep="")
 else:p("NO")
m()