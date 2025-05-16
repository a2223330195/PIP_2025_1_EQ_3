import sys
from PyQt5 import uic, QtWidgets, QtCore
import serial as placa

qtCreatorFile1 = "Diseño_interfaz.ui"
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None
        self.max_items = 20

        self.btn_desactivar.clicked.connect(self.conectar_arduino)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leer_valor_fotocelda)
        self.timer.start(500)

    def conectar_arduino(self):
        try:
            if self.arduino is None or not self.arduino.is_open:
                self.arduino = placa.Serial("COM7", baudrate=9600, timeout=1)
                self.btn_desactivar.setText("DESCONECTAR")
                print("Arduino conectado")
            else:
                self.arduino.close()
                self.btn_desactivar.setText("CONECTAR")
                print("Arduino desconectado")
        except Exception as error:
            print(f"Error al conectar o desconectar el Arduino: {error}")

    def leer_valor_fotocelda(self):
        if self.arduino and self.arduino.is_open and self.arduino.in_waiting:
            try:
                linea = self.arduino.readline().decode('utf-8').strip()
                if linea.isdigit():
                    ldr_value = int(linea)
                    self.actualizar_estado_leds(ldr_value)
                    self.listWidget.addItem(f"Valor LDR: {ldr_value}")
                    if self.listWidget.count() > self.max_items:
                        self.listWidget.takeItem(0)
                    self.listWidget.scrollToItem(self.listWidget.item(self.listWidget.count() - 1))
            except Exception as e:
                print(f"Error al leer del Arduino: {e}")

    def actualizar_estado_leds(self, ldr_value):
        if ldr_value < 700:
            print("LED 1 encendido")
        if ldr_value < 500:
            print("LED 2 encendido")
        if ldr_value < 300:
            print("LED 3 encendido")
        if ldr_value < 200:
            print("LED 4 encendido")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
