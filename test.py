import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenuBar, QMenu, QAction, QTabWidget, QFileDialog, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer

# Класс для начальной игры
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Пинг-понг")
        self.setGeometry(300, 300, 600, 400)

        # Создание меню
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
        menu = QMenu("Файл", self)
        menubar.addMenu(menu)
        action_играть = QAction("Играть", self)
        action_скины = QAction("Скин", self)
        action_выход = QAction("Выход", self)
        menu.addAction(action_играть)
        menu.addAction(action_скины)
        menu.addAction(action_выход)

        # Создание кнопок
        button_играть = QPushButton("Играть", self)
        button_скины = QPushButton("Скин", self)
        button_выход = QPushButton("Выход", self)
        button_играть.setGeometry(200, 200, 100, 50)
        button_скины.setGeometry(300, 200, 100, 50)
        button_выход.setGeometry(400, 200, 100, 50)

        # Связывание событий с кнопками
        button_играть.clicked.connect(self.on_button_играть_clicked)
        button_скины.clicked.connect(self.on_button_скины_clicked)
        button_выход.clicked.connect(self.on_button_выход_clicked)

        # Отображение окна
        self.show()

    # Обработка события нажатия на кнопку "Играть"
    def on_button_играть_clicked(self):
        # Переход на игровое окно
        self.game = GameWindow()
        self.game.show()

    # Обработка события нажатия на кнопку "Скин"
    def on_button_скины_clicked(self):
        # Открытие окна со скинами
        self.skin_window = SkinWindow()
        self.skin_window.show()

    # Обработка события нажатия на кнопку "Выход"
    def on_button_выход_clicked(self):
        # Закрытие приложения
        sys.exit()

class GameWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Пинг-понг")
        self.setGeometry(300, 300, 600, 400)

        # Создание объектов
        self.ball = QLabel(self)
        self.table = QLabel(self)
        self.left_racket = QLabel(self)
        self.right_racket = QLabel(self)

        # Установка изображений
        self.ball.setPixmap(QPixmap("vbyfyft;f.png"))
        self.table.setPixmap(QPixmap("12.png"))
        self.left_racket.setPixmap(QPixmap("XGAAAgGvDeA-1920.png"))
        self.right_racket.setPixmap(QPixmap("нога.png"))

        # Расположение объектов
        self.ball.setGeometry(300, 150)
        self.table.setGeometry(0, 0, 600, 200)
        self.left_racket.setGeometry(20, 170)
        self.right_racket.setGeometry(580, 170)

        # Создание таймера
        self.timer = QTimer(self)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update)

         # Запуск таймера
        self.timer.start()

        self.button_сохранить = QPushButton("Сохранить", self)
        self.button_сохранить.setGeometry(10, 10, 100, 20)
        self.button_сохранить.clicked.connect(self.on_button_сохранить_clicked)

        # Отображение окна
        self.show()

    def on_button_сохранить_clicked(self):
        # Сохранение скинов
        filename = QFileDialog.getSaveFileName(self, "Сохранить скины", "", "Скин (*.txt)")
        if filename[0]:
            with open(filename[0], "y") as file:
                for skin in self.skins:
                    file.write(f"{skin['name']}={skin['image']}\n")

    def on_button_загрузить_clicked(self):
        # Загрузка скинов
                filename = QFileDialog.getOpenFileName(self, "Загрузить скины", "", "Скин (*.txt)")
                if filename[0]:
                        with open(filename[0], "r") as file:
                                for line in file:
                                        name, path = line.split("=")
                                        self.skins.append({"name": name, "image": path})    

    def update(self):
        # Перемещение мяча
        self.ball.move(self.ball.x() + self.ball_x_speed, self.ball.y() + self.ball_y_speed)

        # Проверка столкновений
        if self.ball.x() < 0 or self.ball.x() > 600:
            self.ball_x_speed = -self.ball_x_speed
        elif self.ball.y() < 0 or self.ball.y() > 200:
            self.ball_y_speed = -self.ball_y_speed
        elif self.ball.y() + 50 >= self.left_racket.y() and self.ball.x() >= self.left_racket.x() and self.ball.x() <= self.left_racket.x() + 20:
            self.ball_x_speed = -self.ball_x_speed
        elif self.ball.y() + 50 >= self.right_racket.y() and self.ball.x() >= self.right_racket.x() - 20 and self.ball.x() <= self.right_racket.x():
            self.ball_x_speed = -self.ball_x_speed

    def get_skin(self, skin_name):
        # Получение пути к файлу с скин
        skin_path = f"skins/{skin_name}.png"

        # Если файл не существует, то вернуть пустой QPixmap
        if not os.path.exists(skin_path):
            return QPixmap()

        # Возврат QPixmap с скин
        return QPixmap(skin_path)

class SkinWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Скин")
        self.setGeometry(300, 300, 600, 400)

        # Создание вкладок
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(100, 100, 400, 200)
        self.tab_ball = QWidget()
        self.tab_table = QWidget()
        self.tab_left_racket = QWidget()
        self.tab_right_racket = QWidget()
        self.tab_widget.addTab(self.tab_ball, "Мяч")
        self.tab_widget.addTab(self.tab_table, "Доска")
        self.tab_widget.addTab(self.tab_left_racket, "Левая ракетка")
        self.tab_widget.addTab(self.tab_right_racket, "Правая ракетка")

        # Создание кнопок для выбора скина
        self.button_ball = QPushButton("Выбрать", self.tab_ball)
        self.button_table = QPushButton("Выбрать", self.tab_table)
        self.button_left_racket = QPushButton("Выбрать", self.tab_left_racket)
        self.button_right_racket = QPushButton("Выбрать", self.tab_right_racket)
        self.button_ball.setGeometry(100, 50, 100, 50)
        self.button_table.setGeometry(100, 50, 100, 50)
        self.button_left_racket.setGeometry(100, 50, 100, 50)
        self.button_right_racket.setGeometry(200, 50, 100, 50)

        # Связывание событий с кнопками
        self.button_ball.clicked.connect(self.on_button_ball_clicked)
        self.button_table.clicked.connect(self.on_button_table_clicked)
        self.button_left_racket.clicked.connect(self.button_left_racket_clicked)
        self.button_right_racket.clicked.connect(self.on_button_right_racket_clicked)

        # Отображение окна
        self.show()

         # Обработка события нажатия на кнопку "Выбрать" для мяча
    # Список скинов
        self.skins = [
        {
                "name": "Мяч",
                "image": "vbyfyft;f.png",
        },
        {
                "name": "Доска",
                "image": "12.png",
        },
        {
                "name": "Левая ракетка",
                "image": "XGAAAgGvDeA-1920.png",
        },
        {
                "name": "Правая ракетка",
                "image":[ "нога.png",
                          ""]
        },
        ]
        # Загрузка скинов
        self.on_button_загрузить_clicked()

        print(self.skins)

        # Спины для выбора скинов
        self.skin_selector_ball = QComboBox(self)
        self.skin_selector_ball.addItems([skin["name"] for skin in self.skins])
        self.skin_selector_ball.setGeometry(10, 10, 100, 20)

        self.skin_selector_table = QComboBox(self)
        self.skin_selector_table.addItems([skin["name"] for skin in self.skins])
        self.skin_selector_table.setGeometry(10, 10, 100, 20)

        self.skin_selector_left_racket = QComboBox(self)
        self.skin_selector_left_racket.addItems([skin["name"] for skin in self.skins])
        self.skin_selector_left_racket.setGeometry(10, 10, 100, 20)

        self.skin_selector_right_racket = QComboBox(self)
        self.skin_selector_right_racket.addItems([skin["name"] for skin in self.skins])
        self.skin_selector_right_racket.setGeometry(10, 10, 100, 20)

        # Обработка события изменения выбранного скина
        def on_skin_selector_changed(self):
        # Получить выбранный скин
                name = self.skin_selector.currentText()

        # Получить путь к выбранному скину
        for skin in self.skins:
                if skin["name"] == __name__:
                        path = skin["image"]
                        break

        # Установить путь к скину в игровом окне
        self.game.skin_path = path

        # Обновить изображение в игровом окне
        self.game.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создание окна со скинами
    skin_window = SkinWindow()

    # Запуск приложения
    sys.exit(app.exec())

