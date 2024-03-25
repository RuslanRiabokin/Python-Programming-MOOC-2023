# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((800, 200))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

x_position = 50  

for _ in range(10):
    window.blit(robot, (x_position, 50))
    x_position += 70  
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

