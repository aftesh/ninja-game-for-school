import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        
        self.img_pos = [160, 260]
        self.movement = [False, False, False, False]
        
        self.collision_area1 = pygame.Rect(50, 50, 300, 50)
        self.collision_area2 = pygame.Rect(200, 150, 300, 50)
        self.collision_area3 = pygame.Rect(600, 400, 300, 50)


        self.bgc = (14, 219, 248)
    def run(self):
        while True:

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area1) or img_r.colliderect(self.collision_area2) or img_r.colliderect(self.collision_area3):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area1)
                self.screen.fill((0, 0, 0))
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area1)
                self.screen.fill((14, 219, 248))

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.img_pos[0] += (self.movement[3] - self.movement[2]) * 5
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()