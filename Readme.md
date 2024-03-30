Readme
### setup python version
pyenv local 3.10.0

### setup virtual environment 
python -m venv venv

### activate virtaul environment
venv\Scripts\activate

### create requirements.txt file 
create new file and put the list of libraries need to install 
in this case 
pygame 
pip install -r requirements.txt 


### create python main.py 
creat the black screen 

```
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

    pygame.draw.rect(screen,"green",snake_pixel)

    pygame.display.flip()
    clock.tick(10) # limit FPS to 60


pygame.quit()
```



#### create .gitignore
create gitignore to list the files and folder that not include the git 
in this caase 
venv 

### initial git
init git 

### setup git 
git config --global user.email "you@example.com"
git config --global user.name "Your Name"


### modified the main.py 
```
create snake at middle of the screen
pixel_width = 50 
snake_pixel  = pygame.Rect(0,0, pixel_width,pixel_width)
snakePosition = pygame.Vector2(350,250)
snake_pixel.center = snakePosition
```

and add draw rect in the main loop

```
pygame.draw.rect(screen,"green",snake_pixel)

```

### add food 
```
food_pixel = pygame.Rect(0,0, pixel_width, pixel_width)
foodPosition = pygame.Vector2(100,100)
food_pixel.center = foodPosition
```
```
pygame.draw.rect(screen,"red",food_pixel)
```


### Move snake 
```
   if oldkey == pygame.K_UP:
        snakePosition.y -= pixel_width
    elif oldkey == pygame.K_DOWN:
        snakePosition.y += pixel_width
    elif oldkey == pygame.K_LEFT:
        snakePosition.x -= pixel_width
    elif oldkey == pygame.K_RIGHT:
        snakePosition.x += pixel_width
    
```

### Collision of snake and food.

```
    if snake_pixel.colliderect(food_pixel):
        print("Collision")
        print("game OVER")
        running = False
```
    
#### to deactivate the virtual env.
venv\Scripts\deactivate
