#!/usr/bin/python3

from pyrob.api import *


def get_reverse_move(move):
    if move == move_right:
        result = move_left
    elif move == move_down:
        result = move_up
    elif move == move_left:
        result = move_right
    elif move == move_up:
        result = move_down
    return result


def get_down_restriction(move_f):
    if move_f == move_right:
        result = wall_is_above
    elif move_f == move_down:
        result = wall_is_on_the_right
    elif move_f == move_left:
        result = wall_is_beneath
    elif move_f == move_up:
        result = wall_is_on_the_left
    return result


def get_forward_restriction(move_f):
    if move_f == move_right:
        result = wall_is_on_the_right
    elif move_f == move_down:
        result = wall_is_beneath
    elif move_f == move_left:
        result = wall_is_on_the_left
    elif move_f == move_up:
        result = wall_is_above
    return result

def get_move_up_action(move_f):
    if move_f == move_right:
        result = move_down
    elif move_f == move_down:
        result = move_left
    elif move_f == move_left:
        result = move_up
    elif move_f == move_up:
        result = move_right
    return result


def fill_tryangle(row, move_f, stay_at_start = False):
    move_b = get_reverse_move(move_f)
    move_u = get_move_up_action(move_f)
    move_d = get_reverse_move(move_u)
    down_restriction = get_down_restriction(move_f)
    forward_restriction = get_forward_restriction(move_f)
    while row > 0:
        for i in range(row):
            move_f()
            fill_cell()
        if row > 2:
            move_b(row - 1)
            move_u()
        row -= 2
    while not down_restriction():
        move_d()
    while not stay_at_start and not forward_restriction():
        move_f()


@task(delay=0.01)
def task_9_3():
    base_row_width = 0
    while not wall_is_on_the_right():
        move_right()
        base_row_width += not wall_is_on_the_right()
    row = base_row_width
    move_left(row + 1)
    fill_tryangle(row, move_right)
    fill_tryangle(row, move_down)
    fill_tryangle(row, move_left)
    fill_tryangle(row, move_up, True)
    while not wall_is_beneath():
        move_down()

if __name__ == '__main__':
    run_tasks()
