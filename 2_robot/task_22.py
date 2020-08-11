#!/usr/bin/python3

from pyrob.api import *


def fill_row_to_right():
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    fill_cell()
    while not wall_is_on_the_left():
        move_left()


@task
def task_5_10():
    move_up = True if not wall_is_above() else False

    if move_up:
        while True:
            fill_row_to_right()
            if wall_is_above():
                break
            move_up()
    else:
        while True:
            fill_row_to_right()
            if wall_is_beneath():
                break
            move_down()


if __name__ == '__main__':
    run_tasks()