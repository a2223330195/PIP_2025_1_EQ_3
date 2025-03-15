import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P13_RadioButton_Ejemplo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rb1.clicked.connect(self.jotaro)
        self.rb2.clicked.connect(self.andrew)
        self.rb3.clicked.connect(self.dante)
        self.rb4.clicked.connect(self.azul)
    def jotaro(self):
        valor = self.rb1.isChecked()
        print("Jotaro", valor)
    def andrew(self):
        valor = self.rb2.isChecked()
        print("andrew", valor)
    def dante(self):
        valor = self.rb3.isChecked()
        print("dante", valor)
    def azul(self):
        valor = self.rb4.isChecked()
        print("azul", valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())