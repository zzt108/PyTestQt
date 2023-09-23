import sys

from PyQt6 import QtGui
from PyQt6.QtGui import QMovie, QScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MainWindow3(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLabel Widget')
        # self.setGeometry(100, 100, 320, 210)

        label = QLabel()
        movie = QMovie('python.gif')
        label.setMovie(movie)
        movie.start()

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow2(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        # self.setGeometry(0, 0, 320, 210)

        label = QLabel()
        pixmap = QPixmap('python-logo.png')
        label.setPixmap(pixmap)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow1(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        # self.setGeometry(0, 0, 320, 210)

        # create a QLabel widget
        label = QLabel('This is a QLabel widget')

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow2()
    window.center()
    window.show()
    # start the event loop
    sys.exit(app.exec())
