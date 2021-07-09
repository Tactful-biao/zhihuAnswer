import pygame
import cv2


def get_font_pic(text):
    pygame.init()

    # text = '标'

    font = pygame.font.Font('font/xqx.TTF', 400)

    ftext = font.render(text, True, (0, 0, 0), (255, 255, 255))

    pygame.image.save(ftext, 'pic.png')

    img = cv2.imread('pic.png')

    crop = img[150:550, 0:400]

    cv2.imwrite('pic.png', crop)
    return crop