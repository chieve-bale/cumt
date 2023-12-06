import sys
from Home import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Zhuye(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Zhuye, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.actionNew.triggered.connect(self.new_file)
    def new_file(self):
        with open('set_up',mode='w',encoding='utf-8') as f:
            f.write('hello world')

def main():
    zhuye=Zhuye(QMainWindow,Ui_MainWindow)


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui= Zhuye()
    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
