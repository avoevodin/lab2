#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    step = 1
    move_right()
    fill_cell()
    while 1 == 1:
        i = 0
        while i < step and not wall_is_on_the_right():
            move_right()
            i += 1
        if wall_is_on_the_right():
            break
        else:
            fill_cell()
        step += 1


if __name__ == '__main__':
    run_tasks()
