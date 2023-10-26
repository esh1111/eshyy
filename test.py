import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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

# Класс для окна со скинами
class SkinWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Скин")
        self.setGeometry(300, 300, 600, 400)

        # Создание вкладок
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(100, 100, 400, 200)
        self.tab_мяч = QWidget()
        self.tab_доска = QWidget()
        self.tab_левая_ракетка = QWidget()
        self.tab_правая_ракетка = QWidget()
        self.tabWidget.addTab(self.tab_мяч, "Мяч")
        self.tabWidget.addTab(self.tab_доска, "Доска")
        self.tabWidget.addTab(self.tab_левая_ракетка, "Левая ракетка")
        self.tabWidget.addTab(self.tab_правая_ракетка, "Правая ракетка")

         # Создание кнопок для выбора скина
        self.button_мяч = QPushButton("Выбрать", self.tab_мяч)
        self.button_доска = QPushButton("Выбрать", self.tab_доска)
        self.button_левая_ракетка = QPushButton("Выбрать", self.tab_левая_ракетка)
        self.button_правая_ракетка = QPushButton("Выбрать", self.tab_правая_ракетка)
        self.button_мяч.setGeometry(100, 50, 100, 50)
        self.button_доска.setGeometry(100, 50, 100, 50)
        self.button_левая_ракетка.setGeometry(100, 50, 100, 50)
        self.button_правая_ракетка.setGeometry(200, 50, 100, 50)

        # Связывание событий с кнопками
        self.button_мяч.clicked.connect(self.on_button_мяч_clicked)
        self.button_доска.clicked.connect(self.on_button_доска_clicked)
        self.button_левая_ракетка.clicked.connect(self.on_button_левая_ракетка_clicked)
        self.button_правая_ракетка.clicked.connect(self.on_button_правая_ракетка_clicked)

        # Отображение окна
        self.show()

        # Обработка события нажатия на кнопку "Выбрать" для мяча
        def on_button_мяч_clicked(self):
    # Открытие диалогового окна для выбора файла
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Изображения (*.jpg *.png)")
            if file_dialog.exec():
        # Загрузка файла
                file_path = file_dialog.selectedFiles()[0]
        # Установка изображения мяча
                self.image_ball.setPixmap(QPixmap(file_path))

# Обработка события нажатия на кнопку "Выбрать" для доски
        def on_button_доска_clicked(self):
    # Открытие диалогового окна для выбора файла
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Изображения (*.jpg *.png)")
            if file_dialog.exec():
        # Загрузка файла
                file_path = file_dialog.selectedFiles()[0]
        # Установка изображения доски
                self.image_table.setPixmap(QPixmap(file_path))

# Обработка события нажатия на кнопку "Выбрать" для левой ракетки
        def on_button_левая_ракетка_clicked(self):
    # Открытие диалогового окна для выбора файла
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Изображения (*.jpg *.png)")
            if file_dialog.exec():
        # Загрузка файла
                file_path = file_dialog.selectedFiles()[0]
        # Установка изображения левой ракетки
                self.image_left_racket.setPixmap(QPixmap(file_path))

# Обработка события нажатия на кнопку "Выбрать" для правой ракетки
        def on_button_правая_ракетка_clicked(self):
    # Открытие диалогового окна для выбора файла
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Изображения (*.jpg *.png)")
            if file_dialog.exec():
        # Загрузка файла
                file_path = file_dialog.selectedFiles()[0]
        # Установка изображения правой ракетки
                self.image_right_racket.setPixmap(QPixmap(file_path))