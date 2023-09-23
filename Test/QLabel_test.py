import pytest

import QTTutorial.QLabel


@pytest.fixture
def app(qtbot):
    test_app = QTTutorial.QLabel.MainWindow1()
    qtbot.addWidget(test_app)

    return test_app


def test_label(app):
    assert app.label.text() == "This is a QLabel widget"
