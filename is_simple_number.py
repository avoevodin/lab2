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
    
print('Input positive int number:')
x = int(input())
if is_simple_number(x) == True:
    print("The number is simple")
else:
    print("The number isn't simple")