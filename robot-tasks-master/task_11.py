#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    while 1 == 1:
        if wall_is_above() == wall_is_beneath() is True:
            fill_cell()
        if not wall_is_on_the_right():
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()
