#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    counter = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            counter += 1
            if counter == 3:
                break
        else:
            counter = 0
        move_right()


if __name__ == '__main__':
    run_tasks()
