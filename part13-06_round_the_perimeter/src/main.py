# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

# Define the starting position and velocities
x = 0  # Start from the left side
y = 0  # Start from the top
velocity_x = 1  # Move to the right initially
velocity_y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    # Update the position
    x += velocity_x
    y += velocity_y
    
    # Check if the robot reaches the perimeter boundaries and adjust velocities accordingly
    if x + robot.get_width() >= 640 and y == 0:  # Move downwards from the right side
        velocity_x = 0
        velocity_y = 1
    elif x + robot.get_width() >= 640 and y + robot.get_height() >= 480:  # Move from right to left on the bottom
        velocity_x = -1
        velocity_y = 0
    elif x == 0 and y + robot.get_height() >= 480:  # Move from bottom to top on the left side
        velocity_x = 0
        velocity_y = -1
    elif x == 0 and y == 0:  # Move from left to right on the top
        velocity_x = 1
        velocity_y = 0

    clock.tick(60)

