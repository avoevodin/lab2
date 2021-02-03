#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(12):
        action = move_right if i % 2 == 0 else move_left
        bound = 26 if i > 0 else 27
        for j in range(bound):
            action()
            fill_cell()
        move_down()
        if i < 11:
            fill_cell()


if __name__ == '__main__':
    run_tasks()
