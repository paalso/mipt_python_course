import pygame, random
import spec_figures

width = 640
height = int(1.414 * width)
screen_size = width, height
WHITE = (0xff,0xff,0xff)

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

    # левые лапки
    spec_figures.draw_bordered_ellipsis(
            screen, (0.52 * width, 0.87 * height,
                    0.047 * width, 0.013 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.85 * width, 0.88 * height,
                    0.03 * width, 0.015 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    # туловище
    spec_figures.draw_bordered_ellipsis(
            screen, (0.54 * width, 0.83 * height,
                    0.34 * width, 0.083 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    # правые лапки
    spec_figures.draw_bordered_ellipsis(
            screen, (0.55 * width, 0.887 * height, 0.047 * width,
                    0.018 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.817 * width, 0.887 * height,
                    0.047 * width, 0.017 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    # порция колючек
    prickles_data_1 = [
        ((0.505, 0.87), 0),
        ((0.66, 0.845), 0),
        ((0.81, 0.87), 0),
        ((0.66, 0.91), 0)
    ]

    draw_pricles(screen, prickles_data_1)
    draw_random_pricles(screen, 30)

    # апельсинка 1
    orange_color = (0xc7, 0x71, 0x38)
    spec_figures.draw_bordered_ellipsis(
            screen, (0.54 * width, 0.80 * height,
                    0.07 * width, 0.07 * width), orange_color,
            WHITE, hedgehog_border_width)

    # колючка
    draw_pricles_pair(screen, (0.53 * width, 0.88 * height),
            int(0.035 * width), -15)

    # апельсинка 2
    orange_color = (0xc7, 0x71, 0x38)
    spec_figures.draw_bordered_ellipsis(
            screen, (0.559 * width, 0.797 * height,
                    0.07 * width, 0.07 * width), orange_color,
            WHITE, hedgehog_border_width)

    # яблоко
    apple_color = (0xfe, 0x00, 0x00)
    spec_figures.draw_bordered_ellipsis(
            screen, (0.74 * width, 0.79 * height,
                    0.08 * width, 0.08 * width), apple_color,
            WHITE, hedgehog_border_width)

    # гриб
    draw_mushroom(screen, (0.60 * width, 0.86 * height), 0.13 * width, 20)

    # голова
    spec_figures.draw_bordered_ellipsis(
            screen, (0.828 * width, 0.845 * height,
                    0.094 * width, 0.035 * height), hedgehog_color,
            WHITE, hedgehog_border_width)

    # глаза и носик
    hedgehog_eyes_color = (0x0b,0x0b,0x06)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.869 * width, 0.855 * height,
                    0.016 * width, 0.011 * height), hedgehog_eyes_color,
            WHITE, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.889 * width, 0.851 * height,
                    0.014 * width, 0.01 * height), hedgehog_eyes_color,
            WHITE, hedgehog_border_width)

    spec_figures.draw_bordered_ellipsis(
            screen, (0.916 * width, 0.859 * height,
                    0.009 * width, 0.007 * height), hedgehog_eyes_color,
            WHITE, hedgehog_border_width)


def draw_pricles(screen, prickles_data):
    pricles_width = int(0.035 * width)
    for coord, angle in prickles_data:
        width_coef, height_coef = coord
        coord = width_coef * width, height_coef * height
        draw_pricles_pair(screen, coord, pricles_width, angle)


def draw_random_pricles(screen, number):
    pricles_width = int(0.035 * width)

    left = 0.505
    right = 0.81
    top = 0.845
    bottom = 0.91
    edge_indent = 0.2

    k = 0
    while k < number:
        angle = random.randint(-35, -8)
        width_coef = random.uniform(left, right)
        height_coef = random.uniform(top, bottom)

        width_share = (width_coef - left) / (right - left)
        height_share = (height_coef - top) / (bottom - top)

        if width_share < edge_indent and height_share < edge_indent or \
                width_share < edge_indent and height_share >1 - edge_indent or \
                width_share > 1 - edge_indent and height_share < edge_indent or \
                width_share > 1 - edge_indent and height_share > 1 - edge_indent:
                    continue

        coord = width_coef * width, height_coef * height
        draw_pricles_pair(screen, coord, pricles_width, angle)
        k += 1


def draw_pricles_pair(screen, bottom_left, base, angle_to_vertical=0):
    pricles = pygame.image.load('prickles.png')
    scaled_pricles = pygame.transform.scale(pricles,
            (base, int(base / pricles.get_width() * pricles.get_height())))
    rotated_pricles = pygame.transform.rotate(
            scaled_pricles, - angle_to_vertical)
    pricles_rect = rotated_pricles.get_rect(bottomleft=bottom_left)
    screen.blit(rotated_pricles, pricles_rect)


def draw_mushroom(screen, bottom_left, side, angle_to_vertical=0):
    surf_width = 1000
    surf_height = 1000

    leg_color = dot_color = 0xff, 0xff, 0xff
    hat_color = 0xef, 0x0, 0x0

    background_color = 0x0, 0xff, 0x0

    base_mashroom = pygame.Surface((surf_width, surf_height))
    base_mashroom.fill(background_color)

    # ножка и шляпка
    pygame.draw.ellipse(base_mashroom, leg_color, (350, 150, 300, 750))
    pygame.draw.ellipse(base_mashroom, hat_color, (0, 0, 1000, 250))

    # крапинки на шляпке
    pygame.draw.ellipse(base_mashroom, dot_color, (110, 70, 90, 40))
    pygame.draw.ellipse(base_mashroom, dot_color, (290, 190, 80, 35))
    pygame.draw.ellipse(base_mashroom, dot_color, (340, 60, 85, 40))
    pygame.draw.ellipse(base_mashroom, dot_color, (550, 55, 85, 40))
    pygame.draw.ellipse(base_mashroom, dot_color, (800, 50, 130, 55))
    pygame.draw.ellipse(base_mashroom, dot_color, (540, 180, 85, 40))

    side = int(side)
    scaled_mashroom = pygame.transform.scale(base_mashroom, (side, side))
    rotated_mashroom = pygame.transform.rotate(scaled_mashroom,
         - angle_to_vertical)
    mashroom_rect = rotated_mashroom.get_rect(bottomleft=bottom_left)

    rotated_mashroom.set_colorkey((0x0, 0xff, 0x0))

    screen.blit(rotated_mashroom, mashroom_rect)


