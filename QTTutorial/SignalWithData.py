import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        # create widgets
        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        # show the window
        # self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

'''
When you type something on the QLineEdit:

The textChanged signal sends the text
The QLabel receives the text and passes it to the setText() method.
Summary
A signal is a special property of an object that is emitted when an event occurs.
A slot is a callable that can receive a signal and respond to it accordingly.
PyQt uses signals and slots to wire up events with callables.
'''    