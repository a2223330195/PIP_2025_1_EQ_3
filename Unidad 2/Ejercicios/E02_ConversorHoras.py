import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_ConversorHoras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dialTiempo.valueChanged.connect(self.convertirhoras)
        self.dialTiempo.setMinimum(0)
        self.dialTiempo.setMaximum(23)
        self.dialTiempo.setSingleStep(1)
        self.dialTiempo.setValue(0)
        self.resultado.setReadOnly(True)
        self.Horas.setReadOnly(True)
    def convertirhoras(self):
        horas = self.dialTiempo.value()
        segundos = horas * 3600
        self.resultado.setText(str(segundos))
        self.Horas.setText(str(horas))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())