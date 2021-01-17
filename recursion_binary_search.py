'''Binary search.

'''

def left_bound(num_list: list, key: int):
    '''Search left bound for target interval of found numbers.

    Keyword arguments:
    num_list -- list of numbers (list)
    key -- number that's searched for (int)

    '''
    left = -1
    right = len(num_list)
    while right - left > 1:
        middle = (left + right) // 2
        if num_list[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(num_list: list, key: int):
    '''Search right bound for target interval of found numbers.

    Keyword arguments:
    num_list -- list of numbers (list)
    key -- number that's searched for (int)

    '''
    left = -1
    right = len(num_list)
    while right - left > 1:
        middle = (left + right) // 2
        if num_list[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def find_number(num_list: list, key: int):
    '''Search selected number in the list.

    Keyword arguments:
    num_list -- list of numbers (list)
    key -- number that's searched for (int)

    '''
    left = left_bound(num_list, key)
    right = right_bound(num_list, key)
    return generate_result(left, right)

def generate_result(left, right):
    '''Generate result with left and right bound of found interval.

    '''
    if right - left == 1:
        res = "Number wasn't found"
    elif right - left == 2:
        res = "Number's index is " + str(left + 1)
    else:
        res = ("Searched number's indexes are from " + str(left + 1)
            + " to " + str(right - 1))
    return res

def test_binary_search():
    '''Common tests for module.

    '''
    num_list = [1, 2, 5, 8, 10, 24, 48, 100, 120]
    key = 10
    res = generate_result(3, 5)
    test_case_binary_search(num_list, key, res, "1")

    num_list = list(range(977))
    key = 483
    res = generate_result(482, 484)
    test_case_binary_search(num_list, key, res, "2")

    num_list = [1, 2, 4, 5, 5, 5, 9, 17, 17]
    key = 5
    res = generate_result(2, 6)
    test_case_binary_search(num_list, key, res, "3")

    num_list = [1, 2, 5, 8, 9, 11, 14, 14, 16]
    key = 17
    res = generate_result(8, 9)
    test_case_binary_search(num_list, key, res, "4")

    num_list = [2, 2, 4, 88, 99, 110, 140, 141, 141]
    key = 1
    res = generate_result(-1, 0)
    test_case_binary_search(num_list, key, res, "5")

def test_case_binary_search(num_list, key, res, case_name):
    '''Test case for binary search.

    '''
    print("testcase #", case_name, ": ", end="")
    res_counted = find_number(num_list, key)
    print("Ok" if res == res_counted else "Fail", end = ":\n")
    print(res, res_counted, sep = "\n")

if __name__ == '__main__':
    test_binary_search()
