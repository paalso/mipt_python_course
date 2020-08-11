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


def crosses_row(n):
    move_right()
    fill_cross()
    for _ in range(n - 1):
        move_right(5)
        fill_cross()


@task(delay=0.01)
def task_2_4():
    n = 10
    for _ in range(4):
        crosses_row(n)
        move_left((n - 1) * 4)
        move_down(4)
    crosses_row(n)
    move_left((n - 1) * 4)


if __name__ == '__main__':
    run_tasks()
