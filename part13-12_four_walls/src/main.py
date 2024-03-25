# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")
robot_width, robot_height = robot.get_size()
x = (window_width - robot_width) // 2
y = (window_height - robot_height) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 2
        if x < 0:  # Проверка на выход за левую границу окна
            x = 0
    if keys[pygame.K_RIGHT]:
        x += 2
        if x > window_width - robot_width:  # Проверка на выход за правую границу окна
            x = window_width - robot_width
    if keys[pygame.K_UP]:
        y -= 2
        if y < 0:  # Проверка на выход за верхнюю границу окна
            y = 0
    if keys[pygame.K_DOWN]:
        y += 2
        if y > window_height - robot_height:  # Проверка на выход за нижнюю границу окна
            y = window_height - robot_height

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
