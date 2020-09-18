# http://cs.mipt.ru/python/lessons/lab3.html#id15

# Упражнение № 3
# Перенесите описание способа рисования почтовых цифр (списки движений) в файл.
# Пусть черепаха считывает "шрифт" из файла.
"""
'Шрифт' хранится в отдельном csv-файле в виде:
    первый символ - это, собственно, изображаемый символ
    далее идут tuples вида (0,90,1),
    где первый элемент - 0/1 - признак того, что перо поднято/опущено,
    второй - 90 - угол направления движения,
    третий - 1 - длина элемента шрифта
'Шрифт' читается с помощью ф-ии read_font() в словарь, в к-м каждому строчному
элементу сооттвествует список кортежей, в к-х зашифровано движение каждого
элемента
"""

import turtle, random
import turtle_helper, read_font


def print_digit(turtle, font, symbol, step):

    gap = int(0.4 * step)   # расстояние между символами

    def move_gap():     # сдвиг к соседнему символу
        turtle.penup(); turtle.setheading(0); turtle.fd(gap); turtle.pendown()

    for pen_down, angle, step_quot in font[symbol]:
        if not pen_down: turtle.penup()
        turtle.setheading(angle)
        turtle.fd(step_quot * step)
        turtle.pendown()
    move_gap()


def print_with_font(turtle, font, string, step):
    try:
        string = str(string)    # if type(string) == int
    except:
        raise ValueError
    turtle.speed(8)
    for d in string:
        print_digit(turtle, font, d, step)


def main():
    wn = turtle_helper.make_window("lightgreen", "Letter S")
    t = turtle_helper.make_turtle("red", 2, shape="classic")
    turtle_helper.move(t, -350, 0)

    font_file = "index_like_font.csv"
    font = read_font.read_font(font_file)
    # print_with_font(t, font, "02123475297516589", 30)
    print_with_font(t, font, "0123456789", 30)

    wn.mainloop()


if __name__ == '__main__':
    main()
