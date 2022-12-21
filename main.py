import pygame as pyopengl
import math
import random
from pygame import mixer
# initialize pygame
pyopengl.init()
# creating screen
screen = pyopengl.display.set_mode((1000, 900))
# title and screen icon
pyopengl.display.set_caption('Space Inveador')
icon = pyopengl.image.load('Ufo.png')
pyopengl.display.set_icon(icon)
# background_image
background = pyopengl.image.load('background.jpg')
mixer.music.load("background.wav")
mixer.music.play(-1)
# player_image
player_img = pyopengl.image.load('spaceship.png')
# enemy_image
enemy_img = pyopengl.image.load('enemy.png')
enemyX = random.randint(0, 936)
enemyY = random.randint(50, 150)
enemyX_change = 0.6
enemyY_change = 20
playerX = 450
playerY = 600
playerX_change = 0
playerY_change = 0

# bullet_image
bullet_img = pyopengl.image.load('bullet.png')
bulletX = 0
bulletY = 600
bullet_change = 0
bulletY_change = 4
bullet_state = "ready"  # ready--> it is the state where u cannot see the bullet at the screen
score = 0
font = pyopengl.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10
def show_score(x,y):
    score1 = font.render("Score of Player is : "+str(score),True, (255,255,255))
    screen.blit(score1,(x,y))

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




# game loop
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pyopengl.event.get():
        if event.type == pyopengl.QUIT:
            run = False
        if event.type == pyopengl.KEYDOWN:
            if event.key == pyopengl.K_RIGHT:
                playerX_change = 1
            if event.key == pyopengl.K_LEFT:
                playerX_change = -1
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.6
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.6
            if event.key == pyopengl.K_SPACE:
                if bullet_state == "ready":
                    bullet_music = mixer.Sound("laser.wav")
                    bullet_music.play()
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pyopengl.KEYUP:
            if event.key == pyopengl.K_RIGHT or event.key == pyopengl.K_LEFT:
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
        collision_music = mixer.Sound("explosion.wav")
        collision_music.play()
        bulletY = playerY
        bullet_state = "ready"
        score += 1
        # print(score)
        enemyX = random.randint(0, 936)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX,textY)
    pyopengl.display.update()
