import pygame 
pygame.init()
screen = pygame.display.set_mode((700,520))
clock = pygame.time.Clock()
running = True
oldkey = 0
pixel_width = 50 
snake_pixel  = pygame.Rect(0,0, pixel_width,pixel_width)
snakePosition = pygame.Vector2(350,250)
snake_pixel.center = snakePosition
old_pos = snakePosition.copy()


food_pixel = pygame.Rect(0,0, pixel_width, pixel_width)
foodPosition = pygame.Vector2(100,100)
food_pixel.center = foodPosition


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    if old_pos != snakePosition:
        old_pos = snakePosition.copy()
        snake_pixel.center = snakePosition



    pygame.draw.rect(screen,"green",snake_pixel)
    pygame.draw.rect(screen,"red",food_pixel)

    if snake_pixel.colliderect(food_pixel):
        print("Collision")
        print("game OVER")
        running = False

    if event.type == pygame.KEYDOWN:
        oldkey  = event.key


    if oldkey == pygame.K_UP:
        snakePosition.y -= pixel_width
    elif oldkey == pygame.K_DOWN:
        snakePosition.y += pixel_width
    elif oldkey == pygame.K_LEFT:
        snakePosition.x -= pixel_width
    elif oldkey == pygame.K_RIGHT:
        snakePosition.x += pixel_width
    
    pygame.display.flip()
    clock.tick(5) # limit FPS to 60


pygame.quit()