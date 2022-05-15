import pygame
import classes_models
from visuals.constants import *
import math
import random

mol = classes_models.Molecule(120, 120, 20, 5)

WINDOWWIDTH = 500
WINDOWHEIGHT = 500

angle = random.randrange(0, 360, 10) * math.pi / 180

Vx = round(mol.speed * math.sin(angle))
Vy = round(mol.speed * math.cos(angle))

pygame.init()
win = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption("Visualizer")

runFlag = True

while runFlag:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runFlag = False

    keys = pygame.key.get_pressed()

    win.fill((0, 0, 0))
    pygame.draw.circle(win, GREEN, (mol.xc, mol.yc), mol.radius)

    mol.xc = mol.xc + Vx
    mol.yc = mol.yc + Vy

    if mol.xc > WINDOWWIDTH - mol.radius:
        mol.xc = WINDOWWIDTH - mol.radius
        Vx = -Vx
    if mol.xc < mol.radius:
        mol.xc = mol.radius
        Vx = -Vx
    if mol.yc > WINDOWHEIGHT - mol.radius:
        mol.yc = WINDOWHEIGHT - mol.radius
        Vy = -Vy
    if mol.yc < mol.radius:
        mol.yc = mol.radius
        Vy = -Vy

    pygame.display.update()

pygame.quit()
