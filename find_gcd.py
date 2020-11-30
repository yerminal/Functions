def find_gcd(a,b):
    #To make "a" small number, and "b" big number 
    if(a>b): 
        temp=a 
        a=b 
        b=temp
    #Backup for a and b
    small=a 
    big=b
    #Finding gcd
    while(1):
        remain=b%a
        if(remain==0): break
        a=remain
    #Checking the result whether it's true or not.
    #Actually, to find out the numbers have gcd "1"    
    if(small%a!=0 or big%a!=0):
        return 1
    return a
