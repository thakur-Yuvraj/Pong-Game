import pygame

from entities import PhysicalEntities, Ball
from utils import load_img, draw_text


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PONG")
        self.screen = pygame.display.set_mode([1366, 768])
        self.clock = pygame.time.Clock()
        self.assets = {
            'player_img': load_img("rect_ent.png"),
            'ball_img': load_img('ball.png'),
        }
        self.assets['player_img'] = pygame.transform.scale(self.assets['player_img'], [30, 200])  # changing height
        self.assets['ball_img'] = pygame.transform.scale(self.assets['ball_img'], [20, 20])
        self.player = PhysicalEntities([10, 20], self.assets['player_img'])
        self.ball = Ball([1366/2, 768/2], self.assets['ball_img'])
        self.movement = [0, 0]
        self.ball_dir = True
        self.comp_player = PhysicalEntities([1366 - 40, 20], self.assets['player_img'])
        self.comp_movement = [0, 0]
        self.ball_movement = [0, 0]
        self.player_score = 0
        self.comp_player_score = 0
        pass

    def run(self):
        while True:
            self.screen.fill([10, 8, 23, 0])
            score = str(self.player_score) + " :: " + str(self.comp_player_score)
            draw_text(self.screen, "Score: " + score, [1366/2 - 50, 10])

            # self.screen.blit(self.assets['player_img'], [10, 50])
            self.player.update(self.movement)
            self.player.render(self.screen)
            self.comp_player.render(self.screen)

            # computer ai
            if self.ball.pos[1] != self.comp_movement[1]:
                if self.ball.pos[1] > self.comp_player.pos[1] + 70:
                    self.comp_movement[1] = 5
                else:
                    self.comp_movement[1] = -5

            else:
                self.comp_movement[1] = 0

            self.comp_player.update(self.comp_movement)

            self.ball.render(self.screen)
            self.ball.update(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[1] = -7
                        if self.ball.rect().colliderect(self.player.rect()):
                            self.ball_movement[1] = -5
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = 7
                        if self.ball.rect().colliderect(self.player.rect()):
                            self.ball_movement[1] = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.movement[1] = 0

            self.clock.tick(60)
            pygame.display.update()


Game().run()
