import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_Carrusellimagenes.ui"
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        # Configuración del QDial
        self.selectorimagen.valueChanged.connect(self.cambiaValor)
        self.selectorimagen.setMinimum(0)
        self.selectorimagen.setMaximum(2)
        self.selectorimagen.setSingleStep(1)
        self.selectorimagen.setValue(0)
        # Diccionario de imágenes
        self.datosImagenes = {
            0: [":/Logos/1.jpeg", "Galaxia"],
            1: [":/Logos/2.jpeg", "Sol"],
            2: [":/Logos/3.jpeg", "Luna"]
        }
        nombre = self.datosImagenes[0][1]
        self.txt_nombre_imagen.setText(nombre)
        #Área de los Slots
    def cambiaValor(self):
        valor = self.selectorimagen.value()
        Imagen_ruta = self.datosImagenes[valor][0]
        self.imagen.setPixmap(QtGui.QPixmap(Imagen_ruta))
        nombre = self.datosImagenes[valor][1]
        self.txt_nombre_imagen.setText(nombre)
        print(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


