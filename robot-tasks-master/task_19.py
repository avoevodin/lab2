#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    action = move_left
    while wall_is_above() and not wall_is_on_the_right():
        action()
        if wall_is_on_the_left():
            action = move_right
    jailbreak_is_ok = not wall_is_above()
    while not wall_is_above():
        move_up()
    if jailbreak_is_ok:
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
