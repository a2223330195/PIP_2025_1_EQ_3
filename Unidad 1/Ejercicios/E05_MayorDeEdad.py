import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="E05_MayorDeEdad.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.btn_calcularA.clicked.connect(self.CalcularEdad)

    #Area de los slots
    def CalcularEdad(self):
        try:
            edad = int(self.txt_valor.text())
            if edad<18:
                self.msj("Eres menor de edad tienes:"+str(edad)+ " años")
            else:
                self.msj("Eres mayor de edad tienes:" + str(edad) + " años")
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