from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# You need only one QApplication instance per app.
# Sys.argy allows app to use command line arguments.
# If you don't need system commands, QApplication([]) works.
app = QApplication(sys.argv)

# Creates a Qt widget, which is the window.
window = QMainWindow()
window.show() # <-- Must be done as windows are hidden by default.

# Starts the loop.
app.exec()

# All top level widgets are windows, they don't have a parent
# and aren't nested within another widget.
# So, any widget can actually be a window, not just "QWidget()" or 
# "QMainWindow()", and the name window is simply there to signify
# that it is the MAIN widget.