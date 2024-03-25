# WRITE YOUR SOLUTION HERE:
import pygame
import time
import math

pygame.init()
window_width = 640
window_height = 480
display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

def draw_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 255, 255), (window_width // 2, window_height // 2), 200, 2)

    # Рисуем цифры на циферблате
    font = pygame.font.SysFont(None, 36)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = int(window_width // 2 + 180 * math.cos(angle))
        y = int(window_height // 2 + 180 * math.sin(angle))
        text = font.render(str(i), True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        display.blit(text, text_rect)

    # Рисуем стрелки
    draw_hand((hours % 12) * 30 + (minutes / 60) * 30, 100, 6, (0, 0, 255))  # Часовая стрелка
    draw_hand(minutes * 6 + (seconds / 60) * 6, 140, 4, (0, 255, 0))  # Минутная стрелка
    draw_hand(seconds * 6, 180, 2, (255, 0, 0))  # Секундная стрелка

    pygame.display.flip()

def draw_hand(angle, length, width, color):
    angle_rad = math.radians(angle - 90)
    x = window_width // 2 + length * math.cos(angle_rad)
    y = window_height // 2 + length * math.sin(angle_rad)
    pygame.draw.line(display, color, (window_width // 2, window_height // 2), (x, y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    clock.tick(60)

pygame.quit()
