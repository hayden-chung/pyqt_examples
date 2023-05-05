from PyQt5.QtCore import QThread 
import time 

class WorkerThread(QThread):
    def run(self):
        for i in range(101):
            print(i) 
            time.sleep(0.1)