import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    # method(self) : function of class
    # member : variable of class 

    l1.setText("Hello World")
    l2.setText("welcome to Python GUI Programming")
    l4.setText('<a href="https://www.example.com">Click Me!</a>') 
   
    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)

    l3.setPixmap(QPixmap("python.jpg"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)
    vbox.addStretch()

    win.setLayout(vbox)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
