import sys
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QLabel, QPushButton, QDialog, QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пинг-понг")
        self.setFixedSize(600, 400)

        # Создаем изображения для доски, мяча и ракеток
        self.skins_board = {
            "bard1": QImage("images/bard1.png"),
            "bard2": QImage("images/bard2.png"),
            "bard3": QImage("images/bard3.png"),
        }
        self.skins_ball = {
            "ball1": QImage("images/ball1.png"),
            "ball2": QImage("images/ball2.png"),
            "ball3": QImage("images/ball3.png"),
        }
        self.skins_rackets = {
            "left_racket1": QImage("images/left_racket1.png"),
            "left_racket2": QImage("images/left_racket2.png"),
            "left_racket3": QImage("images/left_racket3.png"),
            "right_racket1": QImage("images/right_racket1.png"),
            "right_racket2": QImage("images/right_racket2.png"),
            "right_racket3": QImage("images/right_racket3.png"),
        }

        # Создаем элементы управления
        self.label_score = QLabel("0:0", self)
        self.button_left_up = QPushButton("^", self)
        self.button_left_down = QPushButton("v", self)
        self.button_right_up = QPushButton("^", self)
        self.button_right_down = QPushButton("v", self)

        # Располагаем элементы управления
        self.label_score.move(20, 20)
        self.button_left_up.move(20, 100)
        self.button_left_down.move(20, 200)
        self.button_right_up.move(540, 100)
        self.button_right_down.move(540, 200)

        # Назначаем обработчики событий
        self.button_left_up.clicked.connect(self.on_button_left_up_clicked)
        self.button_left_down.clicked.connect(self.on_button_left_down_clicked)
        self.button_right_up.clicked.connect(self.on_button_right_up_clicked)
        self.button_right_down.clicked.connect(self.on_button_right_down_clicked)

        # Создаем объекты для игры
        self.ball = Ball()
        self.left_racket = Racket(self.skins_rackets["left_racket1"])
        self.right_racket = Racket(self.skins_rackets["right_racket1"])

        # Создаем меню
        self.menu_bar = QMenuBar(self)
        self.menu_game = QMenu("Игра", self.menu_bar)
        self.menu_skins = QMenu("Скины", self.menu_bar)
        self.menu_exit = QMenu("Выход", self.menu_bar)

        # Добавляем пункты в меню
        self.menu_game.addAction(QAction("Играть", self, triggered=self.on_action_play_triggered))
        self.menu_skins.addAction(QAction("Доска", self, triggered=self.on_action_skins_board_triggered))
        self.menu_skins.addAction(QAction("Мяч", self, triggered=self.on_action_skins_ball_triggered))
        self.menu_skins.addAction(QAction("Ракетки", self, triggered=self.on_action_skins_rackets_triggered))
        self.menu_exit.addAction(QAction("Выйти", self, triggered=self.on_action_exit_triggered))

        # Добавляем меню в окно
        self.menu_bar.addMenu(self.menu_game)
        self.menu_bar.addMenu(self.menu_skins)
        self.menu_bar.addMenu(self.menu_exit)

        # Запускаем основной цикл игры
        self.mainloop()

    def on_button_left_up_clicked(self):
        # Если нажата клавиша w
        if self.key_pressed(Qt.Key_W):
            self.left_racket.move(self.left_racket.x(), self.left_racket.y() - 5)

    def on_button_left_down_clicked(self):
        # Если нажата клавиша s
        if self.key_pressed(Qt.Key_S):
            self.left_racket.move(self.left_racket.x(), self.left_racket.y() + 5)

    def on_button_right_up_clicked(self):
        # Если нажата клавиша вверх
        if self.key_pressed(Qt.Key_Up):
            self.right_racket.move(self.right_racket.x(), self.right_racket.y() - 5)

    def on_button_right_down_clicked(self):
        # Если нажата клавиша вниз
        if self.key_pressed(Qt.Key_Down):
            self.right_racket.move(self.right_racket.x(), self.right_racket.y() + 5)

    def on_action_play_triggered(self):
        # Запускаем игру
        self.game_on = True
        self.score_left = 0
        self.score_right = 0
        self.ball.reset()

    def on_action_skins_board_triggered(self):
        # Отображаем диалог выбора скинов для доски
        self.skins_dialog_board = SkinsDialog(self)
        self.skins_dialog_board.show()

    def on_action_skins_ball_triggered(self):
        # Отображаем диалог выбора скинов для мяча
        self.skins_dialog_ball = SkinsDialog(self)
        self.skins_dialog_ball.show()

    def on_action_skins_rackets_triggered(self):
        # Отображаем диалог выбора скинов для ракеток
        self.skins_dialog_rackets = SkinsDialog(self)
        self.skins_dialog_rackets.show()

    def on_action_exit_triggered(self):
        # Завершаем приложение
        sys.exit()

    def paintEvent(self, event):
        # Рисуем доску
        painter = QPainter(self)
        painter.drawImage(0, 0, self.skins_board[self.skin_board])

        # Рисуем мяч
        painter.drawImage(self.ball.x, self.ball.y, self.skins_ball[self.skin_ball])

        # Рисуем ракетки
        painter.drawImage(self.left_racket.x, self.left_racket.y, self.skins_rackets["left_racket" + self.skin_left_racket])
        painter.drawImage(self.right_racket.x, self.right_racket.y, self.skins_rackets["right_racket" + self.skin_right_racket])

    def update_game(self):
        # Проверяем, не пересек ли мяч сетку
        if self.ball.x <= 0:
            # Мяч перелетел на левую сторону
            self.score_right += 1
            self.ball.reset()
        elif self.ball.x >= 600:
            # Мяч перелетел на правую сторону
            self.score_left += 1
            self.ball.reset()

        # Проверяем, не коснулся ли мяч ракетки
        if self.ball.x >= self.left_racket.x - self.ball.width / 2 and self.ball.x <= self.left_racket.x + self.ball.width / 2 and self.ball.y >= self.left_racket.y - self.ball.height / 2 and self.ball.y <= self.left_racket.y + self.ball.height / 2:
            # Мяч коснулся левой ракетки
            self.ball.direction_x = -self.ball.direction_x

        elif self.ball.x >= self.right_racket.x - self.ball.width / 2 and self.ball.x <= self.right_racket.x + self.ball.width / 2 and self.ball.y >= self.right_racket.y - self.ball.height / 2 and self.ball.y <= self.right_racket.y + self.ball.height / 2:
            # Мяч коснулся правой ракетки
            self.ball.direction_x = -self.ball.direction_x

        # Обновляем положение мяча
        self.ball.x += self.ball.direction_x
        self.ball.y += self.ball.direction_y

        # Проверяем, не вышел ли мяч за пределы поля
        if self.ball.y <= 0 or self.ball.y >= 300:
            # Мяч вышел за пределы поля
            self.game_on = False

        # Обновляем счет
        self.label_score.setText(str(self.score_left) + ":" + str(self.score_right))

    def mainloop(self):
        # Запускаем основной цикл игры
        while True:
            # Обновляем состояние игры
            self.update_game()

            # Рисуем элементы игры
            self.update()

            # Ждем следующего события
            self.processEvents()


class Ball(object):

    def __init__(self):
        self.x = 300
        self.y = 150
        self.width = 20
        self.height = 20
        self.direction_x = 5
        self.direction_y = 5

    def reset(self):
        self.x = 300
        self.y = 150
        self.direction_x = 5
        self.direction_y = 5


class Racket(object):

    def __init__(self, image):
        self.x = 300
        self.y = 100
        self.width = 200
        self.height = 20
        self.image = image

    def move(self, x, y):
        self.x = x
        self.y = y


class SkinsDialog(QDialog):

    def __init__(self, parent):
        super().init(parent)
        self.setWindowTitle("Выберите скин")
        self.setFixedSize(250, 200)

        # Создаем элементы управления
        self.label_title = QLabel("Выберите скин", self)
        self.combo_box = QComboBox(self)
        self.button_ok = QPushButton("ОК", self)
        self.button_cancel = QPushButton("Отмена", self)

        # Заполняем список скинов
        self.combo_box.addItems(list(parent.skins.keys()))

        # Располагаем элементы управления
        self.label_title.move(20, 20)
        self.combo_box.move(20, 50)
        self.button_ok.move(150, 100)
        self.button_cancel.move(100, 100)

        # Назначаем обработчики событий
        self.button_ok.clicked.connect(self.on_button_ok_clicked)
        self.button_cancel.clicked.connect(self.on_button_cancel_clicked)

    def on_button_ok_clicked(self):
        # Получаем выбранный скин
        skin = self.combo_box.currentText()

        # Устанавливаем выбранный скин
        if skin == "Доска":
            self.parent().skin_board = skin
        elif skin == "Мяч":
            self.parent().skin_ball = skin
        elif skin == "Ракетка":
            self.parent().skin_left_racket = skin[6:]
            self.parent().skin_right_racket = skin[6:]

        # Закрываем диалог
        self.close()

    def on_button_cancel_clicked(self):
        # Закрываем диалог
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()