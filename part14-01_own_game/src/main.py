import pygame
import random
import sys

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid Collector")

# Load images
robot_image = pygame.image.load("robot.png")
robot_width, robot_height = robot_image.get_size()
coin_image = pygame.image.load("coin.png")
coin_width, coin_height = coin_image.get_size()
monster_image = pygame.image.load("monster.png")
monster_width, monster_height = monster_image.get_size()

clock = pygame.time.Clock()


class Robot:
    def __init__(self):
        # Initialize the robot's position and speed
        # Accessing global variables directly for convenience
        self.x = window_width // 2 - robot_width // 2
        self.y = window_height - robot_height - 20
        self.speed = 5

    def update(self, direction):
        # Update the robot's position based on the input direction
        # Accessing global variables directly for convenience
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        # Ensure the robot stays within the window bounds
        self.x = max(0, min(window_width - robot_width, self.x))

    def draw(self, surface):
        # Draw the robot on the given surface
        # Accessing global variables directly for convenience
        surface.blit(robot_image, (self.x, self.y))


class Coin:
    def __init__(self):
        # Initialize the coin's position and speed
        # Accessing global variables directly for convenience
        self.x = random.randint(0, window_width - coin_width)
        self.y = -coin_height
        self.speed = random.randint(1, 3)

    def update(self):
        # Update the coin's position
        self.y += self.speed

    def draw(self, surface):
        # Draw the coin on the given surface
        surface.blit(coin_image, (self.x, self.y))


class Monster:
    def __init__(self):
        # Initialize the monster's position and speed
        # Accessing global variables directly for convenience
        self.x = random.randint(0, window_width - monster_width)
        self.y = -monster_height
        self.speed = random.randint(1, 3)

    def update(self):
        # Update the monster's position
        self.y += self.speed

    def draw(self, surface):
        # Draw the monster on the given surface
        surface.blit(monster_image, (self.x, self.y))


def display_score(score, color, position):
    # Display the score on the screen
    font = pygame.font.SysFont(None, 36)
    text = font.render(score, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = position
    window.blit(text, text_rect)


def game_over(score, coins_missed):
    # Display the game over screen
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 50))
    window.blit(text, text_rect)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Points: " + str(score), True, (255, 0, 0))
    score_rect = score_text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(score_text, score_rect)

    enter_text = font.render("Click on the cross at the top right", True, (0, 0, 255))  # Changed color here
    enter_rect = enter_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
    window.blit(enter_text, enter_rect)

    missed_text = font.render("Coins missed: " + str(coins_missed), True, (0, 255, 0))
    missed_rect = missed_text.get_rect(center=(window_width // 2, window_height // 2 + 100))
    window.blit(missed_text, missed_rect)

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False


def main():
    # Main function to run the game
    robot = Robot()
    coins = []
    monsters = []
    score = 0
    coins_missed = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            robot.update("left")
        if keys[pygame.K_RIGHT]:
            robot.update("right")

        # Generate coins
        if random.random() < 0.02:
            coins.append(Coin())

        # Generate monsters
        if random.random() < 0.01:
            monsters.append(Monster())

        # Update and draw coins
        window.fill((255, 255, 255))  # White background
        for coin in coins:
            coin.update()
            coin.draw(window)

            # Check for collision with robot
            if (robot.x < coin.x + coin_width and
                    robot.x + robot_width > coin.x and
                    robot.y < coin.y + coin_height and
                    robot.y + robot_height > coin.y):
                coins.remove(coin)
                score += 1

            # Check if coin missed
            if coin.y > window_height:
                coins.remove(coin)
                coins_missed += 1

        # Update and draw monsters
        for monster in monsters:
            monster.update()
            monster.draw(window)

            # Check for collision with robot
            if (robot.x < monster.x + monster_width and
                    robot.x + robot_width > monster.x and
                    robot.y < monster.y + monster_height and
                    robot.y + robot_height > monster.y):
                game_over(score, coins_missed)

            # Remove monsters that go off-screen
            if monster.y > window_height:
                monsters.remove(monster)

        robot.draw(window)
        display_score("Points: " + str(score), (255, 0, 0), (10, 10))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
