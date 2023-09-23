import sys

from PyQt6.QtGui import QMovie
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout

from QTTutorial.BaseWindow import BaseWindow


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
        self.label = QLabel('This is a QLabel widget')

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow1()
    window.center()
    window.show()
    # start the event loop
    sys.exit(app.exec())
