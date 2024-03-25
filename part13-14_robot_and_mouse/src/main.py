# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_width, robot_height = robot.get_size()  # Получаем размеры изображения робота

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0] - robot_width / 2  # Центрируем робота по горизонтали
            target_y = event.pos[1] - robot_height / 2  # Центрируем робота по вертикали

        if event.type == pygame.QUIT:
            exit(0)

    # Плавное перемещение робота к цели
    dx = target_x - robot_x
    dy = target_y - robot_y
    distance = max(abs(dx), abs(dy))  # Максимальное расстояние по одной из осей
    if distance > 0:
        speed = min(5, distance)  # Увеличиваем максимальную скорость перемещения
        ratio = speed / distance
        robot_x += dx * ratio
        robot_y += dy * ratio

    window.fill((0, 0, 0))
    window.blit(robot, (int(robot_x), int(robot_y)))  # Преобразуем координаты в целые числа для blit
    pygame.display.flip()

    clock.tick(440)
