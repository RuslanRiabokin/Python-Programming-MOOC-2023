# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")  # Загружаем изображение для второго робота
robot_width, robot_height = robot1.get_size()
x1 = (window_width - robot_width) // 4  # Начальная позиция для первого робота
x2 = (3 * window_width - robot_width) // 4  # Начальная позиция для второго робота
y1 = y2 = (window_height - robot_height) // 2  # Обе позиции роботов по вертикали

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Управление первым роботом
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1 -= 2
        if x1 < 0:
            x1 = 0
    if keys[pygame.K_RIGHT]:
        x1 += 2
        if x1 > window_width - robot_width:
            x1 = window_width - robot_width
    if keys[pygame.K_UP]:
        y1 -= 2
        if y1 < 0:
            y1 = 0
    if keys[pygame.K_DOWN]:
        y1 += 2
        if y1 > window_height - robot_height:
            y1 = window_height - robot_height

    # Управление вторым роботом
    if keys[pygame.K_a]:
        x2 -= 2
        if x2 < 0:
            x2 = 0
    if keys[pygame.K_d]:
        x2 += 2
        if x2 > window_width - robot_width:
            x2 = window_width - robot_width
    if keys[pygame.K_w]:
        y2 -= 2
        if y2 < 0:
            y2 = 0
    if keys[pygame.K_s]:
        y2 += 2
        if y2 > window_height - robot_height:
            y2 = window_height - robot_height

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
