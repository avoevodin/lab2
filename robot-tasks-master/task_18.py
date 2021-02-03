#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.01)
def task_8_28():
    action = move_left
    while wall_is_above():
        if wall_is_on_the_left():
            action = move_right
        action()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()



if __name__ == '__main__':
    run_tasks()
