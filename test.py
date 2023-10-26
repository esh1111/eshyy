import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class PingPongGame(QMainWindow):
    def __init(self):
        super().__init()

        self.initUI()

    def initUI(self):
        # Создаем кнопки на главном окне
        play_button = QPushButton('Играть', self)
        play_button.clicked.connect(self.start_game)

        skins_button = QPushButton('Скины', self)
        skins_button.clicked.connect(self.show_skins)

        exit_button = QPushButton('Выход', self)
        exit_button.clicked.connect(self.close)

        # Создаем вкладки для скинов
        skin_tabs = QTabWidget(self)
        ball_tab = QWidget()
        paddle_tab = QWidget()
        left_paddle_tab = QWidget()
        right_paddle_tab = QWidget()

        skin_tabs.addTab(ball_tab, 'Мяч')
        skin_tabs.addTab(paddle_tab, 'Доска')
        paddle_tab.addTab(left_paddle_tab, 'Левая ракетка')
        paddle_tab.addTab(right_paddle_tab, 'Правая ракетка')

        # Создаем метки для отображения скинов
        self.ball_skin_label = QLabel(ball_tab)
        self.paddle_skin_label = QLabel(paddle_tab)
        self.left_paddle_skin_label = QLabel(left_paddle_tab)
        self.right_paddle_skin_label = QLabel(right_paddle_tab)

        # Создаем кнопки для выбора скинов
        ball_skin_button = QPushButton('Выбрать скин для мяча', ball_tab)
        ball_skin_button.clicked.connect(self.choose_ball_skin)

        paddle_skin_button = QPushButton('Выбрать скин для доски', paddle_tab)
        paddle_skin_button.clicked.connect(self.choose_paddle_skin)

        left_paddle_skin_button = QPushButton('Выбрать скин для левой ракетки', left_paddle_tab)
        left_paddle_skin_button.clicked.connect(self.choose_left_paddle_skin)

        right_paddle_skin_button = QPushButton('Выбрать скин для правой ракетки', right_paddle_tab)
        right_paddle_skin_button.clicked.connect(self.choose_right_paddle_skin)

        # Размещаем элементы на главном окне
        layout = QVBoxLayout()
        layout.addWidget(play_button)
        layout.addWidget(skins_button)
        layout.addWidget(exit_button)
        layout.addWidget(skin_tabs)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Игра пинг-понг')
        self.show()

    def start_game(self):
        # Ваш код для запуска игры
        pass

    def show_skins(self):
        # Ваш код для отображения скинов
        pass

    def choose_ball_skin(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите скин для мяча", "", "PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        
        if file_name:
            pixmap = QPixmap(file_name)
            self.ball_skin_label.setPixmap(pixmap)

    def choose_paddle_skin(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите скин для доски", "", "PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        
        if file_name:
            pixmap = QPixmap(file_name)
            self.paddle_skin_label.setPixmap(pixmap)

    def choose_left_paddle_skin(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите скин для левой ракетки", "", "PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        
        if file_name:
            pixmap = QPixmap(file_name)
            self.left_paddle_skin_label.setPixmap(pixmap)

    def choose_right_paddle_skin(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите скин для правой ракетки", "", "PNG Files (*.png);;JPEG Files (*.jpg)", options=options)
        
        if file_name:
            pixmap = QPixmap(file_name)
            self.right_paddle_skin_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PingPongGame()
    sys.exit(app.exec_())
