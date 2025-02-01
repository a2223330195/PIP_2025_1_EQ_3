import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="E06_ImprimirTablaDeMultiplicar.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.btn_mostrarTabla.clicked.connect(self.ImprimirTabla)

    #Area de los slots
    def ImprimirTabla(self):
        try:
            num = int(self.txt_valor.text())
            for i in range(1,11):
                print(f'{num} x {i} = {num*i}')

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