import sys
import random
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E09_Adivina_el_número.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class AdivinaNumeroApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Generar un número aleatorio entre 1 y 100
        self.numero_secreto = random.randint(1, 10)
        self.intentos = 0  # Contador de intentos
        # Conectar el botón al método para comprobar el intento
        self.btn_adivinar.clicked.connect(self.comprobar_intento)
    def reiniciar_juego(self):
        # Generar un nuevo número secreto y reiniciar el contador de intentos
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.adivinar_numero.append("Se ha generado un nuevo número. ¡Intenta adivinarlo!")
    def comprobar_intento(self):
        # Obtener el valor del número ingresado por el usuario desde el QSpinBox
        intento = self.spinBox.value()
        self.intentos += 1  # Incrementar el contador de intentos
        # Comparar el intento con el número secreto
        if intento < self.numero_secreto:
            self.adivinar_numero.setPlainText(f"Intento #{self.intentos}: ¡Muy bajo! Intenta con un número mayor.")
        elif intento > self.numero_secreto:
            self.adivinar_numero.setPlainText(f"Intento #{self.intentos}: ¡Muy alto! Intenta con un número menor.")
        else:
            self.adivinar_numero.setPlainText(f"¡Correcto! 🎉 Has adivinado el número en {self.intentos} intentos.")
            self.reiniciar_juego()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdivinaNumeroApp()
    window.show()
    sys.exit(app.exec_())
