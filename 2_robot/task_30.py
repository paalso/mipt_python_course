#!/usr/bin/python3

from pyrob.api import *


def get_row_start():
    while not wall_is_on_the_left():
        move_left()


def explore_field_size():
    counter = 1
    while not wall_is_on_the_right():
        move_right()
        counter += 1
    return counter



@task(delay=0.2)
def task_9_3():
    size = explore_field_size()
##    print(size)
    get_row_start()

    i = 1
    while i <= size:
        j = 1
        while j <= size:
            if i != j and i + j != size + 1:
                fill_cell()
            if j == size:
                break
            j += 1
            move_right()
        get_row_start()
        if i < size:
            move_down()
        else:
            break
        i += 1


if __name__ == '__main__':
    run_tasks()
