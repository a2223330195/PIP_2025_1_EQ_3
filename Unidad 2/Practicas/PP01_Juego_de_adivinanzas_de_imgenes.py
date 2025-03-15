import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "PP01_Juego_de_adivinanzas_de_imgenes.ui"  # Nombre del archivo .ui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        # Configuración del QSlider
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        # Diccionario de imágenes
        self.datosImagenes = {
            0: [":/Logos/1.jpeg", "Galaxia"],
            1: [":/Logos/2.jpeg", "Sol"],
            2: [":/Logos/3.jpeg", "Luna"]
        }
        # Inicializar aleatoriamente el nombre de una imagen
        self.nombreAleatorio = random.choice(list(self.datosImagenes.values()))[1]
        self.txt_nombre_imagen.setText(self.nombreAleatorio)
    # Área de los Slots
    def cambiaValor(self):
        valor = self.horizontalSlider.value()
        Imagen_ruta = self.datosImagenes[valor][0]
        self.label_8.setPixmap(QtGui.QPixmap(Imagen_ruta))
        nombre = self.datosImagenes[valor][1]
        if nombre == self.txt_nombre_imagen.text():
            QtWidgets.QMessageBox.information(self, "Resultado", "¡Felicidades!")
        print(valor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())