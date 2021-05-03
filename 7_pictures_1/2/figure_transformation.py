# https://younglinux.info/pygame/draw

import pygame
import pygame.draw

def main():

    pygame.init()
    FPS = 30

    square_size = 100, 100
    width, height = square_size[0] * 5, square_size[1] * 2
    screen_size = width, height
    pygame.display.set_caption("Figures transformation")
    screen = pygame.display.set_mode(screen_size)

    RED = (0xff, 0, 0)

    # Основной фон
    background_color = (0xe9, 0xfb, 0xaf)
    screen.fill(background_color)

    #Генерация изображения
    x = 0
    rect = pygame.Rect((x, square_size[1] // 2), square_size)

    # Рисование
    pygame.display.update()

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.draw.rect(screen, RED, rect)
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
