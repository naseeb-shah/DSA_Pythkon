def plainDromic(n):
    rev=0
    temp=n
    while temp !=0:
        mode=temp%10
        rev=rev*10+mode
        temp=temp//10
    
    return rev==n

print(plainDromic(1231))