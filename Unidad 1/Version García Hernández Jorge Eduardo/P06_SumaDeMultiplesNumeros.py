import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P06_SumaDeMultiplesNumeros.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.a.clicked.connect(self.agregar)
        self.a_2.clicked.connect(self.guardar)
        self.numero=[]
    def guardar(self):
        archivo=open("Ejercicios/numeros.csv", "a")
        for num in self.numero:
            archivo.write(str(num) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado")
    def agregar(self):
        num = float(self.recibidor.text())
        self.numero.append(num)
        self.sumar()
    def sumar(self):
        sumaa=sum(self.numero)
        self.recibidor_3.setText(str(sumaa))



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())