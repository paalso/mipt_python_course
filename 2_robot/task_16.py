#!/usr/bin/python3

from pyrob.api import *


def move_right_to_end():
    while not wall_is_on_the_right():
        move_right()

def move_left_to_end():
    while not wall_is_on_the_left():
        move_left()

def move_down_to_end():
    while not wall_is_beneath():
        move_down()

def move_up_to_end():
    while not wall_is_above():
        move_up()


@task
def task_8_22():
    move_up_to_end()
    if wall_is_on_the_left():
        move_right_to_end()
    else:
        move_left_to_end()


if __name__ == '__main__':
    run_tasks()
