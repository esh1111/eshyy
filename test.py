import sys
import pygame 
from PyQt5 import QtWidgets


# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Инициализация PyQt5
app = QtWidgets.QApplication(sys.argv)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Инициализация PyGame
pygame.init()

# Загрузка изображений
ball_image = pygame.image.load("ball.png")
board_image = pygame.image.load("bard.png")
left_racket_image = pygame.image.load("left_rocket.png")
right_racket_image = pygame.image.load("right_rocket.png")
menu_fon_image = pygame.image.load("menu_fon.png")

# Создание объектов
ball = pygame.Rect(SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2 - 25, 50, 50)
board = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
left_racket = pygame.Rect(10, SCREEN_HEIGHT / 2 - 50, 13, 100)
right_racket = pygame.Rect(SCREEN_WIDTH - 43, SCREEN_HEIGHT / 2 - 50, 30, 100)

# Настройки PyGame
pygame.display.set_caption("Пинг-понг")
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Переменные
left_score = 0
right_score = 0
round_number = 1

# Функции
def draw_objects():
    """Рисование объектов на экране"""
    pygame.draw.rect(screen, pygame.Color("black"), board)
    pygame.draw.rect(screen, pygame.Color("white"), left_racket)
    pygame.draw.rect(screen, pygame.Color("white"), right_racket)
    pygame.draw.rect(screen, pygame.Color("red"), ball)

def update_objects():
    """Обновление положения объектов"""
    global ball, left_racket, right_racket

    # Движение мяча
    ball.x += ball.xvel
    ball.y += ball.yvel

    # Отражение мяча от стенок
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        ball.yvel = -ball.yvel

    # Отражение мяча от ракеток
    if ball.colliderect(left_racket):
        ball.xvel = -ball.xvel

    if ball.colliderect(right_racket):
        ball.xvel = ball.xvel

def check_winner():
    """Проверка победителя"""
    global left_score, right_score

    if ball.right > SCREEN_WIDTH:
        left_score += 1
    elif ball.left < 0:
        right_score += 1

def play_game():
    """Игра в пинг-понг"""
    global ball, left_racket, right_racket, left_score, right_score, round_number

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Управление левой ракеткой
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    left_racket.y -= 5
                elif event.key == pygame.K_s:
                    left_racket.y += 5

            # Управление правой ракеткой
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    right_racket.y -= 5
                elif event.key == pygame.K_DOWN:
                    right_racket.y += 5

        # Обновление объектов
        update_objects()

        # Проверка победителя
        check_winner()

        # Рисование объектов
        draw_objects()

        # Задержка
        pygame.time.delay(10)

        # Переход на следующий раунд
        if round_number == 10:
            if left_score > right_score:
                print("Победил левый игрок!")
            elif right_score > left_score:
                print("Победил правый игрок!")
            else:
                print("Ничья!")
            return

        round_number += 1

        # Отскок мяча от ворот
        if ball.right > SCREEN_WIDTH:
            ball.xvel = -ball.xvel
        elif ball.left < 0:
            ball.xvel = ball.xvel

        # Отскок мяча от ракеток
        if ball.colliderect(left_racket):
            ball.xvel = -ball.xvel

        if ball.colliderect(right_racket):
            ball.xvel = ball.xvel

class Menu(QtWidgets.QWidget):
    def init(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("Пинг-понг")
        self.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Загрузка изображений
        self.menu_fon_image = pygame.image.load("menu_fon.png")

        # Создание кнопок
        self.play_button = QtWidgets.QPushButton("Играть")
        self.exit_button = QtWidgets.QPushButton("Выход")

        # Установка размеров кнопок
        self.play_button.setFixedSize(200, 50)
        self.exit_button.setFixedSize(200, 50)

        # Установка положения кнопок
        self.play_button.move(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 25)
        self.exit_button.move(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 25)

        # Связывание событий с кнопками
        self.play_button.clicked.connect(self.play_game)
        self.exit_button.clicked.connect(QtWidgets.qApp.quit)

    def paintEvent(self, event):
        # Отрисовка фона
        screen.blit(self.menu_fon_image, (0, 0))

        # Отрисовка кнопок
        self.play_button.setStyleSheet("background-color: #000000; color: #ffffff;")
        self.exit_button.setStyleSheet("background-color: #000000; color: #ffffff;")

        self.play_button.render(screen)
        self.exit_button.render(screen)

    def play_game(self):
        # Переход в игру
        self.hide()
        play_game()

def main():
    # Создание окна меню
    menu = Menu()
    menu.show()

    # Запуск основного цикла PyQt5
    app.exec()

if __name__ == "__main__":
    main()