#!/usr/bin/python3

from pyrob.api import *


def fill_row(n):
    for _ in range(n):
        move_right()
        fill_cell()


def return_to_start(n):
    for _ in range(n):
        move_left()


@task(delay=0.05)
def task_4_11():
    for i in range(1, 14):
        move_down()
        fill_row(i)
        return_to_start(i)

    move_down()
    move_right()



if __name__ == '__main__':
    run_tasks()
