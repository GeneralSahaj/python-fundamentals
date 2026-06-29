# PyQt5 Introduction and GUI Creation

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(500, 525, 700, 500)
        self.setWindowIcon(QIcon("profile.jpeg"))
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Kudasai", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(250, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(250, 300, 250, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button clicked!")
        self.button.setText("YAMETE!💦")
        self.label.setText("Kudasai!💦")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()