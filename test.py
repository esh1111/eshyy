import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTabWidget, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class PingPongGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Создаем главное окно и устанавливаем его размер
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Ping Pong Game")

        # Создаем виджет и устанавливаем его как центральный виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем вкладки
        tab_widget = QTabWidget()
        tab_widget.addTab(self.createSkinTab(), "Скины")

        # Создаем кнопки для начального меню
        play_button = QPushButton("Играть", self)
        play_button.clicked.connect(self.startGame)

        exit_button = QPushButton("Выход", self)
        exit_button.clicked.connect(self.close)

        # Создаем главный макет
        layout = QVBoxLayout()
        layout.addWidget(play_button)
        layout.addWidget(tab_widget)
        layout.addWidget(exit_button)

        central_widget.setLayout(layout)

    def createSkinTab(self):
        skin_tab = QWidget()

        ball_label = QLabel("Выберите скин для мяча:")
        ball_skin_combobox = QComboBox()
        ball_skin_combobox.addItem("skin1.jpg")
        ball_skin_combobox.addItem("skin2.png")

        paddle_label = QLabel("Выберите скин для доски:")
        paddle_skin_combobox = QComboBox()
        paddle_skin_combobox.addItem("paddle1.jpg")
        paddle_skin_combobox.addItem("paddle2.png")

        racket_label = QLabel("Выберите скин для ракетки:")
        racket_skin_combobox = QComboBox()
        racket_skin_combobox.addItem("racket1.jpg")
        racket_skin_combobox.addItem("racket2.png")

        layout = QVBoxLayout()
        layout.addWidget(ball_label)
        layout.addWidget(ball_skin_combobox)
        layout.addWidget(paddle_label)
        layout.addWidget(paddle_skin_combobox)
        layout.addWidget(racket_label)
        layout.addWidget(racket_skin_combobox)

        skin_tab.setLayout(layout)
        return skin_tab

    def startGame(self):
        # Здесь вы можете добавить код для начала игры с выбранными скинами
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PingPongGame()
    game.show()
    sys.exit(app.exec_())
