#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    filled_cells = 0
    while filled_cells < 3 and not wall_is_on_the_right():
        move_right()
        filled_cells = filled_cells + 1 if cell_is_filled() else 0


if __name__ == '__main__':
    run_tasks()
