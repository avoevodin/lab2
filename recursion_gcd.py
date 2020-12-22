'''Calculating of Grand Common Divisor with Euclidean algorithm.

'''

def get_gcd(num1, num2):
    '''Calculate gcd.
    num1, num2 -- input integer numbers for calculating gcd (int)

    '''
    return num1 if num2 == 0 else get_gcd(num2, num1 % num2)

def test_gcd():
    '''Common tests for module.

    '''
    num1 = 2
    num2 = 10
    test_case_gcd(num1, num2, 2, "1")

    num1 = 7
    num2 = 17
    test_case_gcd(num1, num2, 1, "2")

    num1 = 24
    num2 = 33
    test_case_gcd(num1, num2, 3, "3")

    num1 = 240
    num2 = 240
    test_case_gcd(num1, num2, 240, "4")

def test_case_gcd(num1, num2, gcd_fact, case_name):
    '''Test case for Euclidean algorithm.

    '''
    print("testcase #", case_name, ": ", end="")
    gcd_counted = get_gcd(num1, num2)
    print("Ok" if gcd_fact == gcd_counted else "Fail", gcd_counted, sep = '; ')

if __name__ == '__main__':
    test_gcd()
