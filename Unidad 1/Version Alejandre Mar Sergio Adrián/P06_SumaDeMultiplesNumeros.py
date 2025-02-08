import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="P06_SumaDeMultiplesNumeros-save.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.numeros=[]

    #Area de los slots
    def agregar(self):
        try:
            num=float(self.txt_numero.text())
            self.numeros.append(num)
            self.sumar()
        except Exception as error:
            print(error)



    def guardar(self):
        archivo=open("../Archivos/numeros.csv","w")#"w"=write/"a"=append
        for num in self.numeros:
            archivo.write(str(num)+"\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado! :D")

    def sumar(self):
        sumaa=sum(self.numeros)
        self.txt_suma.setText(str(sumaa))



    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())