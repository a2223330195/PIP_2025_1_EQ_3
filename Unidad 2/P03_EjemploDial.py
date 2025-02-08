import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P03_EjemploDial.ui" #Nombre del archivo aqui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(2)
        self.dial.setValue(0)
        #Area de los Signals
#Area de los Slots
    def cambiaValor(self):
        valor = str(self.dial.value())
        self.lineEdit.setText(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

