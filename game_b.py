import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game B: Flappy Bird Mini")

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

bird_size = 30
bird_x = 50
bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.5
jump_strength = -10

pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_top_height = random.randint(50, HEIGHT - pipe_gap - 50)
pipe_speed = 3

font = pygame.font.SysFont(None, 36)
score = 0
passed_pipe = False

clock = pygame.time.Clock()
running = True

def draw_pipes():
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_top_height))
    bottom_height = HEIGHT - pipe_top_height - pipe_gap
    pygame.draw.rect(screen, GREEN, (pipe_x, HEIGHT - bottom_height, pipe_width, bottom_height))

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_vel = jump_strength

    bird_vel += gravity
    bird_y += bird_vel

    pipe_x -= pipe_speed
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_top_height = random.randint(50, HEIGHT - pipe_gap - 50)
        passed_pipe = False

    if bird_y <= 0 or bird_y + bird_size >= HEIGHT:
        running = False
    if (pipe_x < bird_x + bird_size < pipe_x + pipe_width or pipe_x < bird_x < pipe_x + pipe_width):
        if bird_y < pipe_top_height or bird_y + bird_size > pipe_top_height + pipe_gap:
            running = False

    if pipe_x + pipe_width < bird_x and not passed_pipe:
        score += 1
        passed_pipe = True

    pygame.draw.rect(screen, BLUE, (bird_x, bird_y, bird_size, bird_size))
    draw_pipes()
    score_text = font.render(f"Diem: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
