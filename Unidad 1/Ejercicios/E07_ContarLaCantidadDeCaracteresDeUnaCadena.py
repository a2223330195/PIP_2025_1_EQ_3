import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E07_ContarLaCantidadDeCaracteresDeUnaCadena.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_contar.clicked.connect(self.contar_caracteres)

    def contar_caracteres(self):
        cadena = self.txt_cadena.text()
        cantidad = len(cadena)
        self.txt_resultado.setText(str(cantidad))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
