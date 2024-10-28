E,N,*W=open(0).read().split()
for k in range(26):
 if any(w in(d:=''.join(chr((ord(c)+k-97)%26+97)for c in E))for w in W):print(d);quit()