import pygame


class Bullet:
    def __init__(self, screen_surf):
        self.bullet_rect = pygame.rect.Rect(0, 0, 50, 10)
        self.screen_surf = screen_surf
          
    def render(self):
        pygame.draw.rect(self.screen_surf, 'red', self.bullet_rect)

    def move_front_ship(self, ship_rect):
        self.bullet_rect.midbottom = ship_rect.midtop
    
    def get_rect(self):
        return self.ship_rect

# bullet = Bullet()
# bullet.move_front_ship(ship_rect)
# bullet.render()