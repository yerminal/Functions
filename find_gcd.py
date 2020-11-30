def find_gcd(a,b):
    if(a>b): 
        temp=a 
        a=b 
        b=temp
    small=a
    big=b
    while(1):
        remain=b%a
        if(remain==0): break
        a=remain
    if(small%a!=0 or big%a!=0):
        return 1
    return a
