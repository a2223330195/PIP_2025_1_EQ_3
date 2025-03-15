import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile="P016_CheckBox_Ejemplo1.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los signals
        self.cb_supergucci.clicked.connect(self.streamer)
        self.cb_mrbeast.clicked.connect(self.streamer)
        self.cb_alkapone.clicked.connect(self.streamer)

        self.cb_pollo.toggled.connect(self.comida)
        self.cb_tacos.toggled.connect(self.comida)
        self.cb_pizza.toggled.connect(self.comida)


        #area de los slots


    def streamer(self):
       obj = self.sender()
       valor = obj.isChecked()
       if valor:
         print("Streamer-Obj.  ",obj.text(),":", valor)

    def comida(self):
        obj = self.sender()
        valor = obj.isChecked()
        if valor:
            print("Comida-Obj. ", obj.text(), ":", valor)





if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())