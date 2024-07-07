from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Subclass QMainWindow to easily customise app's main window.
# This is kind of like the "properties" of the main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.btn = QPushButton("Press-able Apparatus")
        # self.btn.setCheckable(True)

        # # == Connects to funcs that receives data == #
        # btn.clicked.connect(self.the_btn_was_clicked)
        # btn.clicked.connect(self.the_btn_was_tggled)

        # # This variable stores the check status of btn.
        # self.btn_is_checked = True

        self.btn.clicked.connect(self.the_btn_was_clicked)
        # self.btn.setChecked(self.btn_is_checked)

        self.setCentralWidget(self.btn)

    # # == Receives check state data == #
    # def the_btn_was_clicked(self):
    #     print("Clicked")

    # def the_btn_was_tggled(self, checked):
    #     print("Checked?", checked)

    # # == Receives check state data & modifies variable == #
    # # Does the same thing as abv but I guess it's 
    # # considered storing now since it's printing 
    # # a variable.
    # def the_btn_was_tggled(self, checked):
    #     self.btn_is_checked = checked

    #     print(self.btn_is_checked)

    # == Receives check state & modifies interface == #
    def the_btn_was_clicked(self):
        self.btn.setText("Apparatus has been modified permanantly.")
        self.btn.setEnabled(False)

        self.setWindowTitle("Our App: Communism Edition")

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