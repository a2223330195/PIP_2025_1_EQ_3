import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "PP02_Reloj_digital.ui" #Nombre del archivo aqui
Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindows):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindows.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        # Inicialización de la hora
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

        # Configuración del temporizador
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizarReloj)

        # Conectar botones
        self.btn_establecer_hora.clicked.connect(self.establecerHora)

        # Mostrar la hora inicial en ceros
        self.mostrarHora()

    def actualizarReloj(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1
        if self.horas == 24:
            self.horas = 0

        self.mostrarHora()

    def establecerHora(self):
        self.horas = int(self.txt_horas.text()) % 24
        self.minutos = int(self.txt_minutos.text()) % 60
        self.segundos = int(self.txt_segundos.text()) % 60
        self.mostrarHora()
        self.timer.start(100)

    def mostrarHora(self):
        hora_formateada = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
        self.lbl_hora.setText(hora_formateada)
#Area de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
