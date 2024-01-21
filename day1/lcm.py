def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def lcm(a,b):
    return a*b//gcd(a,b)



num1 = 24
num2 = 36

gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
