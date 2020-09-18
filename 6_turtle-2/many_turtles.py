# http://cs.mipt.ru/python/lessons/lab3.html#id17

# Упражнение № ???
"""
Пока придется приостановится, т.к. мало времени
Модуль turtle_helper Не очень годится, т.к. все воздействия на черепашек
осуществляются как внешние функции, и это не очень удобно
Нужно разработать класс - дочерний от Turtle и добавить туда методы по работе:
    задавать направление, контролировать взаимодействие друг с другом и стенками
    и т.п.
"""

import turtle, random
import turtle_helper

def check_near_borders(window, turtle):
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    x, y = turtle.xcor(), turtle.ycor()


def main():
    wn = turtle_helper.make_window("lightgreen", "Many turtles")

    # Исходные данные
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    number_of_turtles = 10
    steps_of_time_number = 100

    # Создаем частицы
    pool = [turtle_helper.make_turtle("blue", 3, random.randint(x_min, x_max),
            random.randint(y_min, y_max), "circle")
                for i in range(number_of_turtles)]

    for i in range(steps_of_time_number):
        for unit in pool:
            unit.forward(2)

    wn.mainloop()


if __name__ == '__main__':
    main()
