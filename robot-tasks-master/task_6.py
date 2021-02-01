#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    wall_started = wall_is_beneath()
    while not wall_started or wall_is_beneath():
        wall_started = wall_started if wall_started else wall_is_beneath()
        move_right()


if __name__ == '__main__':
    run_tasks()
