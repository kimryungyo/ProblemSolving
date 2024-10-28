A,R,D=[1000,900,500,400,100,90,50,40,10,9,5,4,1],"M CM D CD C XC L XL X IX V IV I".split(),dict(zip("IVXLCDM",(1,5,10,50,100,500,1000)))
def Z(n):
 E = ''
 for i in range(len(A)):E+=R[i]*(n//A[i]);n%=A[i]
 return E
def X(s):
 r=p=0
 for c in s:v=D[c];r+=v;r-=2*p if p<v else 0;p=v
 return r
for s in open(0).read().split()[1:]:print(Z(int(s)) if s.isdigit() else X(s))