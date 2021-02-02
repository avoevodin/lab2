#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    for i in range(13):
        move_down()
        fill_cell()
        j = 0
        for j in range(i):
            move_right()
            fill_cell()
        if i > 0:
            move_left(j + 1)
    move_down()


if __name__ == '__main__':
    run_tasks()
