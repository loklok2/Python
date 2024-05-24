
import sys
import pygame

from alian import Alien
from bullet import Bullet
from ship import Ship


class Game:
    def __init__(self, title):
        pygame.init()
        self.title = title

        self._create_screen()
        self._create_ship()
        self._create_alien()
        self.create_score()
       

        self.bullets = []
        self.right_pressed = True
        self.left_pressed = True
        
        self.clock = pygame.time.Clock()

    def create_score(self):
        self.score_font = pygame.font.SysFont(None, 64)
        self.font_surf = self.score_font.render(
            str(5678), 
            True, 
            'black'
            )

    def _create_alien(self):
        self.aliens = []
        for i in range(1, 2):
            for j in range(10):
                alien = Alien(self.screen_surf)
                x_pos = 50 + (50*2)*j
                y_pos = 50 + (40*2)*i
                alien.move(x_pos, y_pos)
                
            self.aliens.append(alien)

    def _create_ship(self):
        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

    def _create_screen(self):
        self.screen_surf = pygame.display.set_mode(size=(800, 640))


    def __str__(self):
       return self.title


    def start(self):
        while True:
            events = pygame.event.get() 
            for e in events:
                if e.type == pygame.QUIT:
                    #print('QUIT')
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if e.key == pygame.K_RIGHT:
                        self.RIGHT_pressed = True
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if e.key == pygame.K_RIGHT:
                        self.RIGHT_pressed = True
                    if e.key == pygame.  K_SPACE:
                        bullet = Bullet(self.screen_surf)
                        bullet.move_front_ship(self.ship.get_rect)
                        self.bullets.append(bullet)

                    # if self.right_pressed:
                    #     self.ship.right

                    # if self.left_pressed:
                    #     self.ship.left

                    self.ship.update()


            self.render()   
            pygame.display.flip()
            self.clock.tick(60)

    def render(self):
        self.screen_surf.fill('white')
        self.ship.render()
        for alien in self.aliens:
            alien.render()
        self.screen_surf.blit(self.font_surf, (100, 100, 
                                        self.font_surf.get_rect().width,
                                        self.font_surf.get_rect().height))
game = Game('Space Invader!')
game.start()
