from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,\
      QLabel, QLineEdit, QVBoxLayout, QWidget
import sys
from random import choice



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        # Line below connects the input box to the text line
        # everytime something changes in the input box, the
        # label reflects it
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Sets the central widget
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()