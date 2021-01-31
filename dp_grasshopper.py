"""Generate grasshopper's routs into selected step. It can move in 1, 2 or 3
   steps forward. Some steps may be not allowed for hop.

"""


def count_gh_routs(final_step: int, allowed_steps: list):
    """Calculate amount of grasshopper's routs to get the final_step.

    Keyword arguments:
    final_step -- the destination of grasshopper (int)
    allowed_steps -- allowed steps for grasshopper (list)

    """
    res_list = ([1, allowed_steps[1] * 2, allowed_steps[2]
                 * (allowed_steps[1] * 2 + 2)] + [0]
                * (final_step - 3))
    i = 0
    if final_step > 3:
        for i in range(3, final_step):
            if allowed_steps[i]:
                res_list[i] = res_list[i - 1] + res_list[i - 2] + res_list[i - 3]
    else:
        i = final_step - 1
    return res_list[i]


def test_gh():
    """Common tests for module.

    """
    final_step = 3
    res = 4
    test_case_gh(final_step, res, None, "1")

    final_step = 4
    res = 7
    test_case_gh(final_step, res, None, "2")

    final_step = 5
    res = 13
    test_case_gh(final_step, res, None, "3")

    final_step = 6
    res = 24
    test_case_gh(final_step, res, None, "4")

    final_step = 3
    res = 2
    test_case_gh(final_step, res, [1, 0, 1], "5")

    final_step = 4
    res = 0
    test_case_gh(final_step, res, [1, 0, 1, 0], "6")

    final_step = 4
    res = 3
    test_case_gh(final_step, res, [1, 0, 1, 1], "7")

    final_step = 4
    res = 3
    test_case_gh(final_step, res, [1, 1, 0, 1], "8")

    final_step = 5
    res = 5
    test_case_gh(final_step, res, [1, 1, 0, 1, 1], "9")

    final_step = 5
    res = 6
    test_case_gh(final_step, res, [1, 1, 1, 0, 1], "10")


def test_case_gh(final_step, res, allowed_steps, case_name):
    """Test case for grasshopper's routs.

    """
    print("testcase #", case_name, ": ", end="")
    allowed_steps = ([1] * final_step if allowed_steps is None else
                     allowed_steps)
    res_counted = count_gh_routs(final_step, allowed_steps)
    print("Ok" if res == res_counted else "Fail", res_counted, sep=": ")


if __name__ == "__main__":
    test_gh()
