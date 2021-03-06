import pygame
import math
import random

# initialize pygame
pygame.init()
# creating screen
screen = pygame.display.set_mode((1000, 800))
# title and screen icon
pygame.display.set_caption('Space Inveador')
icon = pygame.image.load('Ufo.png')
pygame.display.set_icon(icon)
# background_image
background = pygame.image.load('background1.jpg')
# player_image
player_img = pygame.image.load('spaceship.png')
# enemy_image
enemy_img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 936)
enemyY = random.randint(50, 150)
enemyX_change = 0.6
enemyY_change = 20
playerX = 450
playerY = 600
playerX_change = 0
playerY_change = 0

# bullet_image
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 600
bullet_change = 0
bulletY_change = 4
bullet_state = "ready"  # ready--> it is the state where u cannot see the bullet at the screen


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def bullet(X, Y):
    global bullet_state
    bullet_state = "fire"  # fire--->bullet is moving
    screen.blit(bullet_img, (X + 15, Y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


score = 0

# game loop
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.9
            if event.key == pygame.K_LEFT:
                playerX_change = -0.9
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.6
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         playerY_change = 0
    # RGB(Red, Green, Blue)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 936:
        playerX = 936
    # playerY += playerY_change
    # if playerY <= 0:
    #     playerY = 0
    # if playerY >= 730:
    #     playerY = 730

    if enemyX <= 0:
        enemyX_change = 0.6
        enemyY += enemyY_change
    if enemyX >= 936:
        enemyX_change = -0.6
        enemyY += enemyY_change
    enemyX += enemyX_change
    # enemyY += enemyY_change
    # if enemyY <= 0:
    #     enemyY = 0
    # if enemyY >= 730:
    #     enemyY = 730
    # bullet movements
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"
    # collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision == True:
        bulletY = playerY
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 936)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
