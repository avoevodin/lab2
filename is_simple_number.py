# Samble of function, that can define prime number

def is_simple_number(x):
    """Define is number simple or not.
       If number is simple, returns True, else returns False
       x -- selected positive number (0)
       
    """
    divisor = 2
    is_simple = True
    while divisor < x / 2 and is_simple == True:
        is_simple = x % divisor != 0
        divisor += 1
    return is_simple

def factorize_number(x):
    """Factorize number to it's multiplicators.
       Print these multiplicators in a row with divisor ' * '.
    
    """
    divisor = 2
    res = []
    res_str = ''
    while x > 1:
        if x % divisor == 0:
            res.append(divisor)
            x //= divisor
        else:
            divisor += 1
    else: 
        res.append(1)
    
    first_step = 1
    for i in res:
        if first_step:
            sep = ''
            first_step = 0
        else:
            sep = ' * '
        res_str += sep + str(i) 
    print(res_str)           
        
print('Input positive int number:')
x = int(input())
if is_simple_number(x) == True:
    print("The number is simple")
else:
    print("The number isn't simple")
    
factorize_number(x)