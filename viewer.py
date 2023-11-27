import sys
from bianjiqi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Zhuye(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Zhuye, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)



if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui= Zhuye()
    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())