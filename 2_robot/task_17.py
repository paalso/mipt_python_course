#!/usr/bin/python3

from pyrob.api import *

def find_filled():
    while True:
        if cell_is_filled():
            break
        move_up()


@task
def task_8_27():
    find_filled()
    move_left()
    if not cell_is_filled():
        move_right()
        move_right()


if __name__ == '__main__':
    run_tasks()
