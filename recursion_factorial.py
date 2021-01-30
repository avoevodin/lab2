'''Counting factorial with recursion

'''

def recursion_factorial(num):
    '''Count factorial for input number n

    Keyword arguments:
    n -- input number. n must be positive integer number.
         For n <= 1 function returns 1 (int)

    '''
    assert num >= 0, "Factorial of negative numbers is indefined"
    if num < 2:
        return 1
    return num * recursion_factorial(num - 1)

def test_factorial():
    '''Common tests for module.

    '''

    test_number = 5
    res_fact = 120
    test_factorial_case(test_number, res_fact, "1")

    test_number = 3
    res_fact = 6
    test_factorial_case(test_number, res_fact, "2")

    test_number = 8
    res_fact = 40320
    test_factorial_case(test_number, res_fact, "3")

    test_number = 0
    res_fact = 1
    test_factorial_case(test_number, res_fact, "4")

    test_number = -10
    res_fact = 1
    test_factorial_case(test_number, res_fact, "5")

def test_factorial_case(test_number, res_fact, case_name):
    '''Test case for recursion_factorial().

    '''
    print("testcase #", case_name, ": ", end="")
    res_fact_counted = recursion_factorial(test_number)
    print("Ok" if res_fact == res_fact_counted else "Fail", res_fact_counted, sep = '; ')

if __name__ == '__main__':
    test_factorial()
