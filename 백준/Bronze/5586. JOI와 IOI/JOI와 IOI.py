s=input()
a=b=0
if len(s)>2:
 for i in range(len(s)-2):
  if s[i:i+3]=="JOI":a+=1
  if s[i:i+3]=="IOI":b+=1
print(a)
print(b)