from math import*
def funct(x):
    return cos(x)
def dih(x0,x1,e):
    i=0
    l=x0
    r=x1
    while True:
        x = (l+r)/2
        f = funct(x)
        if(f>0):
            r = x
        else:
            l=x
        i+=1
        if abs(f)<e and i>=2000:
         break
    return x
print(dih(-1,99,0.00001))




