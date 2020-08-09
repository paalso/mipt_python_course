#!/usr/bin/python3

from pyrob.api import *


def get_final():
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()


def get_out():
    exit_found = False
    while True:
        if not wall_is_above():
            exit_found = True
            move_up()
            break
        if wall_is_on_the_left():
            break
        move_left()
    if not exit_found:
        while True:
            if not wall_is_above():
                move_up()
                break
            move_right()



@task
def task_8_28():
    get_out()
    get_final()


if __name__ == '__main__':
    run_tasks()
