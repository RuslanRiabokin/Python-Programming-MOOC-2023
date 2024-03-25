import pygame
import random

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid Collector")

# Load images
robot_image = pygame.image.load("robot.png")
robot_width, robot_height = robot_image.get_size()
rock_image = pygame.image.load("rock.png")
rock_width, rock_height = rock_image.get_size()

clock = pygame.time.Clock()

class Robot:
    def __init__(self):
        self.x = window_width // 2 - robot_width // 2
        self.y = window_height - robot_height - 20
        self.speed = 5

    def update(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        # Keep the robot within the window
        self.x = max(0, min(window_width - robot_width, self.x))

    def draw(self, surface):
        surface.blit(robot_image, (self.x, self.y))

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, window_width - rock_width)
        self.y = -rock_height
        self.speed = random.randint(1, 3)

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        surface.blit(rock_image, (self.x, self.y))

def display_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Points: " + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.topright = (window_width - 10, 10)
    window.blit(text, text_rect)

def game_over(score):
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(text, text_rect)
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Points: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
    window.blit(score_text, score_rect)

    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

def main():
    robot = Robot()
    asteroids = []
    score = 0
    running = True
    missed_asteroid = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            robot.update("left")
        if keys[pygame.K_RIGHT]:
            robot.update("right")

        # Generate asteroids
        if random.random() < 0.02:
            asteroids.append(Asteroid())

        # Update and draw asteroids
        window.fill((0, 0, 0))
        for asteroid in asteroids:
            asteroid.update()
            asteroid.draw(window)

            # Check for collision with robot
            if (robot.x < asteroid.x + rock_width and
                robot.x + robot_width > asteroid.x and
                robot.y < asteroid.y + rock_height and
                robot.y + robot_height > asteroid.y):
                asteroids.remove(asteroid)
                score += 1

            # Check if asteroid missed
            if asteroid.y > window_height:
                missed_asteroid = True

            # Remove asteroids that go off-screen
            if asteroid.y > window_height:
                asteroids.remove(asteroid)

        robot.draw(window)
        display_score(score)
        pygame.display.flip()
        clock.tick(60)

        # Check if game over
        if missed_asteroid:
            game_over(score)

    pygame.quit()

if __name__ == "__main__":
    main()
