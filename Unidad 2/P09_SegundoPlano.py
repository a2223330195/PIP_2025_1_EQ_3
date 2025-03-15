import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P09_SegundoPlano.ui"
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_temporizador.clicked.connect(self.iniciarTiempo)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizadorV2)
    def iniciarTiempo(self):
        self.value = int(self.txt_temporizador.text())
        self.segundoPlano.start(250)
    def temporizadorV2(self):
        if self.value>0:
            self.value -= 1
            self.txt_temporizador.setText(str(self.value))
        else:
            self.segundoPlano.stop()
    def temporizador(self):
        import time as t
        valor = int(self.txt_temporizador.text())
        for v in range(valor, 0, -1):
            self.txt_temporizador.setText(str(v))
            print(v)
            t.sleep(0.25)
#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
