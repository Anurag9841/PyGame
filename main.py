import pygame
import random

pygame.init()
# creating screen
screen = pygame.display.set_mode((1000, 800))
# title and screen icon
pygame.display.set_caption('Space Inveador')
icon = pygame.image.load('Ufo.png')
pygame.display.set_icon(icon)
background=pygame.image.load('background1.jpg')
# player
player_img = pygame.image.load('spaceship.png')
enemy_img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 936)
enemyY = random.randint(50, 150)
playerX = 450
playerY = 600
playerX_change = 0
playerY_change = 0
enemyX_change = 0.6
enemyY_change = 40
def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


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
                playerX_change = 0.6
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_UP:
                playerY_change = -0.6
            if event.key == pygame.K_DOWN:
                playerY_change = 0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # RGB(Red, Green, Blue)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 936:
        playerX = 936
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    if playerY >= 730:
        playerY = 730

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.6
        enemyY+=enemyY_change
    if enemyX >= 936:
        enemyX_change = -0.6
        enemyY += enemyY_change
    # enemyY += enemyY_change
    # if enemyY <= 0:
    #     enemyY = 0
    # if enemyY >= 730:
    #     enemyY = 730
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
