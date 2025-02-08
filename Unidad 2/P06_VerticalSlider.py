import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P06_VerticalSlider.ui" #Nombre del archivo aqui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.cambiaValor)
        self.verticalSlider.setMinimum(-10)
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setSingleStep(2)
        self.verticalSlider.setValue(0)
        #Area de los Signals
#Area de los Slots
    def cambiaValor(self):
        valor = str(self.verticalSlider.value())
        self.lineEdit.setText(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

