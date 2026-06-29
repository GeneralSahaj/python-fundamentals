# PyQt5 Introduction and GUI Creation

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(500, 525, 700, 500)
        self.setWindowIcon(QIcon("profile.jpeg"))

        label = QLabel("Wassup", self)
        label.setFont(QFont("Consolas", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #0be646;"
                            "background-color: #040505;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        # label.setAlignment(Qt.AlignTop)   Vertically TOP
        # label.setAlignment(Qt.AlignBottom)  Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter)  Vertically Center

        # label.setAlignment(Qt.AlignRight)  Horizontally Right
        # label.setAlignment(Qt.AlignLeft)   Horizontally Left
        # label.setAlignment(Qt.AlignHCenter) Horizontally Center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  Center and Center

        label.setAlignment(Qt.AlignCenter)  # Center and Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()