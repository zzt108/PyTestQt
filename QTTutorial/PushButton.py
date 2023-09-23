import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from QTTutorial.BaseWindow import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QPushButton Widget')
        # self.setGeometry(100, 100, 320, 210)

        self.button = QPushButton('Toggle Me')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_toggle)

        # place the button on the window
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        # show the window
        # self.show()

    def on_toggle(self, checked):
        self.button.setText(str(checked))
        print(checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()
    window.center()
    window.show()
    # start the event loop
    sys.exit(app.exec())
