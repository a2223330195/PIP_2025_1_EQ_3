import sys
from PyQt5 import uic, QtWidgets
import math

qtCreatorFile = "E07_Teorema_de_Pitágoras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class PitagorasApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Conectar el botón "Calcular" al método de cálculo
        self.btn_calcular.clicked.connect(self.calcular_hipotenusa)

    def calcular_hipotenusa(self):
        # Leer valores de los QDoubleSpinBox
        cateto_a = self.cat_a.value()
        cateto_b = self.cat_b.value()
        # Calcular hipotenusa usando el teorema de Pitágoras
        hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
        # Mostrar el resultado en el QLineEdit
        self.txt_resultado.setText(f"{hipotenusa:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PitagorasApp()
    window.show()
    sys.exit(app.exec_())
