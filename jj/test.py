import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Загрузка изображений
background = pygame.image.load("jj\_fon.png")
menu_background = pygame.image.load("jj\_menu_fon.png")
ball = pygame.image.load("jj\_ball.png")
bard = pygame.image.load("jj\_bard.png")
left_rocket = pygame.image.load("jj\_left_rocket.png")
right_rocket = pygame.image.load("jj\_right_rocket.png")

# Размеры объектов
ball_rect = ball.get_rect()
bard_rect = bard.get_rect()
left_rocket_rect = left_rocket.get_rect()
right_rocket_rect = right_rocket.get_rect()

left_rocket_rect.height = 130  # Изменение высоты левой ракетки
right_rocket_rect.height = 130

# Начальные позиции объектов
ball_rect.center = (WIDTH // 2, HEIGHT // 2)
bard_rect.center = (WIDTH // 2, HEIGHT // 2)
left_rocket_rect.topleft = (20, (HEIGHT - left_rocket_rect.height) // 2)
right_rocket_rect.topright = (WIDTH - 20, (HEIGHT - right_rocket_rect.height) // 2)

# Скорость мяча
ball_speed = [7, 7]

# Скорость ракеток
left_rocket_speed = 5
right_rocket_speed = 5

# Очки
left_score = 0
right_score = 0
rounds = 0

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Основной игровой цикл
running = False
menu = True
paused = False

while menu:
    screen.blit(menu_background, (0, 0))
    quit_text = font.render("Нажмите Enter", True, WHITE)

    screen.blit(quit_text, (WIDTH // 2 - 100, 400))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                menu = False

while not running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    if paused:
        pause_text = font.render("Пауза", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - 40, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(0.5)
        continue

    # Движение ракеток
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_rocket_rect.y -= left_rocket_speed
    if keys[pygame.K_s]:
        left_rocket_rect.y += left_rocket_speed
    if keys[pygame.K_UP]:
        right_rocket_rect.y -= right_rocket_speed
    if keys[pygame.K_DOWN]:
        right_rocket_rect.y += right_rocket_speed

    # Границы для ракеток
    left_rocket_rect.y = max(0, left_rocket_rect.y)
    left_rocket_rect.y = min(HEIGHT - left_rocket_rect.height, left_rocket_rect.y)
    right_rocket_rect.y = max(0, right_rocket_rect.y)
    right_rocket_rect.y = min(HEIGHT - right_rocket_rect.height, right_rocket_rect.y)

    # Движение мяча
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    top_wall = 100  # Высота верхней стенки
    bottom_wall = HEIGHT - 100  # Высота нижней стенки

    if ball_rect.top <= top_wall or ball_rect.bottom >= bottom_wall:
        ball_speed[1] = -ball_speed[1]

    # Отскок мяча от ракеток
    if ball_rect.colliderect(left_rocket_rect) or ball_rect.colliderect(right_rocket_rect):
        ball_speed[0] = -ball_speed[0]

    # Мяч вышел за границы
    if ball_rect.left <= 0:
        right_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] = 7
        ball_speed[1] = 7
        rounds += 1

    if ball_rect.right >= WIDTH:
        left_score += 1
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] = -7
        ball_speed[1] = -7
        rounds += 1

    # Проверка на завершение игры
    if rounds >= 10:
        if left_score > right_score:
            winner_text = font.render("Зеленый выиграл", True, GREEN)
        elif left_score < right_score:
            winner_text = font.render("Синий выиграл", True, BLUE)
        else:
            winner_text = font.render("Ничья", True, WHITE)

        screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        pygame.display.flip()
        time.sleep(2)
        running = True

    screen.blit(bard, bard_rect)
    screen.blit(left_rocket, left_rocket_rect)
    screen.blit(right_rocket, right_rocket_rect)
    screen.blit(ball, ball_rect)

    left_score_text = font.render(str(left_score), True, GREEN)
    right_score_text = font.render(str(right_score), True, BLUE)
    screen.blit(left_score_text, (WIDTH // 4, 20))
    screen.blit(right_score_text, (3 * WIDTH // 4 - 20, 20))

    pygame.display.flip()

# Завершение игры
pygame.quit()
sys.exit()
