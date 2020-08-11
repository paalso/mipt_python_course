#!/usr/bin/python3

from pyrob.api import *


def go_along():
    direction_to_right = True
    # счетчик того, сколько раз на одном уровне робот до шел до края - левого
    # или правого
    counter = 0
    while True:
        if wall_is_on_the_right():
            direction_to_right = False
            counter += 1
        if wall_is_on_the_left():
            direction_to_right = True
            counter += 1
            # если counter > 1, то это значит робот дошел до одного края,
            # потом до другого и за этот проход не смог спустится на уровень
            # ниже, т.е. находится на нижнем уровне - это условие выхода
            if counter > 1:
                break
        if not wall_is_beneath():
            move_down()
            counter = 0     # при переходе на новый уровень счетчик обнуляется
        if direction_to_right:
            move_right()
        else:
            move_left()


@task(delay=0.05)
def task_8_30():
    go_along()  # можно было и не выносить в отдельную функцию


if __name__ == '__main__':
    run_tasks()
