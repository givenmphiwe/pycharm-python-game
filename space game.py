import pygame
import random
import math

pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.png")
#creating the tittle of the game
pygame.display.set_caption("space invader")

#player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyY = []
enemyX = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("cartoon.png"))
    enemyY.append(random.randint(50, 150))
    enemyX.append(random.randint(0, 735))
    enemyX_change.append(10)
    enemyY_change.append(30)

#bullet that the player will be shooting

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"    #you cant see the bullet on screen

score = 0
def player(x,y):
    screen.blit(playerImg, (x, y))      #for displaying    

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x, y))

def bullet (x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))
    
#game loop
running = True
while running:

    screen.fill((0, 0, 0))     #color of my background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
         
        if event.type == pygame.KEYDOWN:         #when pressing the key down
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.type == pygame.K_SPACE:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:           #when you releasing the key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    playerX += playerX_change
    
    if  playerX <= 0:      #for player not to leave the screen
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4     #not to leave screen boundries and disappear
            enemyY[i] += enemyY_change[i]   #moving the enemy down by down a bit
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        enemy(enemyX[i], enemyY[i], i)
        
    #bullet movement
    if bulletY <= 0:
        bulletY = 480           #shooting many bullets
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    
    player(playerX,playerY)
    pygame.display.update()    #updating the screen of pygame        
