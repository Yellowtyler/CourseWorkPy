from math import*
def funct(x):
    return x-1
def dif(x,difx = 0.000000001):
    lf = funct(x+ difx)
    rf = funct(x)
    return (lf-rf)/difx
def iter(x,e):
    i=0
    l = 1/dif(x)
    while True:
        x = x - l*funct(x)
        i+=1
        if(abs(funct(x))<e and i>=2000):
            break
    return x
print(iter(3,0.0001))