#!/usr/bin/python3

from pyrob.api import *


def fill_cross():
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    for _ in range(2):
        fill_cell()
        move_left()
    fill_cell()
    move_up()


@task
def task_2_2():
    move_down()
    move_right()
    fill_cross()
    for _ in range(4):
        move_right(5)
        fill_cross()


if __name__ == '__main__':
    run_tasks()
