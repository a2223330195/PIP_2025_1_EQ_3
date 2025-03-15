import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P09_SegundoPlano.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_temporizador.clicked.connect(self.iniciarTempo)
        self.SegundoPlano = QtCore.QTimer()
        self.SegundoPlano.timeout.connect(self.temporizadorv2)
        self.value = 0
    def temporizador(self):
        import time as t
        valor = int(self.txt_temporizador.text())
        for v in range(valor, 0, -1):
            self.txt_temporizador.setText(str(v))
            t.sleep(0.25)
    def temporizadorv2(self):
        if self.value > 0:
            self.value -= 1
            self.txt_temporizador.setText(str(self.value))
        else:
            self.SegundoPlano.stop()
    def iniciarTempo(self):
        try:
            self.value = int(self.txt_temporizador.text())
            if self.value < 0:
                raise ValueError("Value must be non-negative")
            self.SegundoPlano.start(250)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
        except Exception as e: # Catch other potential errors (like empty input)
           QtWidgets.QMessageBox.critical(self, "Error", "Invalid input. Please enter a number.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())