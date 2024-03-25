# WRITE YOUR SOLUTION HERE:
import pygame
import random

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

# Draw one thousand robots at random positions
for _ in range(1000):
    x = random.randint(0, window_width - robot.get_width())
    y = random.randint(0, window_height - robot.get_height())
    window.blit(robot, (x, y))

# Update the display
pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

