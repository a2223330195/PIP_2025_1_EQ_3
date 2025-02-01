import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E01_DistanciaDeDosPuntos.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(lambda:self.distancia())
    def distancia(self):
        xa = float(self.xa.text())
        xb = float(self.xb.text())
        if xa > xb:
            d = xa - xb
        else:
            d = xb - xa
        m = QtWidgets.QMessageBox()
        m.setText("La distancia es: " + str(d)+ " metros")
        m.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
