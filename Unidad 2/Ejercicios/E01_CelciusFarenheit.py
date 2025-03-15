import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E01_CelciusFarenheit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dialCelsius.valueChanged.connect(self.actualizartemp)
        self.dialCelsius.setMinimum(-98)
        self.dialCelsius.setMaximum(56)
        self.dialCelsius.setSingleStep(1)
        self.dialCelsius.setValue(0)
        self.lineEditCelsius.setReadOnly(True)
        self.lineEditFahrenheit.setReadOnly(True)
        self.actualizartemp()
    def actualizartemp(self):
        celsius = self.dialCelsius.value()
        fahrenheit = (celsius * 9 / 5) + 32
        self.lineEditCelsius.setText(str(celsius))
        self.lineEditFahrenheit.setText(str(fahrenheit))
        self.dialFahrenheit.setValue(int(fahrenheit))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())