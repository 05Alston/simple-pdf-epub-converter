import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget


class Button(QPushButton):
    entered = pyqtSignal()
    leaved = pyqtSignal()

    def enterEvent(self, event):
        super().enterEvent(event)
        self.entered.emit()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.leaved.emit()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.setWindowTitle("Wassup?")
        self.setFixedSize(1000, 600)
        self.move(100, 50)
        self.setStyleSheet("background-color: rgb(208, 208, 208);")

        button = Button(self)
        button.setGeometry(100, 50, 120, 60)
        button.setStyleSheet(
            "QPushButton {"
            "border: 0px solid;"
            "background-color: rgb(255, 50, 50);"
            "}"
        )

        self.label = QLabel(self)
        self.label.setGeometry(100, 120, 120, 60)
        self.label.setStyleSheet("background-color: rgb(128, 255, 64);")
        self.label.setText("Initial Text")

        button.entered.connect(self.handle_entered)
        button.leaved.connect(self.handle_leaved)

    def handle_entered(self):
        self.label.setText("Wassup yall?")

    def handle_leaved(self):
        self.label.setText("Initial Text")


# app = QApplication(sys.argv)

# window = Widget()
# window.show()

# sys.exit(app.exec())