import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "p14.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rb1.clicked.connect(self.personaje)
        self.rb2.clicked.connect(self.personaje)
        self.rb3.clicked.connect(self.personaje)
        self.rb4.clicked.connect(self.color)
        self.rb5.clicked.connect(self.color)
        self.rb6.clicked.connect(self.color)
    def personaje(self):
        obj=self.sender()
        valor=obj.isChecked()
        if valor:
            print("Obj",obj.text(),":",valor)
    def color(self):
        obj = self.sender()
        valor = obj.isChecked()
        if valor:
            print("Obj", obj.text(), ":", valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())