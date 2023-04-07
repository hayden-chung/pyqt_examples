import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

enter_value = ''

def window():
    # Create an application object of QApplication class 
    app = QApplication(sys.argv)
    win = QWidget()


    vbox1 = QVBoxLayout()
    button1 = QPushButton("Button1")
    button2 = QPushButton("Button2")
    button3 = QPushButton("Button3")
    button4 = QPushButton("Button4")
    vbox1.addWidget(button1)
    vbox1.addStretch()
    vbox1.addWidget(button2)
    vbox1.addStretch()
    vbox1.addWidget(button3)
    vbox1.addStretch()
    vbox1.addWidget(button4)

    vbox2 = QVBoxLayout()
    button5 = QPushButton("Button5")
    button6 = QPushButton("Button6")
    button7 = QPushButton("Button7")
    button8 = QPushButton("Button8")
    vbox2.addWidget(button5)
    vbox2.addStretch()
    vbox2.addWidget(button6)
    vbox2.addStretch()
    vbox2.addWidget(button7)
    vbox2.addStretch()
    vbox2.addWidget(button8)
    
    hbox = QHBoxLayout()
    hbox.addLayout(vbox1)
    hbox.addLayout(vbox2)


    

    win.setLayout(hbox)
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

