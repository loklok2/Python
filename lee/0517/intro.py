import pygame                                           #라이브러리의 특성을 알아야 잘쓴다

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))
# screen_surf = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

# ship_rect = pygame.rect.Rect(0,0,100,100)        #Rect 사각형을 의미 
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom
alien_rect = pygame.rect.Rect(200,200,200,200)

bullet_rect = None
bullets =[]

bullet_rect = pygame.rect.Rect(0,0,5,50)
bullet_rect.midbottom = ship_rect.midtop

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False


while True:                                 #게임루프
    # Process player inputs.
    for event in pygame.event.get():      #event는 보통 클릭이나 동작을 할때 사용
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.rect.Rect(0,0,5,5)
                bullet_rect.midbottom = ship_rect.midtop
                bullets.append(bullet_rect)
            elif event.key == pygame.K_RIGHT:
               right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:    
                up_pressed = True
            elif event.key == pygame.K_DOWN:    
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                    right_pressed = False  
            elif event.key == pygame.K_LEFT:
                    left_pressed = False                      
            elif event.key == pygame.K_UP:
                    up_pressed = False                      
            elif event.key == pygame.K_DOWN:
                    down_pressed = False                      
            
    # Do logical updates here.
    # ...
    if right_pressed:
        ship_rect.x = ship_rect.x + 1
        alien_rect.x = alien_rect.x + 2
    if left_pressed:
        ship_rect.x = ship_rect.x - 1
        alien_rect.x = alien_rect.x - 2
    if up_pressed:
        ship_rect.y = ship_rect.y -1
        alien_rect.y = alien_rect.y -2
    if down_pressed:
        ship_rect.y = ship_rect.y +1
        alien_rect.y = alien_rect.y +2
    if bullets:
        for bullet in bullets:
            bullet.y = bullet.y -10

    screen_surf.fill(("white"))  # Fill the display with a solid color #

    # Render the graphics here.
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(200)         # wait until next frame (at 60 FPS)