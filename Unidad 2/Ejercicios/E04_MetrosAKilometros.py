import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile="E04_MetrosAKilometros.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los signals
        self.btn_convertir.clicked.connect(self.convertirAKilometros)


    #area de los slots
    def convertirAKilometros(self):
        valor=float(self.txt_valor.text())
        conv=valor/1000
        self.txt_valor_2.setText(str(conv))

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())