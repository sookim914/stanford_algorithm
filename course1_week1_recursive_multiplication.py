# recurive multiplication using Karatsuba method
## assuming we can only do one digit multiplication
## can be slightly inaccurate due to rounding errors
def karatsuba (x,y):
    n = len(x)
    if n == 1:
        return int(x)*int(y)
    else:
        a = x[0:int(n/2)]
        b = x[int(n/2):int(n)]
        c = y[0:int(n/2)]
        d = y[int(n/2):int(n)]
        return (10**(n)*karatsuba(a,c)+karatsuba(b,d)+
               10**(n/2)*(karatsuba(a,d)+karatsuba(b,c)))
