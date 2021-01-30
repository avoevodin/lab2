'''Generating permutations for list of numbers.

'''
def find_number(prefix, number):
    '''Find selected number in current prefix of permutations.
    If number is found, returns True, else False.

    Keyword arguments:
    prefix -- list of numbers (list)
    number -- number for checking (int)

    '''
    res = False
    for i in prefix:
        if i == number:
            res = True
            break
    return res

def generate_permutations(num_amount: int, pos_amount: int = -1, prefix = None):
    '''Generate all permutations for num_amount numbers in pos_amount
    positions with prefix.

    Keyword arguments:
    num_amount -- numbers from 1 to num_amount are the numbers for
                  generating permutations (int)
    pos_amount -- amount of rest positions for generating permutations
                  with current prefix (int)
    prefix -- generated part of permutation (list)

    '''
    # num_amount numbers in num_amount positions by default
    pos_amount = num_amount if pos_amount == -1 else pos_amount
    prefix = prefix or []
    if pos_amount == 0:
        print(*prefix)
        return
    for number in range(1, num_amount + 1):
        if find_number(prefix, number):
            continue
        prefix.append(number)
        generate_permutations(num_amount, pos_amount - 1, prefix)
        del prefix[-1]

def test_permutations():
    '''Common test for permutations.

    '''
    test_case_gen_numbers(3, "1")
    test_case_gen_numbers(4, "2")
    test_case_gen_numbers(5, "3")

def test_case_gen_numbers(num_base, case_name):
    '''Test case for generating numbers.

    '''
    print("testcase #", case_name, sep = ": ")
    generate_permutations(num_base)

if __name__ == '__main__':
    test_permutations()
