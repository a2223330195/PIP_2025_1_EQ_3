import sys
from PyQt5 import uic, QtWidgets
import serial as placa
import Ventana_Servicio_RemotoLeds
import Ventana_Servicio_Ventilador
import Ventana_Servicio_Alarma

qtCreatorFile1 = "Main_SeleccionarServicio.ui"
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)
        self.btn_servicio1.clicked.connect(self.abrir_servicio_remoto_leds)
        self.btn_servicio2.clicked.connect(self.abrir_servicio_alarma)
        self.btn_servicio3.clicked.connect(self.abrir_servicio_ventilador)

    def accion(self):
        try:
            texto = self.btn_accion.text().upper()
            if texto == "CONECTAR":
                com = "COM" + self.txt_com.text()
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
                self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
            elif texto == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.txt_estado.setText("DESCONECTADO")
                self.arduino.close()
            else:
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
                self.arduino.open()
        except Exception as error:
            print(error)

    def abrir_servicio_remoto_leds(self):
        dialog = Ventana_Servicio_RemotoLeds.MyDialog(self)
        dialog.exec_()

    def abrir_servicio_alarma(self):
        dialog = Ventana_Servicio_Alarma.MyDialog(self)
        dialog.exec_()

    def abrir_servicio_ventilador(self):
        dialog = Ventana_Servicio_Ventilador.MyDialog(self)
        dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
