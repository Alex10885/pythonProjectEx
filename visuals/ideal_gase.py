from random import randint, uniform
import constants
import pygame
import sys

# Готовим 100 шариков в случайных местах случайного радиуса и цвета
N = 100
circs = [
    {
        'xy': [uniform(0, constants.WINDOWWIDTH), uniform(0, constants.WINDOWHEIGHT)],
        'r': randint(2, 10),
        'color': [randint(0, 255), randint(0, 255), randint(0, 255)]
    }
    for __ in range(N)]
circs.sort(key=lambda circ: -circ['r'])  # Сортируем, чтобы большие не заслоняли маленьких

# Немного pygame-магии
pygame.init()
screen = pygame.display.set_mode((constants.WINDOWWIDTH, constants.WINDOWHEIGHT))
pygame.display.set_caption("Ideal Gase")
fps = pygame.time.Clock()


# Обновляем коодинаты всех шариков
def update():
    for circ in circs:
        circ['xy'][0] += uniform(-5, 5) / circ['r']
        circ['xy'][1] += uniform(-5, 5) / circ['r']


# Чистим экран и отрисовываем каждый шарик
def render():
    screen.fill((0, 0, 0))  # Заливаем всё чёрным
    for circ in circs:
        pygame.draw.circle(screen, circ['color'], list(map(int, circ['xy'])), circ['r'], 0)
    pygame.display.update()
    fps.tick(60)  # Не обновляем экран чаще, чем 60 раз в секунду


# Главный цикл: пока на нажали крестик обновляем и отрисовываем
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update()
    render()
