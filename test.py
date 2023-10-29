import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Пинг-понг"
        self.ball_skin = "ball1.png"
        self.left_racket_skin = "left_racket1.png"
        self.right_racket_skin = "right_racket1.png"
        self.board_skin = "bard1.png"
        self.init_ui()

    def init_ui(self):
        # Создаем меню
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        # Создаем пункты меню
        game_menu = QMenu("Игра", menubar)
        skins_menu = QMenu("Скины", menubar)
        exit_menu = QAction("Выход", self)

        # Добавляем пункты меню в менюбар
        menubar.addMenu(game_menu)
        menubar.addMenu(skins_menu)
        exit_menu.triggered.connect(self.close)

        # Создаем подпункты меню "Скины"
        board_skins_menu = QMenu("Доска", skins_menu)
        ball_skins_menu = QMenu("Мяч", skins_menu)
        racket_skins_menu = QMenu("Ракетки", skins_menu)

        # Добавляем подпункты меню "Скины" в меню "Скины"
        skins_menu.addMenu(board_skins_menu)
        skins_menu.addMenu(ball_skins_menu)
        skins_menu.addMenu(racket_skins_menu)

        # Создаем кнопки для выбора скинов
        board_skin_buttons = [
            QPushButton(skin, self) for skin in ["bard1.png", "bard2.png", "bard3.png"]
        ]
        ball_skin_buttons = [
            QPushButton(skin, self) for skin in ["ball1.png", "ball2.png", "ball3.png"]
        ]
        left_racket_skin_buttons = [
            QPushButton(skin, self) for skin in ["left_racket1.png", "left_racket2.png", "left_racket3.png"]
        ]
        right_racket_skin_buttons = [
            QPushButton(skin, self) for skin in ["right_racket1.png", "right_racket2.png", "right_racket3.png"]
        ]

        # Добавляем кнопки для выбора скинов в подпункты меню "Скины"
        board_skins_menu.addActions(board_skin_buttons)
        ball_skins_menu.addActions(ball_skin_buttons)
        racket_skins_menu.addActions(left_racket_skin_buttons + right_racket_skin_buttons)

        # Соединяем сигналы кнопок с соответствующими слотами
        for button in board_skin_buttons:
            button.clicked.connect(self.set_board_skin)
        for button in ball_skin_buttons:
            button.clicked.connect(self.set_ball_skin)
        for button in left_racket_skin_buttons:
            button.clicked.connect(self.set_left_racket_skin)
        for button in right_racket_skin_buttons:
            button.clicked.connect(self.set_right_racket_skin)

        # Создаем игровое поле
        self.board = QLabel(self)
        self.board.setPixmap(QPixmap(self.board_skin))
        self.board.setGeometry(0, 0, 600, 400)

        # Создаем ракетки
        self.left_racket = QLabel(self)
        self.left_racket.setPixmap(QPixmap(self.left_racket_skin))
        self.left_racket.setGeometry(20, 180, 100, 20)

        # Создаем ракетки
        self.left_racket = QLabel(self)
        self.left_racket.setPixmap(QPixmap(self.right_racket_skin))
        self.left_racket.setGeometry(20, 180, 100, 20)

        # Создаем мяч
        self.ball = QLabel(self)
        self.ball.setPixmap(QPixmap(self.ball_skin))
        self.ball.setGeometry(300, 200, 20, 20)

        # Создаем левую стенку
        self.left_wall = QLabel(self)
        self.left_wall.setGeometry(0, 0, 20, 400)

        # Задаем цвет левой стены
        self.left_wall.setStyleSheet("background-color: rgb(255, 0, 0);")

        # Создаем правую стенку
        self.right_wall = QLabel(self)
        self.right_wall.setGeometry(580, 0, 20, 400)

        # Задаем цвет правой стены
        self.right_wall.setStyleSheet("background-color: rgb(0, 0, 255);")

        
        # Создаем таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

        # Создаем переменные для хранения состояния игры
        self.left_score = 0
        self.right_score = 0
        self.left_serving = True

        # Устанавливаем фокус на левую ракетку
        self.left_racket.setFocus()

        self.show()

    def set_board_skin(self, action):
        self.board_skin = action.text()
        self.board.setPixmap(QPixmap(self.board_skin))

    def set_ball_skin(self, action):
        self.ball_skin = action.text()
        self.ball.setPixmap(QPixmap(self.ball_skin))

    def set_left_racket_skin(self, action):
        self.left_racket_skin = action.text()
        self.left_racket.setPixmap(QPixmap(self.left_racket_skin))

    def set_right_racket_skin(self, action):
        self.right_racket_skin = action.text()
        self.right_racket.setPixmap(QPixmap(self.right_racket_skin))

    def update(self):
        # Обновляем положение мяча
        self.ball.move(self.ball.x() + self.ball_x_vel, self.ball.y() + self.ball_y_vel)

        # Проверяем, столкнулся ли мяч со стеной или ракеткой
        if self.ball.x() <= 0 or self.ball.x() >= 580:
            self.ball_x_vel = -self.ball_x_vel
        elif self.ball.y() <= 0:
            self.ball_y_vel = -self.ball_y_vel
        elif self.ball.y() + 20 >= 380:
            if self.left_serving:
                self.left_score += 1
            else:
                self.right_score += 1
            self.ball.move(300, 200)
            self.ball_x_vel = random.randint(-5, 5)
            self.ball_y_vel = random.randint(-5, 5)
            self.left_serving = not self.left_serving

        # Проверяем, закончилась ли игра
        if self.left_score >= 11 or self.right_score >= 11:
            self.timer.stop()

    def keyPressEvent(self, event):
        # Движение левой ракетки
        if event.key() == Qt.Key.Up:
            self.left_racket.move(self.left_racket.x(), self.left_racket.y() - 5)
        elif event.key() == Qt.Key.Down:
            self.left_racket.move(self.left_racket.x(), self.left_racket.y() + 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())