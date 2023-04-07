import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

buttondict = {}

def window(button_column):
    app = QApplication(sys.argv)
    win = QWidget()

    for i in range(1, button_column+1):
        buttondict["button{0}".format(i)] = QPushButton(f'Button {i}')

    hbox = QHBoxLayout()
    for i in range(len(buttondict)):
        hbox.addWidget(buttondict[f'button{i+1}'])

    

    win.setLayout(hbox)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())

def button1_clicked():
    print("1 clicked")

def button2_clicked():
    print("2 clicked")

if __name__ == '__main__':
    window(15)