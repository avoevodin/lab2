# Examples of sorts algorithms:
#     - Square sorts

def insert_sort(A):
    """Sorting of list A with inserts
    
    """
    pass

def choice_sort(A):
    """Sorting of list A with choices
    
    """
    pass

def bubble_sort(A):
    """Sorting of list A with bubble-sort method
    
    """
    pass
    
def test_sort(sort_algorithm):
    print("Testing: ", sort_algorithm.__doc__.rstrip())
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    test_sort_case(A, A_sorted, sort_algorithm, "1")
    
    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    test_sort_case(A, A_sorted, sort_algorithm, "2")
    
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    test_sort_case(A, A_sorted, sort_algorithm, "3")
    
def test_sort_case(A, A_sorted, sort_algorithm, case_name):
    print("testcase #", case_name, ": ", end="")
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    
if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)