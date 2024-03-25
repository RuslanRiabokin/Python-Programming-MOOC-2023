# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

num_robots = 10
radius = 100
angle_step = 2 * math.pi / num_robots
angles = [i * angle_step for i in range(num_robots)]  # Углы для каждого робота
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))

    for i in range(num_robots):
        x = 320 + math.cos(angles[i]) * radius - robot.get_width() / 2
        y = 240 + math.sin(angles[i]) * radius - robot.get_height() / 2
        window.blit(robot, (x, y))
        angles[i] += 0.01  # Увеличиваем угол для следующего кадра

    pygame.display.flip()
    clock.tick(60)
