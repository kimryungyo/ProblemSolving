h,v=map(float,input().split());d=(h*h+v*v)**.5;a=v*(h/(h+d));b=v*(d/(h+d));c=(a*a+h*h)**.5;print(f"{c/2:.2f} {(b*h)/c:.2f}")