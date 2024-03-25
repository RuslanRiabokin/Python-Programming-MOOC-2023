# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_top = pygame.image.load("robot.png")
robot_bottom = pygame.image.load("robot.png")

# Define the starting positions and velocities for both robots
top_x = 0  # Start from the left side
top_y = 50  # Slightly below the top edge
top_velocity_x = 1  # Move to the right initially
top_velocity_y = 0

bottom_x = 0  # Start from the left side
bottom_y = 300  # Slightly above the bottom edge
bottom_velocity_x = 2  # Move to the right initially (twice faster)
bottom_velocity_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))
    window.blit(robot_top, (top_x, top_y))
    window.blit(robot_bottom, (bottom_x, bottom_y))
    pygame.display.flip()
    
    # Update the positions of both robots
    top_x += top_velocity_x
    top_y += top_velocity_y
    
    bottom_x += bottom_velocity_x
    bottom_y += bottom_velocity_y
    
    # Check if the top robot reaches the perimeter boundaries and adjust velocities accordingly
    if top_x + robot_top.get_width() >= 640:  # Reached the right edge
        top_velocity_x = -1  # Move to the left
        top_velocity_y = 0
    elif top_x <= 0:  # Reached the left edge
        top_velocity_x = 1  # Move to the right
        top_velocity_y = 0
    
    # Check if the bottom robot reaches the perimeter boundaries and adjust velocities accordingly
    if bottom_x + robot_bottom.get_width() >= 640:  # Reached the right edge
        bottom_velocity_x = -2  # Move to the left (twice faster)
        bottom_velocity_y = 0
    elif bottom_x <= 0:  # Reached the left edge
        bottom_velocity_x = 2  # Move to the right (twice faster)
        bottom_velocity_y = 0

    clock.tick(60)
