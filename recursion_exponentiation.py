'''Fast exponentiation.

'''

def elevate(num: float, deg: int):
    '''Elevate num to selected degree.
    num -- input float number for exponentiation (float)
    deg -- input degree (int)

    '''
    assert deg >= 0, "Degree must be positive."

    if deg == 0:
        res = 1
    elif deg % 2 == 0:
        res = elevate(num ** 2, deg // 2)
    else:
        res = elevate(num, deg - 1) * num
    return res

def test_elevate():
    '''Common tests for module.

    '''
    num = 2
    deg = 0
    res = 1
    test_case_elevate(num, deg, res, "1")

    num = 234
    deg = 1
    res = 234
    test_case_elevate(num, deg, res, "2")

    num = 25
    deg = 2
    res = 625
    test_case_elevate(num, deg, res, "3")

    num = 5
    deg = 3
    res = 125
    test_case_elevate(num, deg, res, "4")

    num = 6
    deg = -3
    res = 0
    test_case_elevate(num, deg, res, "5")

def test_case_elevate(num, deg, res, case_name):
    '''Test case for exponentiation.

    '''
    print("testcase #", case_name, ": ", end="")
    res_counted = elevate(num, deg)
    print("Ok" if res == res_counted else "Fail", res_counted, sep = '; ')

if __name__ == '__main__':
    test_elevate()
