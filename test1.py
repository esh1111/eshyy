import pygame, random

# Инициализация PyGame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Загрузка изображений
ball_image = pygame.image.load("ball.png")
board_image = pygame.image.load("board.png")
left_rocket_image = pygame.image.load("left_rocket.png")
right_rocket_image = pygame.image.load("right_rocket.png")
menu_background_image = pygame.image.load("menu_background.png")

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Создание объектов
ball = pygame.Rect(SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 25, 50, 50)
board = pygame.Rect(SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 200, 600, 400)
left_rocket = pygame.Rect(SCREEN_WIDTH / 2 - 320, SCREEN_HEIGHT / 2 - 100, 13, 100)
right_rocket = pygame.Rect(SCREEN_WIDTH / 2 + 287, SCREEN_HEIGHT / 2 - 100, 30, 100)

# Начальное меню
running = True
while running:
    screen.blit(menu_background_image, (0, 0))

    # Кнопка "Играть"
    if pygame.mouse.get_pressed()[0]:
        if 100 < pygame.mouse.get_pos()[0] < 700 and 200 < pygame.mouse.get_pos()[1] < 400:
            running = False

    # Кнопка "Выход"
    if pygame.mouse.get_pressed()[0]:
        if 100 < pygame.mouse.get_pos()[0] < 700 and 400 < pygame.mouse.get_pos()[1] < 600:
            pygame.quit()
            quit()

    pygame.display.update()

# Игра
running = True
rounds = 1
while running:
    # Отрисовка экрана
    screen.blit(board_image, (0, 0))
    screen.blit(ball_image, ball)
    screen.blit(left_rocket_image, left_rocket)
    screen.blit(right_rocket_image, right_rocket)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Движение ракеток
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_rocket.y -= 5
            elif event.key == pygame.K_s:
                left_rocket.y += 5

    # Движение мяча
    ball.x += ball.vx
    ball.y += ball.vy

    # Отскок мяча от ракеток
    if ball.colliderect(left_rocket):
        ball.vx = -ball.vx
        ball.vy += 5 * random.randint(-1, 1)
    if ball.colliderect(right_rocket):
        ball.vx = ball.vx
        ball.vy += 5 * random.randint(-1, 1)

    # Отскок мяча от стен
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        ball.vy = -ball.vy

    # Завершение игры
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        rounds += 1
        if rounds == 11:
            running = False

    pygame.display.update()
        # Вывод счета
    if ball.left < 0:
        score_left += 1
    elif ball.right > SCREEN_WIDTH:
        score_right += 1

    # Вывод счета на экран
    font = pygame.font.Font("freesansbold.ttf", 30)
    text_score_left = font.render("Счет: {} - {}".format(score_left, score_right), True, (255, 255, 255))
    screen.blit(text_score_left, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 200))

    pygame.display.update()

# Вывод результата игры
if score_left > score_right:
    print("Победил игрок 1!")
elif score_right > score_left:
    print("Победил игрок 2!")
else:
    print("Ничья!")

# Завершение игры
pygame.quit()
quit()

