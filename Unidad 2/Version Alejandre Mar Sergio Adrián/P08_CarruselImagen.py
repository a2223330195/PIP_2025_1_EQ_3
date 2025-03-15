import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile="P08_CarruselImagenes.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de signals
        self.selectorimagen.valueChanged.connect(self.cambiaValor)
        self.selectorimagen.setMinimum(0)
        self.selectorimagen.setMaximum(2)
        self.selectorimagen.setSingleStep(1)
        self.selectorimagen.setValue(0)

        self.datosImagenes ={
            0:[":/Logos/993971.png","Mary"],
            1:[":/Logos/993966.png","Yume"],
            2:[":/Logos/01.jpeg","Saturno"]
        }

    # area de slots
    def cambiaValor(self):
      try:
          valor=self.selectorimagen.value()
          imagen_ruta=self.datosImagenes[valor][0]
          self.imagen.setPixmap(QtGui.QPixmap(imagen_ruta))
          nombre= self.datosImagenes[valor][1]
          self.txt_nombre_imagen.setText(nombre)
          print(valor)
      except Exception as error:
          print(error)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())