# WRITE YOUR SOLUTION HERE:
import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))

# Load the robot image
robot = pygame.image.load("robot.png")

# Clear the window
window.fill((0, 0, 0))

# Calculate the spacing for the grid
grid_spacing_x = window_width // 10
grid_spacing_y = window_height // 10

# Draw one hundred robots in a grid pattern
for row in range(10):
    for col in range(10):
        x = col * grid_spacing_x
        y = row * grid_spacing_y
        window.blit(robot, (x, y))

# Update the display
pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

