def check_prime_number(number):
    if((number%2==0 and number!=2) or number==1): return False
    for i in range(3,int((number/2)+1),2):
        if(number%i == 0): return False
    return True
