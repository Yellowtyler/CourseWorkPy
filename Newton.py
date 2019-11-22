from math import*

def funct(x):
    return x*x -1
def dif(x,difx = 0.000000001):
    lf = funct(x+ difx)
    rf = funct(x)
    return (lf-rf)/difx
def newton(x,e):
 i=0
 while True:
     df = dif(x)
     f = funct(x)
     x = x - f/df
     i+=1
     if(abs(f)<e and i>=2000):
         break
 return x
print(newton(3,0.000001))
