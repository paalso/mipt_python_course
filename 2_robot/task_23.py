#!/usr/bin/python3

from pyrob.api import *


def fill_column():
    while not wall_is_above():
        fill_cell()
        move_up()
    fill_cell()
    while not wall_is_beneath():
        fill_cell()
        move_down()


def move_along():
    while True:
        if not wall_is_above():
            move_up()
            fill_column()
        if wall_is_on_the_right():
            break
        move_right()


def return_to_start():
    while wall_is_beneath():
        move_left()


@task(delay=0.1)
def task_6_6():
    move_right()
    move_along()
    return_to_start()


if __name__ == '__main__':
    run_tasks()
