#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    while True:
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
