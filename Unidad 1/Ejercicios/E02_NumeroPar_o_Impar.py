import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_NumeroPar_o_Impar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(lambda: self.paroimpar())
    def paroimpar(self):
        numero = float(self.recibidor.text())
        if numero % 2 == 0:
            m = QtWidgets.QMessageBox()
            m.setText("El numero es par")
            m.exec_()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("El numero es impar")
            m.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
