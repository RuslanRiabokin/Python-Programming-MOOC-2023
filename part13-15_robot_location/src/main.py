# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width, robot_height = robot.get_size()

# Генерируем случайные начальные координаты для робота
robot_x = random.randint(0, window_width - robot_width)
robot_y = random.randint(0, window_height - robot_height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Обработка нажатия кнопки мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем, попал ли клик мышью в робота
            if robot_x <= mouse_x <= robot_x + robot_width and robot_y <= mouse_y <= robot_y + robot_height:
                # Если да, генерируем новые случайные координаты для робота
                robot_x = random.randint(0, window_width - robot_width)
                robot_y = random.randint(0, window_height - robot_height)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
