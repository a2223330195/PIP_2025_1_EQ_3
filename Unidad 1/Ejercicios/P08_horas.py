import sys
from PyQt5 import uic, QtWidgets

# Cargar el archivo .ui creado en Qt Designer
qtCreatorFile = "E08_horas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar el botón al método calcular_horas_restantes
        self.btn_calcular.clicked.connect(self.calcular_horas_restantes)

    # Método para calcular cuántas horas quedan para terminar el día
    def calcular_horas_restantes(self):
        try:
            hora = int(self.txt_hora.text())  # Leer la hora ingresada
            if 0 <= hora <= 23:  # Validar que la hora esté en formato 24h
                horas_restantes = 24 - hora  # Calcular horas restantes
                self.txt_res.setText(str(horas_restantes))  # Mostrar resultado
            else:
                self.mostrar_mensaje("Por favor, ingresa una hora válida (0-23).")
        except ValueError:
            self.mostrar_mensaje("Entrada no válida. Ingresa un número entero.")

    # Método para mostrar un mensaje de error
    def mostrar_mensaje(self, texto):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setText(texto)
        mensaje.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
