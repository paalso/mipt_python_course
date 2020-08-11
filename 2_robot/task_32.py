#!/usr/bin/python3

from pyrob.api import *


def move_up_and_down():
    counter = 0
    while True:
        if not cell_is_filled():
            fill_cell()
        else:
            counter += 1
        if wall_is_above():
            break
        move_up()
    while not wall_is_beneath():
        move_down()
    return counter


@task(delay=0.01)
def task_8_18():
    counter = 0
    while not wall_is_on_the_right():
        if not wall_is_above():
            move_up()
            counter += move_up_and_down()
        elif cell_is_filled():
            counter += 1
        else:
            fill_cell()
        move_right()
    mov('ax', counter)
    print(counter)


if __name__ == '__main__':
    run_tasks()