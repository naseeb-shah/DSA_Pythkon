def gcd(a,b):
    while a!=b:
        if a >b:
            a=a-b
        else :
            b=b-a
        
    return a

print(gcd(32,16))

# optimized
def higherCommonFactor(a,b):
    if b==0:
        return a
    return higherCommonFactor(b,a%b)

print(higherCommonFactor(16,32))