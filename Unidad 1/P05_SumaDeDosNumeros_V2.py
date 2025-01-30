import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_SumaDeDosNumeros_V2.ui"
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        #Area de los Signals

        self.btn_sumar.clicked.connect(self.suma)
#Area de los Slots
    def suma(self):
        num1 = float(self.txt_a.text())
        num2 = float(self.txt_b.text())
        sum = num1 + num2
       # self.msj("La suma de los numeros es : " + str(sum))
        self.txt_resultado.setText(str(sum))
    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())