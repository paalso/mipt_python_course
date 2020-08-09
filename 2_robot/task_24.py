#!/usr/bin/python3

from pyrob.api import *


def fill_cross():
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right(2)
    for _ in range(3):
        move_left()
        fill_cell()
    move_up()


@task
def task_2_1():
    move_down()
    move_right(2)
    fill_cross()


if __name__ == '__main__':
    run_tasks()
