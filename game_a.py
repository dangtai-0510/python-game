import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Di chuyen khoi vuong")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
speed = 5

font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
time_elapsed = 0

running = True
while running:
    dt = clock.tick(60)
    time_elapsed += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    seconds = time_elapsed // 1000
    score_text = font.render(f"Thoi gian: {seconds} s", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
