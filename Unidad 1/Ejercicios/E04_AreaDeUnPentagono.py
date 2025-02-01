import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="E04_AreaDeUnPentagono.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.btn_calcularA.clicked.connect(self.CalcularArea)

    #Area de los slots
    def CalcularArea(self):
        try:
            num1 = float(self.txt_valor.text())
            num2 = float(self.txt_valor_2.text())
            area=(num1*num2)/2
            print("hola")
            self.msj("El área de tu pentágono es de:"+str(area)+" centímetros cuadrados")
        except Exception as error:
            print(error)



    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())