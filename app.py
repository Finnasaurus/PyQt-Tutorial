from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QSize
import sys

# Subclass QMainWindow to easily customise app's main window.
# This is kind of like the "properties" of the main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        btn = QPushButton("Press-able Apparatus")

        self.setFixedSize(QSize(400, 300))

        # Sets the central widget of the Window
        self.setCentralWidget(btn)

# You need only one QApplication instance per app.
# Sys.argy allows app to use command line arguments.
# If you don't need system commands, QApplication([]) works.
app = QApplication(sys.argv)

# Creates a Qt widget, which is the window.
window = MainWindow()
window.show() # <-- Must be done as windows are hidden by default.

# Starts the loop.
app.exec()

# All top level widgets are windows, they don't have a parent
# and aren't nested within another widget.
# So, any widget can actually be a window, not just "QWidget()" or 
# "QMainWindow()", and the name window is simply there to signify
# that it is the MAIN widget.