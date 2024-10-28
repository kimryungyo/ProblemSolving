import itertools;N,M=map(int,input().split());n=list(map(int,input().split()));p=set()
for q in sorted(itertools.permutations(n,M)):
 s=' '.join(map(str,q))
 if s in p:continue
 p.add(s);print(s)