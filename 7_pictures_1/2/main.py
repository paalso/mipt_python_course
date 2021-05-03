# Задание №1 (пробное)
# http://cs.mipt.ru/python/lessons/lab4.html#id7
# Sample picture: http://cs.mipt.ru/python/images/lab4/13_1.png

# Размеры картинки чуть изменены для того чтобы результат нормально
# отрисовывался на экране: ширина 794 -> 640

import pygame
import spec_figures

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
pygame.draw.rect(screen, ground_color,
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
    pygame.draw.rect(screen, trunks_color, (topleft, size))

# Ежик
hedgehog_color = (0x49,0x37,0x37)
hedgehog_border_width = 1
hedgehog_border_color = (0xff,0xff,0xff)

# левые лапки
spec_figures.draw_bordered_ellipsis(
        screen, (330, 790, 30, 13), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

spec_figures.draw_bordered_ellipsis(
        screen, (547, 792, 18, 14), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

# туловище
spec_figures.draw_bordered_ellipsis(
        screen, (345, 750, 215, 75), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

# правые лапки
spec_figures.draw_bordered_ellipsis(
        screen, (352, 803, 30, 16), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

spec_figures.draw_bordered_ellipsis(
        screen, (523, 805, 30, 15), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

# голова
spec_figures.draw_bordered_ellipsis(
        screen, (530, 765, 60, 32), hedgehog_color,
        hedgehog_border_color, hedgehog_border_width)

# глаза и носик
hedgehog_eyes_color = (0x0b,0x0b,0x06)

spec_figures.draw_bordered_ellipsis(
        screen, (556, 774, 10, 10), hedgehog_eyes_color,
        hedgehog_border_color, hedgehog_border_width)

spec_figures.draw_bordered_ellipsis(
        screen, (569, 770, 9, 9), hedgehog_eyes_color,
        hedgehog_border_color, hedgehog_border_width)

spec_figures.draw_bordered_ellipsis(
        screen, (586, 777, 6, 6), hedgehog_eyes_color,
        hedgehog_border_color, hedgehog_border_width)

# Иголка
pricles_color = (0x25, 0x1c, 0x1d)
border_color = (0x0f, 0x06, 0x07)
spec_figures.draw_triangle(
        screen, (410, 780), 12, 80, pricles_color, border_color)


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
