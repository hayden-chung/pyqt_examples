import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

enter_value = ''

def window():
    # Create an application object of QApplication class 
    app = QApplication(sys.argv)
    win = QWidget()

    button1 = QPushButton("Button1")
    # button1.clicked.connect(button1_clicked)

    vbox = QVBoxLayout()
    vbox.addWidget(button1)

    # vbox.addStretch()
    # vbox.addWidget(button2)

    

    win.setLayout(vbox)
    win.setWindowTitle("PyQt")
    win.show()

    # Enter the mainloop of application by app.exec_() method.
    sys.exit(app.exec_())

def button1_clicked():
    print("Button 1 clicked")
    
def button2_clicked():
    print("Button 2 clicked")




if __name__ == '__main__':
    window()

