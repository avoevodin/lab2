'''Sort list with fast-sort methods. In this module two methods are
realised: merge method and Tony Hoare sorting method.

'''
import time

def merge_sorted_parts(part1: list, part2: list):
    '''Merge two sorted arrays of numbers.
    Return one sorted list of numbers.

    Keyword arguments:
    part1 -- sorted list of integer numbers (list)
    part2 -- sorted list of integer numbers (list)

    '''
    part1_len = len(part1)
    part2_len = len(part2)
    res = []
    i = j = 0 # counters for part1 and part2
    while i < part1_len and j < part2_len:
        part1_el = part1[i]
        part2_el = part2[j]
        if part1_el <= part2_el:
            res.append(part1_el)
            i += 1
        else:
            res.append(part2_el)
            j += 1
    while i < part1_len:
        res.append(part1[i])
        i += 1
    while j < part2_len:
        res.append(part2[j])
        j += 1
    return res

def merge_sort(num_list: list):
    '''Sort list with merge-sort method.

    Keyword arguments:
    num_list -- current list of num for sorting (list)

    '''
    list_len = len(num_list)
    if list_len < 2:
        return
    middle = list_len // 2
    left_part = [num_list[i] for i in range(middle)]
    right_part = [num_list[i] for i in range(middle, list_len)]
    merge_sort(left_part)
    merge_sort(right_part)
    merged_list = merge_sorted_parts(left_part, right_part)
    for i in range(list_len):
        num_list[i] = merged_list[i]

def swap_elements(num_list: list, idx1: int, idx2: int):
    '''Swap two elements in selected list.

    Keyword arguments:
    num_list -- list of numbers (list)
    idx1, idx2 -- indexes of elements that should be swapped (int)

    '''
    tmp = num_list[idx1]
    num_list[idx1] = num_list[idx2]
    num_list[idx2] = tmp

def merge_sorted_parts_alt(num_list, left_side: int, middle: int,
    right_side: int):
    '''Merge sorted parts of selected list with less use of memory.

    Keyword arguments:
    num_list -- list of numbers (list)
    left_side, middle, right_side -- edges of sorted segments. First
            segment's from left_side to middle, and second segment's
            from (middle + 1) to right_sight (int)

    '''
    i = left_side
    j = middle + 1
    while i <= middle:
        if num_list[i] > num_list[j]:
            swap_elements(num_list, i, j)
            if j < right_side and num_list[j] > num_list[j + 1]:
                merge_sort_alt(num_list, j, right_side)
        i += 1

def merge_sort_alt(num_list, left_side: int = None, right_side: int = None):
    '''Sort list with memory-optimized merge-sort method.

    Keyword arguments:
    num_list -- list of numbers (list)
    left_side, right_side -- edges of sorted segment (int)

    '''
    if left_side is None:
        left_side = 0
        right_side = len(num_list) - 1
    elif left_side == right_side:
        return
    middle = (right_side + left_side) // 2
    merge_sort_alt(num_list, left_side, middle)
    merge_sort_alt(num_list, middle + 1, right_side)
    merge_sorted_parts_alt(num_list, left_side, middle, right_side)

def hoar_sort(num_list:list):
    '''Sort list with Tony Hoar method.

    Keyword arguments:
    num_list -- list of numbers (list)

    '''
    if len(num_list) < 2:
        return
    barrier = num_list[0]
    left_part = []
    middle_part = []
    right_part = []
    for elem in num_list:
        if elem < barrier:
            left_part.append(elem)
        elif elem == barrier:
            middle_part.append(elem)
        else:
            right_part.append(elem)
    hoar_sort(left_part)
    hoar_sort(right_part)
    i = 0
    for elem in left_part + middle_part + right_part:
        num_list[i] = elem
        i += 1

def test_sort(sort_algorithm):
    '''Tests for selected sort algorithm'''

    # Write a description of executable method
    alg_doc = sort_algorithm.__doc__
    idx_lb = alg_doc.index('.\n')
    print("Testing: ", alg_doc[:idx_lb])

    test_list = [4, 2, 5]
    list_sorted = [2, 4, 5]
    test_sort_case(test_list, list_sorted, sort_algorithm, "1")

    test_list = [4, 2, 5, 1, 3]
    list_sorted = [1, 2, 3, 4, 5]
    test_sort_case(test_list, list_sorted, sort_algorithm, "2")

    test_list = list(range(10, 20)) + list(range(10))
    list_sorted = list(range(20))
    test_sort_case(test_list, list_sorted, sort_algorithm, "3")

    test_list = [4, 2, 4, 2, 1]
    list_sorted = [1, 2, 2, 4, 4]
    test_sort_case(test_list, list_sorted, sort_algorithm, "4")

def test_sort_case(test_list, list_sorted, sort_algorithm, case_name):
    '''Testcase for selected sort algorithm'''

    print("testcase #", case_name, ": ", end="")
    sort_algorithm(test_list)
    print("Ok" if test_list == list_sorted else "Fail", test_list, sep = '; ')

if __name__ == "__main__":
    start_time = time.time()
    test_sort(merge_sort)
    print('t: ', '--- %s seconds ---' % (time.time() - start_time))

    start_time = time.time()
    test_sort(merge_sort_alt)
    print('t: ', '--- %s seconds ---' % (time.time() - start_time))

    test_sort(hoar_sort)
