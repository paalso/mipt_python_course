# Задание №1 (пробное)
# http://cs.mipt.ru/python/lessons/lab4.html#id6

# Нарисовано с использованием не абсолютных, но неких относительных размеров:
# размер картинки -> радиус рожицы -> все остальное

import pygame
from pygame.draw import *


def draw_eye(screen, eye_color, eye_apple_color, eye_apple_coords,
            eye_radis, eye_apple_radis):
    BLACK = (0, 0, 0)
    circle(screen, eye_color, eye_apple_coords, eye_radis)
    circle(screen, BLACK, eye_apple_coords, eye_radis, 1)
    circle(screen, eye_apple_color, eye_apple_coords, eye_apple_radis)


def draw_inclined_rect(screen, color,
        top_left_coords, to_axis_x_angle_grads, length, width):

    import math
    to_axis_x_angle_rads = math.radians(to_axis_x_angle_grads)

    x, y = top_left_coords
    bottom_left_coords = (x + width * math.sin(to_axis_x_angle_rads),
                        y + width * math.cos(to_axis_x_angle_rads))

    top_right_coords = (x + length * math.cos(to_axis_x_angle_rads),
                        y - length * math.sin(to_axis_x_angle_rads))

    x1, y1 = top_right_coords
    bottom_right_coords = (x1 + width * math.sin(to_axis_x_angle_rads),
                        y1 + width * math.cos(to_axis_x_angle_rads))

    polygon(screen, color, (top_left_coords, top_right_coords,
            bottom_right_coords, bottom_left_coords))


pygame.init()
FPS = 10
screen_sz = 500
pygame.display.set_caption("An angry humanoid")

BLACK = (0, 0, 0)
RED = (0xff, 0, 0)
YELLOW = (0xff, 0xff, 0)
LIGHT_GREY = (0xd9, 0xd9, 0xd9)

# Фон
screen = pygame.display.set_mode((screen_sz, screen_sz))
background_color = LIGHT_GREY
screen.fill(background_color)

# центр рожицы = центр картинки
center_x, center_y, radius = screen_sz // 2, screen_sz // 2, screen_sz // 4

# Собственно рисуем рожицу

# Лицо
face_color = YELLOW
circle(screen, face_color, (center_x, center_y), radius)
circle(screen, BLACK,
        (center_x, center_y), radius, 3)

# Глаза
eye1_apple_x = center_x - 0.5 * radius
eye1_radis = 0.2 * radius
eye2_apple_x = center_x + 0.5 * radius
eye2_radis = 0.15 * radius
eye_apple_y = center_y - 0.2 * radius
eye_apple_radius = 0.08 * radius
eye_color = RED
eye_apple_color = BLACK

draw_eye(screen, eye_color, eye_apple_color, (eye1_apple_x, eye_apple_y),
        eye1_radis, eye_apple_radius)   # левый глаз

draw_eye(screen, eye_color, eye_apple_color, (eye2_apple_x, eye_apple_y),
        eye2_radis, eye_apple_radius)   # правый глаз

# Рот
mouth_left_x = eye1_apple_x
mouth_top_y = center_y + 0.5 * radius
mouth_length = radius
mouth_width = 0.2 * radius
mouth_color = BLACK
rect(screen, mouth_color,
        ((mouth_left_x, mouth_top_y), (mouth_length, mouth_width)))

# Брови
eyebrow_width = 0.1 * radius

eyebrow1_length = 0.95 * radius
eyebrow1_top_left_coords = center_x - 0.98 * radius, center_y - 0.82 * radius
eyebrow1_to_axis_x_angle_grads = -30

eyebrow2_length = 0.87 * radius
eyebrow2_to_axis_x_angle_grads = 20
eyebrow2_top_left_coords = center_x + 0.18 * radius, center_y - 0.34 * radius

# левая бровь
draw_inclined_rect(screen, BLACK, eyebrow1_top_left_coords,
        eyebrow1_to_axis_x_angle_grads, eyebrow1_length, eyebrow_width)

# правая бровь
draw_inclined_rect(screen, BLACK, eyebrow2_top_left_coords,
        eyebrow2_to_axis_x_angle_grads, eyebrow2_length, eyebrow_width)

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
