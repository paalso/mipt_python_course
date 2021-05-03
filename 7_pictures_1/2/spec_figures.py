import pygame


def draw_bordered_ellipsis(
        screen, ellipse_rect, ellipse_color, border_color, border_width=0):
    rect_topleft_x, rect_topleft_y, rect_width, rect_height = ellipse_rect
    inner_rect =   (rect_topleft_x + border_width,
                    rect_topleft_y + border_width,
                    rect_width - 2 * border_width,
                    rect_height - 2 * border_width)
    pygame.draw.ellipse(screen, ellipse_color, inner_rect)
    pygame.draw.ellipse(screen, border_color, ellipse_rect, border_width)


def draw_triangle(
        screen, bottom_left, base, leg, color, border_color, border_width=0):
    bottom_left_x, bottom_left_y = bottom_left
    bottom_right = bottom_left_x + base, bottom_left_y
    half_base = base // 2
    top = bottom_left_x + half_base, \
            bottom_left_y - (leg ** 2 + half_base ** 2) ** 0.5
    pygame.draw.polygon(screen, color, (bottom_left, bottom_right, top))

    # тут я пытался добавить границу, но на столь мелких изображениях
    # получается некрасиво; пока опустим, но фрагмент оставлю
##    bottom_left_x, bottom_left_y = \
##            bottom_left_x - border_width, bottom_left_y + border_width
##    bottom_left = bottom_left_x, bottom_left_y
##    bottom_right = bottom_left_x + base + 2 * border_width, bottom_left_y
##    top_x, top_y = top
##    top_y += border_width
##    top = top_x, top_y
##    pygame.draw.lines(
##            screen, border_color, True, (bottom_left, bottom_right, top))
