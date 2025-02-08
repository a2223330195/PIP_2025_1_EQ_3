import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_Carrusellimagenes.ui" #Nombre del archivo aqui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        self.selectorimagen.valueChanged.connect(self.cambiaValor)
        self.selectorimagen.setMinimum(-10)
        self.selectorimagen.setMaximum(10)
        self.selectorimagen.setSingleStep(2)
        self.selectorimagen.setValue(0)

        self.datosImagenes = {0:[":/Logos/1.jpeg","1"],
                              1:[":/Logos/2.jpeg","2"],
                              3:[":/Logos/3.jpeg","3"]}
        #Area de los Signals
#Area de los Slots
    def cambiaValor(self):
        valor = str(self.selectorimagen.value())
        Imagen_ruta = self.datosImagenes[valor][0]
        self.imagen.setPixmap(QtGui(Imagen_ruta))
        print(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

