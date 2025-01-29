import sys
from PyQt5 import uic, QtWidgets
from math import factorial

# Cargar el archivo .ui creado en Qt Designer
qtCreatorFile = "E09_factorial.ui"  # Cambia este nombre según el archivo que creaste
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar el botón al método calcular_factorial
        self.btn_calcular.clicked.connect(self.calcular_factorial)

    # Método para calcular el factorial
    def calcular_factorial(self):
        try:
            numero = int(self.txt_numero.text())  # Leer el número ingresado
            if numero < 0:
                self.mostrar_mensaje("El factorial no está definido para números negativos.")
            else:
                resultado = factorial(numero)  # Calcular el factorial
                self.txt_resultado.setText(str(resultado))  # Mostrar el resultado
        except ValueError:
            self.mostrar_mensaje("Por favor, ingresa un número entero válido.")

    # Método para mostrar mensajes de error o advertencias
    def mostrar_mensaje(self, texto):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setText(texto)
        mensaje.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
