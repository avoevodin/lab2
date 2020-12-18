# Examples of sorts algorithms:
#   - Square sorts
#   - Count sort

def insert_sort(A):
    """Sorting of list A with inserts
    
    """
    len_A = len(A)
    for top in range(1, len_A):
        i = top
        while i > 0 and A[i] < A[i-1]: # i > 0 at the first place because
                                       # if i = 0, second operator won't be
                                       # calculated
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1 
                    

def choice_sort(A):
    """Sorting of list A with choices
    
    """
    len_A = len(A)
    for pos in range(len_A - 1):
        for i in range(pos + 1, len_A):
            if A[i] < A[pos]:
                A[pos], A[i] = A[i], A[pos]
    
def bubble_sort(A):
    """Sorting of list A with bubble-sort method
    
    """
    len_A = len(A)
        
    for bypass in range(1, len_A):
        for i in range(0, len_A - bypass):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]   

def count_sort(A):
    """Sorting of list A with count-sort method.
    Digits in the list must be less than 20.
    
    """
    len_A = len(A)
    max_digit = 20
    F = [0] * max_digit
    for i in range(len_A):
        F[A[i]] += 1
    A.clear()
    for digit in range(max_digit):
        A += [digit] * F[digit]
    
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
    print("Ok" if A == A_sorted else "Fail", A, sep = '; ')
    
if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
    test_sort(count_sort)