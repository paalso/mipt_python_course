# Задание №1 (пробное)
# http://cs.mipt.ru/python/lessons/lab4.html#id7
# Sample picture: http://cs.mipt.ru/python/images/lab4/13_1.png

# Размеры картинки чуть изменены для того чтобы результат нормально
# отрисовывался на экране: ширина 794 -> 640

import pygame
from pygame.draw import *


pygame.init()
FPS = 10
screen_size = 640, 905
pygame.display.set_caption("A hedgehog in the wood")
screen = pygame.display.set_mode(screen_size)

# Общий фон

# Основной фон
background_color = (0x2c, 0xa0, 0x5a)   # зеленый
screen.fill(background_color)

# Земля
ground_color = (0x6c, 0x5d, 0x53)       # светло-коричневый
ground_topleft = 0, 543
ground_width = screen_size[0]
ground_height = screen_size[1] - ground_topleft[1]
rect(screen, ground_color,
        (ground_topleft, (ground_width, ground_height)))

# Стволы деревьев ?
trunks_color = (0xd4, 0xaa, 0)          # темно-желтый
# В формате (topleft), (width, heigth))
trunks_data = [
    ((0, 0), (50, 588)),
    ((80, 0), (150, 888)),
    ((452, 0), (60, 588)),
    ((590, 0), (40, 660)),
]
for topleft, size in trunks_data:
    print(topleft, size)
    rect(screen, trunks_color, (topleft, size))

# Ежик


# Рисование
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
