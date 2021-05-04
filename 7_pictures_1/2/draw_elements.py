import pygame
import spec_figures

width = 640
height = int(1.414 * width)
screen_size = width, height

def draw_background(screen):
    background_color = (0x2c, 0xa0, 0x5a)   # зеленый
    screen.fill(background_color)


def draw_ground(screen):
    ground_color = (0x6c, 0x5d, 0x53)       # светло-коричневый
    ground_topleft = 0, 0.6 * width
    ground_width = width
    ground_height = height - ground_topleft[1]
    pygame.draw.rect(screen, ground_color,
        (ground_topleft, (ground_width, ground_height)))

def draw_trees(screen):
    trunks_color = (0xd4, 0xaa, 0)          # темно-желтый
    # В формате (topleft), (width, heigth))
    trunks_data = [
        ((0, 0), (0.08 * width, 0.65 * height)),
        ((0.125 * width, 0), (0.23 * width, 0.98 * height)),
        ((0.71 * width, 0), (0.094 * width, 0.65 * height)),
        ((0.92 * width, 0), (0.0625 * width, 0.73 * height)),
    ]
    for topleft, size in trunks_data:
        print(topleft, size)
        pygame.draw.rect(screen, trunks_color, (topleft, size))


def draw_hedgehog(screen):
    hedgehog_color = (0x49,0x37,0x37)
    hedgehog_border_width = 1
    hedgehog_border_color = (0xff,0xff,0xff)

    # левые лапки
    spec_figures.draw_bordered_ellipsis(
            screen, (0.52 * width, 0.87 * height,
                    0.047 * width, 0.013 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.85 * width, 0.88 * height,
                    0.03 * width, 0.015 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    # туловище
    spec_figures.draw_bordered_ellipsis(
            screen, (0.54 * width, 0.83 * height,
                    0.34 * width, 0.083 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    # правые лапки
    spec_figures.draw_bordered_ellipsis(
            screen, (0.55 * width, 0.887 * height, 0.047 * width,
                    0.018 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.817 * width, 0.887 * height,
                    0.047 * width, 0.017 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    # голова
    spec_figures.draw_bordered_ellipsis(
            screen, (0.828 * width, 0.845 * height,
                    0.094 * width, 0.035 * height), hedgehog_color,
            hedgehog_border_color, hedgehog_border_width)

    # глаза и носик
    hedgehog_eyes_color = (0x0b,0x0b,0x06)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.869 * width, 0.855 * height,
                    0.016 * width, 0.011 * height), hedgehog_eyes_color,
            hedgehog_border_color, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.889 * width, 0.851 * height,
                    0.014 * width, 0.01 * height), hedgehog_eyes_color,
            hedgehog_border_color, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.916 * width, 0.859 * height,
                    0.009 * width, 0.007 * height), hedgehog_eyes_color,
            hedgehog_border_color, hedgehog_border_width)

    list_of_prickles = [
        ((0.56 * width, 0.87 * height), -10),
        ((0.57 * width, 0.871 * height), -12),
        ((0.58 * width, 0.875 * height), -10),
        ((0.65 * width, 0.872 * height), -15),
    ]

    # Иголки
    pricles_width = int(0.032 * width)
    for coord, angle in list_of_prickles:
        print(coord, angle)
        spec_figures.draw_pricles_pair(screen, coord, pricles_width, angle)


def draw_pricles(list_of_prickles):
    for coord, angle in list_of_prickles:
        print(coord, angle)
        spec_figures.draw_pricles_pair(screen, coord, 20, angle)
