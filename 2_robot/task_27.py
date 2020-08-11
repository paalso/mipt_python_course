#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    counter = 0
    move_right()
    fill_cell()
    finish = False
    while True:
        for _ in range(counter):
            if wall_is_on_the_right():
                finish = True
                break
            move_right()
        if finish:
            break
        fill_cell()
        counter += 1


if __name__ == '__main__':
    run_tasks()
