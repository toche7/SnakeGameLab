import pygame 
pygame.init()
screen = pygame.display.set_mode((700,520))
clock = pygame.time.Clock()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    pygame.display.flip()
    clock.tick(10) # limit FPS to 60


pygame.quit()