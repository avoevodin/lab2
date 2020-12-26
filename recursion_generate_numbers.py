'''Generating all the numbers before selected number.

'''
def generate_numbers(num_base: int, dig_amount: int, prefix = None):
    '''Generating numbers with selected digits amount.
    num_base -- base of number (int)
    dig_amount -- digits amount of numbers (int)
    prefix -- current list of generated digits (list
    )
    '''
    prefix = prefix or []
    if dig_amount == 0:
        print(prefix)
        return
    for i in range(num_base):
        prefix.append(i)
        generate_numbers(num_base, dig_amount - 1, prefix)
        del prefix[-1]

def test_generate_numbers():
    '''Common tests for module.

    '''
    num_base = 10
    dig_amount = 2
    test_case_gen_numbers(num_base, dig_amount, "1")

    num_base = 4
    dig_amount = 4
    test_case_gen_numbers(num_base, dig_amount, "2")

    num_base = 2
    dig_amount = 4
    test_case_gen_numbers(num_base, dig_amount, "3")

def test_case_gen_numbers(num_base, dig_amount, case_name):
    '''Test case for generating numbers.

    '''
    print("testcase #", case_name, sep = ": ")
    generate_numbers(num_base, dig_amount)

if __name__ == '__main__':
    test_generate_numbers()
