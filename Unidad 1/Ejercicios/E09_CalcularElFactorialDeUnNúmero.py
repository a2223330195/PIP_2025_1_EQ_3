import sys
from PyQt5 import uic, QtWidgets
from math import factorial
qtCreatorFile = "E09_CalcularElFactorialDeUnNúmero.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcular_factorial)

    def calcular_factorial(self):
        try:
            numero = int(self.txt_numero.text())
            if numero < 0:
                self.mostrar_mensaje("El factorial no está definido para números negativos.")
            else:
                resultado = factorial(numero)
                self.txt_resultado.setText(str(resultado))
        except ValueError:
            self.mostrar_mensaje("Por favor, ingresa un número entero válido.")

    def mostrar_mensaje(self, texto):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setText(texto)
        mensaje.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
