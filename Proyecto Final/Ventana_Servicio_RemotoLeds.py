from PyQt5 import uic, QtWidgets
import time
from threading import Thread

qtCreatorFile3 = "Servicio_RemotoLeds.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        self.acceso = rPrincipal
        self.btn_regresar.clicked.connect(self.regresar)

        # Alias para los LEDs
        self.LED1 = self.checkBox
        self.LED2 = self.checkBox_2
        self.LED3 = self.checkBox_3
        self.LED_OFF = self.checkBox_4  # Apagar todos

        # Conexión de eventos
        self.LED1.stateChanged.connect(self.check_led_individual)
        self.LED2.stateChanged.connect(self.check_led_individual)
        self.LED3.stateChanged.connect(self.check_led_individual)
        self.LED_OFF.stateChanged.connect(self.check_led_off)

        self.escuchando = True
        self.thread = Thread(target=self.escuchar_arduino)
        self.thread.start()

    def regresar(self):
        self.escuchando = False
        self.close()
        self.acceso.show()

    def enviar_codigo(self, codigo_hex):
        arduino = self.acceso.arduino
        if arduino is None or not arduino.is_open:
            QtWidgets.QMessageBox.warning(self, "Error", "Arduino no conectado.")
            return
        try:
            arduino.write((codigo_hex + "\n").encode())
            print("Enviado código IR:", codigo_hex)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def check_led_individual(self):
        # Si alguno de los LEDs individuales se activa, apaga el checkbox de apagar todo
        if self.sender().isChecked():
            self.LED_OFF.blockSignals(True)
            self.LED_OFF.setChecked(False)
            self.LED_OFF.blockSignals(False)

            # Enviar código correspondiente
            if self.sender() == self.LED1:
                self.enviar_codigo("20DF8877")
            elif self.sender() == self.LED2:
                self.enviar_codigo("20DF48B7")
            elif self.sender() == self.LED3:
                self.enviar_codigo("20DFC837")

    def check_led_off(self):
        if self.LED_OFF.isChecked():
            # Desactiva los otros 3 checkboxes
            for led in [self.LED1, self.LED2, self.LED3]:
                led.blockSignals(True)
                led.setChecked(False)
                led.blockSignals(False)
            self.enviar_codigo("20DF08F7")  # Código para apagar todos

    def escuchar_arduino(self):
        arduino = self.acceso.arduino
        if arduino is None:
            return

        while self.escuchando:
            if arduino.in_waiting > 0:
                mensaje = arduino.readline().decode().strip()
                print("Arduino dice:", mensaje)
            time.sleep(0.1)
