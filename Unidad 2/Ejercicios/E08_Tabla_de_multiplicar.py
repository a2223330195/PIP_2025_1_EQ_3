import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E08_Tabla_de_multiplicar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class TablaMultiplicarApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Conectar el botón al método para generar la tabla
        self.btn_generar.clicked.connect(self.generar_tabla)
    def generar_tabla(self):
        # Obtener el valor del número seleccionado
        numero = self.spinBox.value()
        # Generar la tabla de multiplicar
        tabla = ""
        for i in range(1, 11):
            tabla += f"{numero} x {i} = {numero * i}\n"
        # Mostrar la tabla en el QTextEdit
        self.txt_tabla.setPlainText(tabla)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TablaMultiplicarApp()
    window.show()
    sys.exit(app.exec_())
