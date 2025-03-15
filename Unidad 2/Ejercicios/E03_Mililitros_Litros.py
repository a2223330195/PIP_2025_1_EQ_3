import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E03_Mililitros_Litros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.mililitrosSlider.valueChanged.connect(self.militros_a_litros)
        self.mililitrosSlider.setMinimum(0)
        self.mililitrosSlider.setMaximum(100000)
        self.mililitrosSlider.setSingleStep(1)
        self.mililitrosSlider.setValue(0)
        self.resultado.setReadOnly(True)
        self.mililitros.setReadOnly(True)
    def militros_a_litros(self):
        mililitros = self.mililitrosSlider.value()
        litros = mililitros /1000
        self.resultado.setText(str(litros))
        self.mililitros.setText(str(mililitros))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())