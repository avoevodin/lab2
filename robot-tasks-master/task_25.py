#!/usr/bin/python3

from pyrob.api import *

def fill_the_cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up(2)
    move_left()

@task
def task_2_2():
    move_down()
    for i in range(5):
        fill_the_cross()
        if i < 4:
            move_right(4)


if __name__ == '__main__':
    run_tasks()
