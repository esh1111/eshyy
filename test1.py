import pygame
import sys
import time
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
BARD_WIDTH, BARD_HEIGHT = 30, 100
BALL_SIZE = 50
PADDLE_OFFSET = 20
MENU_BACKGROUND = "menu_fon.png"
BACKGROUND = "fon.png"
BALL_IMAGE = "ball.png"
PADDLE_LEFT_IMAGE = "left_rocket.png"
PADDLE_RIGHT_IMAGE = "right_rocket.png"
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60
BALL_SPEED = 5
PADDLE_SPEED = 10
ROUND_DURATION = 3  # Длительность раунда в секундах
MAX_ROUNDS = 10

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Загрузка изображений
background = pygame.image.load(BACKGROUND)
menu_background = pygame.image.load(MENU_BACKGROUND)
ball = pygame.image.load(BALL_IMAGE)
paddle_left = pygame.image.load(PADDLE_LEFT_IMAGE)
paddle_right = pygame.image.load(PADDLE_RIGHT_IMAGE)

# Инициализация начальных параметров
ball_x = (WIDTH - BALL_SIZE) // 2
ball_y = (HEIGHT - BALL_SIZE) // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED
paddle_left_y = (HEIGHT - BARD_HEIGHT) // 2
paddle_right_y = (HEIGHT - BARD_HEIGHT) // 2
paddle_left_dy = 0
paddle_right_dy = 0
round_start_time = time.time()
round_count = 0
left_score = 0
right_score = 0

# Функция для отображения текста
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Основной игровой цикл
running = True
in_menu = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif in_menu:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    in_menu = False
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    in_menu = True
                elif event.key == K_w:
                    paddle_left_dy = -PADDLE_SPEED
                elif event.key == K_s:
                    paddle_left_dy = PADDLE_SPEED
                elif event.key == K_UP:
                    paddle_right_dy = -PADDLE_SPEED
                elif event.key == K_DOWN:
                    paddle_right_dy = PADDLE_SPEED
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    paddle_left_dy = 0
                elif event.key == K_UP or event.key == K_DOWN:
                    paddle_right_dy = 0

    if in_menu:
        screen.blit(menu_background, (0, 0))
        display_text("Меню", pygame.font.Font(None, 36), WHITE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
    else:
        screen.blit(background, (0, 0))

        # Обновление позиции мяча
        ball_x += ball_dx
        ball_y += ball_dy

        # Отскок мяча от верхней и нижней границ
        if ball_y < 0 or ball_y > HEIGHT - BALL_SIZE:
            ball_dy *= -1

        # Отскок мяча от ракеток
        if (
            (ball_x < PADDLE_OFFSET + BARD_WIDTH)
            and (paddle_left_y < ball_y < paddle_left_y + BARD_HEIGHT)
        ) or (
            (ball_x + BALL_SIZE > WIDTH - PADDLE_OFFSET - BARD_WIDTH)
            and (paddle_right_y < ball_y < paddle_right_y + BARD_HEIGHT)
        ):
            ball_dx *= -1

        # Проверка, ушел ли мяч за левую или правую границу
        if ball_x < 0:
            right_score += 1
            if right_score >= MAX_ROUNDS:
                display_text("Синий выиграл", pygame.font.Font(None, 36), BLUE, WIDTH // 2, HEIGHT // 2)
                pygame.display.flip()
                time.sleep(3)
                in_menu = True
            else:
                ball_x = (WIDTH - BALL_SIZE) // 2
                ball_y = (HEIGHT - BALL_SIZE) // 2
                ball_dx = BALL_SPEED
                ball_dy = BALL_SPEED
                paddle_left_y = (HEIGHT - BARD_HEIGHT) // 2
                paddle_right_y = (HEIGHT - BARD_HEIGHT) // 2
                round_start_time = time.time()
        elif ball_x + BALL_SIZE > WIDTH:
            left_score += 1
            if left_score >= MAX_ROUNDS:
                display_text("Зеленый выиграл", pygame.font.Font(None, 36), GREEN, WIDTH // 2, HEIGHT // 2)
                pygame.display.flip()
                time.sleep(3)
                in_menu = True
            else:
                ball_x = (WIDTH - BALL_SIZE) // 2
                ball_y = (HEIGHT - BALL_SIZE) // 2
                ball_dx = -BALL_SPEED
                ball_dy = BALL_SPEED
                paddle_left_y = (HEIGHT - BARD_HEIGHT) // 2
                paddle_right_y = (HEIGHT - BARD_HEIGHT) // 2
                round_start_time = time.time()

        # Обновление позиции ракеток
        paddle_left_y += paddle_left_dy
        paddle_right_y += paddle_right_dy

        # Проверка столкновения ракеток с верхней и нижней границей
        if paddle_left_y < 0:
            paddle_left_y = 0
        if paddle_left_y > HEIGHT - BARD_HEIGHT:
            paddle_left_y = HEIGHT - BARD_HEIGHT
        if paddle_right_y < 0:
            paddle_right_y = 0
        if paddle_right_y > HEIGHT - BARD_HEIGHT:
            paddle_right_y = HEIGHT - BARD_HEIGHT

        screen.blit(paddle_left, (PADDLE_OFFSET, paddle_left_y))
        screen.blit(paddle_right, (WIDTH - PADDLE_OFFSET - BARD_WIDTH, paddle_right_y))
        screen.blit(ball, (ball_x, ball_y))

        # Вывод счета
        display_text(f"{left_score} : {right_score}", pygame.font.Font(None, 36), WHITE, WIDTH // 2, 20)

        pygame.display.flip()

        # Пауза между раундами
        if time.time() - round_start_time >= ROUND_DURATION:
            ball_dx = -ball_dx

# Завершение Pygame
pygame.quit()
sys.exit()
