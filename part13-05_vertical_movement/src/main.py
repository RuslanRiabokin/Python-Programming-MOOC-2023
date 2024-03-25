# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity_y = 1  # Vertical velocity
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    y += velocity_y
    
    # Check if the robot reaches the top or bottom edge of the window
    if y <= 0 or y + robot.get_height() >= 480:
        velocity_y = -velocity_y

    clock.tick(60)
