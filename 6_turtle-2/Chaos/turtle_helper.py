import turtle
import math


def move(turtle, x, y):
    """
      Set up position of the given turtle
    """
    turtle.penup()
    old_speed = turtle.speed()
    turtle.speed(0)
    turtle.setx(x)
    turtle.sety(y)
    turtle.speed(old_speed)
    turtle.pendown()


def make_window(color, title, width=1200, height=900):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    # https://stackoverflow.com/questions/56528067/how-can-i-change-the-size-of-my-python-turtle-window
    wn = turtle.Screen()
    wn.setup(width + 4, height + 8)
    wn.setworldcoordinates(0, 0, 1000, 850)
    wn.bgcolor(color)
    wn.title(title)
    return wn


def make_turtle(color, size, x = 0, y = 0, shape='turtle'):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    move(t, x, y)
    return t


def get_border_sizes(wn):
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    return x_min, x_max, y_min, y_max


def print_text(x, y, textlines, color="black", fontinfo=("Arial", 15, "normal")):
    t =  make_turtle(color, 1, x, y, shape="arrow")
    t.speed(0)
    for line in textlines:
        _, fontsize, _ = fontinfo
        t.write(line, font=fontinfo)
        move(t, x, y - fontsize * 1.5)
    move(t, -10, -10)
    t.penup()
    del(t)


def draw_line(x1, y1, x2, y2, color, size, shape='arrow'):
    t = make_turtle(color, size, x1, y1, shape)
    t.pensize(size)
    t.speed(0)
    t.goto(x2, y2)
    t.penup()
    del(t)

def draw_rectangle(
        x_start, y_start, width, height, color, size, shape='arrow'):
    t = make_turtle(color, size, x_start, y_start, shape)
    t.pensize(size)
    t.speed(0)
    t.forward(width); t.left(90)
    t.forward(height); t.left(90)
    t.forward(width); t.left(90)
    t.forward(height)
    t.penup()
    del(t)

def draw_polygon(
        turtle,
        angles,
        side,
        start_angle,
        sector_angle = 360,
        counterclockwise = True
    ):
    turtle.setheading(180 - start_angle)
    for i in range(int(angles * sector_angle / 360)):
        turtle.forward(side)
        if counterclockwise:
            turtle.left(360 / angles)
        else:
            turtle.right(360 / angles)


def draw_circle(turtle, radius, start_angle, counterclockwise = True):
    ANGLES = 100

    side = 2 * radius * math.sin(math.radians(360 / (2 * ANGLES)))
    draw_polygon(turtle, ANGLES, side, start_angle, 360, counterclockwise)


def draw_arc(
        turtle,
        radius,
        start_angle,
        sector_angle = 180,
        counterclockwise = True
    ):

    ANGLES = 70

    side = 2 * radius * math.sin(math.radians(360 / (2 * ANGLES)))
    draw_polygon(turtle,
        ANGLES,
        side,
        start_angle,
        sector_angle,
        counterclockwise
    )
