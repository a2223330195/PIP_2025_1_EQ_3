from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile3 = "Servicio_Ventilador.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, rPrincipal):
        super().__init__()
        self.acceso = rPrincipal
        self.setupUi(self)

        self.dial.setMinimum(0)
        self.dial.setMaximum(255)
        self.dial.valueChanged.connect(self.dial_cambiado)

        self.btn_regresar.clicked.connect(self.regresar)

        self.radioButton.toggled.connect(self.cambiar_modo)
        self.radioButton_3.toggled.connect(self.cambiar_modo)
        self.radioButton_4.toggled.connect(self.cambiar_modo)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leer_arduino)
        self.timer.start(100)

        self.modo_actual = 0  # 0=Apagado, 1=Medio, 2=Máximo, 3=Potenciómetro

    def regresar(self):
        self.timer.stop()
        self.close()
        self.acceso.show()

    def cambiar_modo(self):
        arduino = self.acceso.arduino
        if arduino is None or not arduino.is_open:
            return

        if self.radioButton.isChecked():  # Apagado (PWM = 0)
            self.modo_actual = 0
            self.dial.setEnabled(False)
            self.dial.setValue(0)
            arduino.write(b"AUTO\n")
            self.enviar_pwm(0)



        elif self.radioButton_3.isChecked():  # Máximo (PWM = 255)
            self.modo_actual = 2
            self.dial.setEnabled(False)
            self.dial.setValue(255)
            arduino.write(b"AUTO\n")
            self.enviar_pwm(255)

        elif self.radioButton_4.isChecked():  # Potenciómetro (manual)
            self.modo_actual = 3
            self.dial.setEnabled(False)
            arduino.write(b"MANUAL\n")  # Activa lectura del potenciómetro

    def leer_arduino(self):
        if self.modo_actual != 3:
            return

        arduino = self.acceso.arduino
        if arduino is None or not arduino.is_open:
            return

        try:
            while arduino.in_waiting:
                linea = arduino.readline().decode(errors='ignore').strip()
                if "Potenciómetro:" in linea:
                    partes = linea.split("|")
                    pot_part = partes[0].split(":")[1].strip()
                    pot_value = int(pot_part)
                    pwm_value = int(pot_value * 255 / 1023)
                    self.dial.setValue(pwm_value)
                    print(f"Potenciómetro: {pot_value} -> PWM: {pwm_value}")
        except Exception as e:
            print("Error leyendo del Arduino:", e)

    def enviar_pwm(self, valor):
        arduino = self.acceso.arduino
        if arduino is None or not arduino.is_open:
            return
        try:
            arduino.write((str(valor) + "\n").encode())
        except Exception as e:
            print("Error enviando PWM:", e)

    def dial_cambiado(self):
        if self.modo_actual == 3:
            self.enviar_pwm(self.dial.value())

    def enviar_valor_manual(self):
        if self.modo_actual == 3:
            self.enviar_pwm(self.dial.value())
