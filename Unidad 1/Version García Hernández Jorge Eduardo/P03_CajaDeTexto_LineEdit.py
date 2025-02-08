import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P03_CajaDeTexto_LineEdit.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(self.saludar)
        self.a.clicked.connect(lambda:self.mensaje())

    def saludar(self):
        nombre=self.recibidor.text()
        print("Hola"+nombre)

    def mensaje(self):

        m=QtWidgets.QMessageBox()
        nombre=self.recibidor.text()
        m.setText(nombre)
        m.exec_()



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())