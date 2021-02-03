#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while 1 == 1:
        exit_is_found = False
        while not wall_is_on_the_right():
            if wall_is_beneath():
                move_right()
            else:
                exit_is_found = True
                break
        while not exit_is_found and not wall_is_on_the_left():
            if wall_is_beneath():
                move_left()
            else:
                exit_is_found = True
        if not exit_is_found:
            break
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
