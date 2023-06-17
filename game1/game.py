# pip install pygame
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("TEST GAME")
icon = pygame.image.load('hero.png')
pygame.display.set_icon(icon)
bg = pygame.image.load("bg.jpg")
player = pygame.image.load("hero.png")
posX = 400
posY = 400
move = 1

while True:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and posX>0:
        posX-=move
    if keys[pygame.K_RIGHT] and posX<800:
        posX+=move

    screen.blit(bg,(0,0))
    screen.blit(player, (posX, posY))
    pygame.display.update()
