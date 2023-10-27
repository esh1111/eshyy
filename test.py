import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTabWidget, QPushButton
import random

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пинг-понг")
        self.setFixedSize(600, 400)

        self.play_button = QtWidgets.QPushButton("Играть")
        self.skins_button = QtWidgets.QPushButton("Скин")
        self.exit_button = QtWidgets.QPushButton("Выход")

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.play_button)
        h_layout.addWidget(self.skins_button)
        h_layout.addWidget(self.exit_button)

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(h_layout)

        self.setCentralWidget(main_widget)

        self.play_button.clicked.connect(self.play_game)
        self.skins_button.clicked.connect(self.show_skins)
        self.exit_button.clicked.connect(self.close)

        self.hide()

    def play_game(self):
        self.game_window = GameWindow()
        self.game_window.show()
        self.game_window.ball.x_speed = -5
        self.game_window.game_started = True

    def show_skins(self):
        self.skins_window = SkinsWindow()
        self.skins_window.show()

class GameWindow(QtWidgets.QMainWindow):
    ball_skins = ["vbyfyft;f.png"]
    left_racket_skins = ["нога.png"]
    right_racket_skins = ["XGAAAgGvDeA-1920.png"]

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пинг-понг")
        self.setFixedSize(600, 400)

        self.left_score = 0
        self.right_score = 0
        self.winner = None
        self.game_started = False

        self.ball = Ball()
        self.left_racket = Racket(x=50, y=200)
        self.right_racket = Racket(x=550, y=200)
        self.score_label = QtWidgets.QLabel()
        self.background_board = QtWidgets.QLabel()
        self.background_board.setPixmap(QtGui.QPixmap("прототип стола номер 3.png"))
        self.background_board.setGeometry(0, 0, 600, 400)
        self.setCentralWidget(self.background_board)

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(QtWidgets.QVBoxLayout())
        main_widget.layout().addWidget(self.score_label)
        main_widget.layout().addWidget(self.ball)
        main_widget.layout().addWidget(self.left_racket)
        main_widget.layout().addWidget(self.right_racket)

        self.setCentralWidget(main_widget)

        self.left_racket.key_up = QtCore.Qt.Key_W
        self.left_racket.key_down = QtCore.Qt.Key_S
        self.right_racket.key_up = QtCore.Qt.Key_Up
        self.right_racket.key_down = QtCore.Qt.Key_Down

        self.ball.skin = random.choice(self.ball_skins)
        self.left_racket.skin = random.choice(self.left_racket_skins)
        self.right_racket.skin = random.choice(self.right_racket_skins)

        self.update()

    def update(self):
        if self.game_started:
            self.ball.move()
            self.score_label.setText(f"Счет: {self.left_score} - {self.right_score}")
            self.ball.check_collision(self.left_racket)
            self.ball.check_collision(self.right_racket)

            if self.ball.x < 0 or self.ball.x > 600:
                self.reset_game()

            self.ball.update()
            self.left_racket.update()
            self.right_racket.update()
            self.check_winner()

    def reset_game(self):
        self.game_started = False
        self.left_score = 0
        self.right_score = 0
        self.winner = None
        self.ball.reset()

    def check_winner(self):
        if self.ball.x < 0:
            self.winner = "Правая сторона"
        elif self.ball.x > 600:
            self.winner = "Левая сторона"

    def keyPressEvent(self, event):
        if self.game_started:
            if event.key() == self.left_racket.key_up:
                self.left_racket.move_up()
            elif event.key() == self.left_racket.key_down:
                self.left_racket.move_down()
            elif event.key() == self.right_racket.key_up:
                self.right_racket.move_up()
            elif event.key() == self.right_racket.key_down:
                self.right_racket.move_down()

class Ball(QtWidgets.QLabel):
    ball_skins = ["vbyfyft;f.png"]

    def __init__(self):
        super().__init__()
        self.skin = None
        self.load_skin()
        self.x_speed = 5
        self.y_speed = 5
        self.x = 300
        self.y = 200

    def load_skin(self):
        self.skin = random.choice(self.ball_skins)
        image = QtGui.QImage(self.skin)
        image = image.scaled(100, 100)
        pixmap = QtGui.QPixmap(image)
        self.setPixmap(pixmap)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x < 0 or self.x > 600:
            self.x_speed = -self.x_speed
        if self.y < 0 or self.y > 300:
            self.y_speed = -self.y_speed

    def reset(self):
        self.x = 300
        self.y = 200
        self.x_speed = random.randint(-5, 5)
        self.y_speed = random.randint(-5, 5)

    def check_collision(self, racket):
        if self.x >= racket.x - racket.width / 2 and self.x <= racket.x + racket.width / 2 and self.y >= racket.y - racket.height / 2 and self.y <= racket.y + racket.height / 2:
            self.y_speed = -self.y_speed

class Racket(QtWidgets.QLabel):
    left_racket_skins = ["нога.png"]
    right_racket_skins = ["XGAAAgGvDeA-1920.png"]

    def __init__(self, x, y):
        super().__init__()
        self.speed = 10
        self.skin = None
        self.load_skin()
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20

    def load_skin(self):
        self.skin = random.choice(self.left_racket_skins)
        image = QtGui.QImage(self.skin)
        image = image.scaled(100, 20)
        pixmap = QtGui.QPixmap(image)
        self.setPixmap(pixmap)

    def move_up(self):
        if self.game_started:
            self.y -= self.speed
            if self.y < 0:
                self.y = 0

    def move_down(self):
        if self.game_started:
            self.y += self.speed
            if self.y > 300:
                self.y = 300

class SkinsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Скин")
        self.setFixedSize(600, 400)

        self.ball_tab = QTabWidget()
        self.left_racket_tab = QTabWidget()
        self.right_racket_tab = QTabWidget()

        self.fill_ball_tab()
        self.fill_left_racket_tab()
        self.fill_right_racket_tab()

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(QtWidgets.QVBoxLayout())
        main_widget.layout().addWidget(self.ball_tab)
        main_widget.layout().addWidget(self.left_racket_tab)
        main_widget.layout().addWidget(self.right_racket_tab)

        self.setCentralWidget(main_widget)

    def fill_ball_tab(self):
        for skin in GameWindow.ball_skins:
            button = QPushButton(skin)
            button.clicked.connect(lambda checked, skin=skin: self.set_skin(skin))
            self.ball_tab.addTab(button, skin)

    def fill_left_racket_tab(self):
        for skin in GameWindow.left_racket_skins:
            button = QPushButton(skin)
            button.clicked.connect(lambda checked, skin=skin: self.set_skin(skin))
            self.left_racket_tab.addTab(button, skin)

    def fill_right_racket_tab(self):
        for skin in GameWindow.right_racket_skins:
            button = QPushButton(skin)
            button.clicked.connect(lambda checked, skin=skin: self.set_skin(skin))
            self.right_racket_tab.addTab(button, skin)

    def set_skin(self, skin):
        if self.sender().parent() == self.ball_tab:
            GameWindow.ball_skins = [skin]
        elif self.sender().parent() == self.left_racket_tab:
            GameWindow.left_racket_skins = [skin]
        elif self.sender().parent() == self.right_racket_tab:
            GameWindow.right_racket_skins = [skin]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
