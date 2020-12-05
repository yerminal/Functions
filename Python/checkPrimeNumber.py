def checkPrimeNumber(number):
    if(number==2): return True
    if(number%2 == 0): return False
    for i in range(3,int((number/2)+1),2):
        if(number%i == 0): return False
    return True
