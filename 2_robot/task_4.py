#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
##    why doesn't work?
##    possible_movements = (
##        (wall_is_above, move_up),
##        (wall_is_beneath, move_down),
##        (wall_is_on_the_left, move_left),
##        (wall_is_on_the_right, move_right)
##    )
##
##    for predicate, move in possible_movements:
##        if not predicate():
##            move()

    if not wall_is_above():
        move_up()
    elif not wall_is_beneath():
        move_down()
    elif not wall_is_on_the_left():
        move_left()
    else:
        move_right()


if __name__ == '__main__':
    run_tasks()
