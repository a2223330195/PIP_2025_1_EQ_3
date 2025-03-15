import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_CarruselImagen.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.cambiaValor)
        self.dial.setMinimum(0)
        self.dial.setMaximum(2)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)

        self.datosImagenes = {
            0: [":/logos/Logo UAT.png", "Logo UAT.png"],
            1: [":/logos/logo equipo 3.jpg", "logo equipo 3.jpg"],
            2: [":/logos/logo facultad de ingenieria uat.png", "logo facultad de ingenieria uat.png"]
        }
        self.cambiaValor()  # Initialize the image on startup
    def cambiaValor(self):
        valor = self.dial.value()
        try:
            imagen_ruta = self.datosImagenes[valor][0]
            nombre_imagen = self.datosImagenes[valor][1]  # Get the image name
            pixmap = QtGui.QPixmap(imagen_ruta)
            if not pixmap.isNull():
                self.imagen.setPixmap(pixmap)
                self.nombreimagen.setText(nombre_imagen)  # Set the name in the line edit
                print(f"Showing image: {nombre_imagen}")
            else:
                print(f"Error: Could not load image at {imagen_ruta}")
                self.imagen.clear()
                self.nombreimagen.clear() # Clear the line edit on error
        except KeyError:
            print(f"Error: Invalid image index: {valor}")
            self.imagen.clear()
            self.nombreimagen.clear() # Clear the line edit on error
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())