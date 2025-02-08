import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P04_SumaDeDosNumeros.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(self.resuelve)

    def resuelve(self):
       numero=float(self.recibidor.text())
       numero2=float(self.recibidor_2.text())
       suma=numero+numero2
       m = QtWidgets.QMessageBox()
       m.setText("la respuesta es :" + str(suma))
       m.exec_()



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())