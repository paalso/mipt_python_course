# Задание №1 (пробное)
# http://cs.mipt.ru/python/lessons/lab4.html#id7
# Sample picture: http://cs.mipt.ru/python/images/lab4/13_1.png

# Размеры картинки чуть изменены для того чтобы результат нормально
# отрисовывался на экране: ширина 794 -> 640

import pygame
import draw_elements

pygame.init()
FPS = 10
screen_size = draw_elements.screen_size
pygame.display.set_caption("A hedgehog in the wood")
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

# Общий фон
# Основной фон
draw_elements.draw_background(screen)

# Земля
draw_elements.draw_ground(screen)

# Стволы деревьев ?
draw_elements.draw_trees(screen)

# Ежик
draw_elements.draw_hedgehog(screen)


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
