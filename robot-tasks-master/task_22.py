#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_5_10():
    action = move_right
    shift_condition = wall_is_on_the_right
    while 1 == 1:
        if shift_condition():
            fill_cell()
            if wall_is_beneath() and wall_is_on_the_left():
                break
            if not wall_is_beneath():
                move_down()
            action = move_right if action == move_left else move_left
            shift_condition = wall_is_on_the_left if \
                shift_condition == wall_is_on_the_right \
                else wall_is_on_the_right
        if not cell_is_filled():
            fill_cell()
        action()


if __name__ == '__main__':
    run_tasks()
