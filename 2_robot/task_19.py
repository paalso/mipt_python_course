#!/usr/bin/python3

from pyrob.api import *


def get_final():
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()


def get_out():
    while True:
        if not wall_is_above():
            move_up()
            return True
        if wall_is_on_the_left():
            break
        move_left()
    while True:
        if not wall_is_above():
            move_up()
            return True
        if wall_is_on_the_right():
            return False
        move_right()


@task
def task_8_29():
    if get_out():
        get_final()


if __name__ == '__main__':
    run_tasks()
