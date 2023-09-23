import pytest
from PyQt6 import QtCore

from PyQt6.QtWidgets import QLabel

import QTTutorial.PushButton


@pytest.fixture
def app(qtbot):
    test_app = QTTutorial.PushButton.MainWindow()
    qtbot.addWidget(test_app)

    return test_app


def test_button_after_click(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.MouseButton.LeftButton)
    assert app.button.isChecked() == True
    qtbot.mouseClick(app.button, QtCore.Qt.MouseButton.LeftButton)
    assert app.button.isChecked() == False
