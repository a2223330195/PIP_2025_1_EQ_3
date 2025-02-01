import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E08_HorasQueLeRestanAlDíaParaTerminarse.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcular_horas_restantes)

    def calcular_horas_restantes(self):
        try:
            hora = int(self.txt_hora.text())
            if 0 <= hora <= 23:
                horas_restantes = 24 - hora
                self.txt_res.setText(str(horas_restantes))
            else:
                self.mostrar_mensaje("Por favor, ingresa una hora válida (0-23).")
        except ValueError:
            self.mostrar_mensaje("Entrada no válida. Ingresa un número entero.")

    def mostrar_mensaje(self, texto):
        mensaje = QtWidgets.QMessageBox()
        mensaje.setText(texto)
        mensaje.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
