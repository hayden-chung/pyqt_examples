import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    # Create an application object of QApplication class 
    app = QApplication(sys.argv)

    # A QWidget object creates top level window add QLabel object 
    w = QWidget()
    b = QPushButton(w)
    b.setText("Hello World!")
    b.move(50, 20)

    w.setGeometry(100, 100, 300, 100)
    w.setWindowTitle("PyQt5 Window")
    w.show()
    # Enter the mainloop of application by app.exec_() method.
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()