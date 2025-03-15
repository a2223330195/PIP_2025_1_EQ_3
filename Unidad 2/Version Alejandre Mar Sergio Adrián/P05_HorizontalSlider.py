import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P05_HorizontalSlider.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de signals
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.horizontalSlider.setMinimum(-10)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(2)
        self.horizontalSlider.setValue(0)



    # area de slots
    def cambiaValor(self):
        valor=str(self.horizontalSlider.value())
        self.lineEdit.setText(valor)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())