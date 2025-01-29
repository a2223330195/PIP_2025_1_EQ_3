import sys
from PyQt5 import uic, QtWidgets

# Nombre del archivo .ui que creaste con Qt Designer
qtCreatorFile = "E07_contador.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectamos el botón al método contar_caracteres
        self.btn_contar.clicked.connect(self.contar_caracteres)

    # Método para contar los caracteres de la cadena
    def contar_caracteres(self):
        cadena = self.txt_cadena.text()  # Obtenemos el texto de la entrada
        cantidad = len(cadena)  # Contamos los caracteres
        self.txt_resultado.setText(str(cantidad))  # Mostramos el resultado en el segundo LineEdit

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
