import pytest
from PyQt5 import QtCore

from PyQt5.QtWidgets import QLabel

import example_app


@pytest.fixture
def label(qtbot):
    qlabel = QLabel()
    qlabel.setText("Hello World")
    qtbot.addWidget(qlabel)
    return qlabel


@pytest.fixture
def app(qtbot):
    test_hello_app = example_app.MyApp()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label0(label):
    assert label.text() == "Hello World"


def test_label(app):
    assert app.text_label.text() == "Hello World!"


def test_label_after_click(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Changed!"
