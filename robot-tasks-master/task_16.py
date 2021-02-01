#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    action = move_up if wall_is_beneath() else move_down
    while wall_is_on_the_left() and wall_is_on_the_right():
        action()
    if wall_is_on_the_left():
        action = move_right
        break_condition = wall_is_on_the_right
    else:
        action = move_left
        break_condition = wall_is_on_the_left
    while not break_condition():
        action()


if __name__ == '__main__':
    run_tasks()
