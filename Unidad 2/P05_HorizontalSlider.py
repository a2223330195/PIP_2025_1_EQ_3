import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_HorizontalSlider.ui" #Nombre del archivo aqui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.horizontalSlider.setMinimum(-10)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(2)
        self.horizontalSlider.setValue(0)
        #Area de los Signals
#Area de los Slots
    def cambiaValor(self):
        valor = str(self.horizontalSlider.value())
        self.lineEdit.setText(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

