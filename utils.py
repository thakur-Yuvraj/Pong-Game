import pygame

PATH = 'Data/images'


def load_img(file_name):
    img = pygame.image.load(PATH + '/' + file_name).convert_alpha()
    return img


def draw_text(surf, string, pos: list):
    text_font = pygame.font.SysFont('Arial', 30)
    img = text_font.render(string, True, [90, 190, 80])
    surf.blit(img, pos)
