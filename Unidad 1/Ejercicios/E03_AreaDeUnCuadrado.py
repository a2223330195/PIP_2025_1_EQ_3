import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E03_AreaDeUnCuadrado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(lambda: self.areac())
    def areac(self):
        lado=float(self.recibidor.text())
        area=lado*lado
        m=QtWidgets.QMessageBox()
        m.setText("El area es :"+str(area))
        m.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
