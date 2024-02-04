import pygame
import random


class PhysicalEntities:
    def __init__(self, pos: list, img):
        self.pos = pos
        self.img = img

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.img.get_width(), self.img.get_height())

    def render(self, surf):
        surf.blit(self.img, self.pos)

    def update(self, movement):
        self.pos[1] += movement[1]
        if self.pos[1] >= 550:
            self.pos[1] = 550
        if self.pos[1] <= 0:
            self.pos[1] = 0


class Ball:
    def __init__(self, pos: list, img):
        self.pos = pos
        self.img = img
        self.flip = False
        self.movement = [0, 0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.img.get_width(), self.img.get_height())

    def render(self, surf):
        surf.blit(self.img, self.pos)

    def update(self, game):
        self.pos[1] += self.movement[1]
        if self.flip:
            self.pos[0] += 15
        else:
            self.pos[0] -= 15

        if self.pos[0] > 1366 + 500 or self.pos[0] < -500:
            if self.pos[0] > 1366 + 500:
                game.player_score += 1
            else:
                game.comp_player_score += 1
            self.pos[0] = 1366//2
            self.flip = not self.flip
            self.movement[1] = 0
            self.pos = [1366/2, 768/2]

        if self.pos[1] <= 30 or self.pos[1] >= 768 - 30:
            self.movement[1] = self.movement[1] * -1

        player_rect = game.player.rect()
        comp_player_rect = game.comp_player.rect()
        ball_rect = self.rect()
        if ball_rect.colliderect(player_rect) or ball_rect.colliderect(comp_player_rect):
            self.flip = not self.flip
            print("collision")
            if random.randint(0, 1):
                self.movement[1] = random.randint(1, 10)
            else:
                self.movement[1] = -random.randint(1, 10)
