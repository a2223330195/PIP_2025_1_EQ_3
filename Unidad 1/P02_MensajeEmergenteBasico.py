import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P02_MensajeEmergenteBasico.ui"
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        #Area de los Signals

        self.btn_saludar.clicked.connect(self.saludar)
#Area de los Slots
    def saludar(self):
        self.msj("hola")
    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())