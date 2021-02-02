#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled_cells = 0
    while filled_cells < 5:
        move_right()
        filled_cells += cell_is_filled()


if __name__ == '__main__':
    run_tasks()
