import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P16_CheckBox_Ejemplo1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cb1.clicked.connect(self.yt)
        self.cb2.clicked.connect(self.yt)
        self.cb3.clicked.connect(self.yt)
        self.cb4.clicked.connect(self.comida)
        self.cb5.clicked.connect(self.comida)
        self.cb6.clicked.connect(self.comida)
    def yt(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Obj",obj.text(),":",valor)
    def comida(self):
        obj = self.sender()
        valor = obj.isChecked()
        if valor:
            print("Obj", obj.text(), ":", valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())