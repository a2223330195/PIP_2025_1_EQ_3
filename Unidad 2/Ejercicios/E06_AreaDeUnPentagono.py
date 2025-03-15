import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile="E06_AreaDeUnPentagono.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los signals
        self.btn_calculararea.clicked.connect(self.CalcularArea)


    #area de los slots
    def CalcularArea(self):
        try:
            perimetro=float(self.txt_perimetro.text())
            apotema= float(self.txt_apotema.text())
            area=(perimetro*apotema)/2
            self.msj("El área de tu pentágono es de:" + str(area) +" cm^2")
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())