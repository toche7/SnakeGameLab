import pygame 
import random

screenW = 700
screenH = 520
pygame.init()
screen = pygame.display.set_mode((screenW,screenH))
clock = pygame.time.Clock()
running = True
oldkey = 0
pixel_width = 50 


def getRandomPostion():
    return (random.randint(0,screenW),random.randint(0,screenH))

snake_pixel  = pygame.Rect(0,0, pixel_width,pixel_width)
snakePosition =  pygame.Vector2(getRandomPostion())
snake_pixel.center = snakePosition
old_pos = snakePosition.copy()
snakeLength = 1
snake = [snake_pixel]
food_pixel = pygame.Rect(0,0, pixel_width, pixel_width)
foodPosition = pygame.Vector2(getRandomPostion())
food_pixel.center = foodPosition


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    # if old_pos != snakePosition:
    #     old_pos = snakePosition.copy()
    #     snake_pixel.center = snakePosition()

    if old_pos != snakePosition:
        old_pos = snakePosition.copy()
        if snakeLength > 1:
            snake = snake[:snakeLength -1]
            snake.insert(0, snake[0].copy())
        snake[0].center =  snakePosition


    #pygame.draw.rect(screen,"green",snake_pixel)
    for segment in snake:
        pygame.draw.rect(screen,"green",segment)


    pygame.draw.rect(screen,"red",food_pixel)

    if snake[0].colliderect(food_pixel):
        food_pixel.center = pygame.Vector2(getRandomPostion())
        snakeLength += 1
        snake.append(snake[-1].copy())
        print("Collision")
        print("eat food")
        print(snakeLength)
        # running = False

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