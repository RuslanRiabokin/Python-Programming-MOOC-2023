# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_image = pygame.image.load("robot.png")
robot_width, robot_height = robot_image.get_size()

clock = pygame.time.Clock()

class Robot:
    def __init__(self):
        self.x = random.randint(0, 640 - robot_width)  # Случайное положение по x
        self.y = -robot_height  # Начинаем за пределами окна
        self.falling = True
        self.direction = random.choice([-1, 1])  # Случайное направление (влево или вправо)
        self.speed = random.randint(1, 3)  # Случайная скорость

    def update(self):
        if self.falling:
            self.y += self.speed
            if self.y >= 480 - robot_height:  # Если робот достиг земли
                self.falling = False
        else:
            self.x += self.direction * self.speed
            if self.x <= -robot_width or self.x >= 640:  # Если робот вышел за пределы экрана
                self.remove = True

    def draw(self, surface):
        surface.blit(robot_image, (self.x, self.y))

robots = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    
    
    if random.random() < 0.01:
        robots.append(Robot())

    # Обновляем и рисуем всех роботов
    for robot in robots:
        robot.update()
        robot.draw(window)

    # Удаляем роботов, которые вышли за пределы экрана
    robots = [robot for robot in robots if not hasattr(robot, 'remove')]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
