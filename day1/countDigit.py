def countDigit(num):
    count=1
    while  num>10:
        num=num/10
        print(num)
        count+=1

    return count 
print(countDigit(266333))