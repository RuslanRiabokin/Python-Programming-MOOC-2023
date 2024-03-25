# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball_color = (72, 209, 204)  # Туркисовый цвет
ball_radius = 20
ball_position = [320, 240]  # Начальное положение мяча
ball_velocity = [5, 5]  # Начальная скорость мяча по x и y

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Обновляем положение мяча
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Проверяем столкновение мяча с краями окна
    if ball_position[0] + ball_radius >= 640 or ball_position[0] - ball_radius <= 0:
        ball_velocity[0] = -ball_velocity[0]  # Меняем направление по x
    if ball_position[1] + ball_radius >= 480 or ball_position[1] - ball_radius <= 0:
        ball_velocity[1] = -ball_velocity[1]  # Меняем направление по y

    # Заполняем окно черным цветом
    window.fill((0, 0, 0))

    # Рисуем мяч
    pygame.draw.circle(window, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Отображаем все изменения
    pygame.display.flip()

    clock.tick(60)
