#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        action1 = move_down
    else:
        action1 = move_up
    if wall_is_on_the_right():
        action2 = move_left
    else:
        action2 = move_right
    for i in range(9):
        action1()
        action2()


if __name__ == '__main__':
    run_tasks()
