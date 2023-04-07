import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

enter_value = ''

def window():
    # Create an application object of QApplication class 
    app = QApplication(sys.argv)
    win = QWidget()


    # ---------- BUTTON 1 ----------- # 
    # A QWidget object creates top level window add QLabel object 
    b1 = QPushButton(win)
    b1.setText("1")
    b1.move(50, 20)
    b1.clicked.connect(b1_clicked)

    # ---------- BUTTON 2 ----------- #
    b2 = QPushButton(win)
    b2.setText("2")
    b2.move(50, 60)
    b2.clicked.connect(b2_clicked)

    # ---------- BUTTON + ----------- #
    b3 = QPushButton(win)
    b3.setText("+")
    b3.move(170, 20)
    b3.clicked.connect(b3_clicked)

    win.setGeometry(200, 200, 300, 100)
    win.setWindowTitle("PyQt5 Window")
    win.show()





    # Enter the mainloop of application by app.exec_() method.
    sys.exit(app.exec_())

def b1_clicked():
    enter_value += '1'
    print(enter_value)
    
def b2_clicked():
    print("Button 2 clicked")
def b3_clicked():
    pass



if __name__ == '__main__':
    window()

