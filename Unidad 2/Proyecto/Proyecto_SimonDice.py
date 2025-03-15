import sys
import random as r
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "Proyecto_SimonDice.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.buat.clicked.connect(lambda: self.verificar_clic("guitarra.png"))
        self.bfit.clicked.connect(lambda: self.verificar_clic("tambor.png"))
        self.blog.clicked.connect(lambda: self.verificar_clic("trompeta.png"))
        self.bcar.clicked.connect(lambda: self.verificar_clic("piano.png"))
        self.nombre_imagenes = ["guitarra.png", "tambor.png", "trompeta.png", "piano.png"]
        self.secuencia_generada = []
        self.secuencia_usuario = []
        self.empezar_juego()

    def empezar_juego(self):
        self.secuencia_generada = []
        self.secuencia_usuario = []
        self.agregar_imagen_a_secuencia()
        self.mostrar_secuencia()

    def agregar_imagen_a_secuencia(self):
        imagen = r.choice(self.nombre_imagenes)
        self.secuencia_generada.append(imagen)

    def mostrar_secuencia(self):
        self.lineor.setText(self.secuencia_generada[-1])

    def verificar_clic(self, nombre_imagen):
        self.secuencia_usuario.append(nombre_imagen)
        if self.secuencia_usuario == self.secuencia_generada[:len(self.secuencia_usuario)]:
            if len(self.secuencia_usuario) == len(self.secuencia_generada):
                self.agregar_imagen_a_secuencia()
                self.mostrar_secuencia()
                self.secuencia_usuario = []
                self.mostrar_exito()
                self.empezar_juego()
        else:
            self.mostrar_error()
            self.empezar_juego()

    def mostrar_error(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("¡Te has equivocado!")
        msg.setWindowTitle("Error")
        msg.exec_()

    def mostrar_exito(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("¡Has acertado!")
        msg.setWindowTitle("Felicidades")
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())