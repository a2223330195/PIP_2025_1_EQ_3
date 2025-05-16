from PyQt5 import uic, QtWidgets

qtCreatorFile3 = "Servicio_Alarma.ui"
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        self.acceso = rPrincipal  # Referencia al main
        self.buzzer_state = False  # Estado local del buzzer (False = apagado)

        # Conexiones
        self.btn_regresar.clicked.connect(self.regresar)
        self.btn_activar.clicked.connect(self.toggle_alarma)

    def regresar(self):
        self.close()
        self.acceso.show()

    def mostrar_alarma(self):
        QtWidgets.QMessageBox.information(self, "Mostrar Alarma", "Aquí mostrarías información de la alarma.")

    def toggle_alarma(self):
        arduino = self.acceso.arduino
        if arduino is not None and arduino.is_open:
            arduino.write(b"20DF906F\n")  # Código IR (Mute) para el buzzer
            self.buzzer_state = not self.buzzer_state

            if self.buzzer_state:
                self.label_4.setText("¡Hay alguien ahí!")
                self.btn_activar.setText("Desactivar")
            else:
                self.label_4.setText("No hay moros en la costa")
                self.btn_activar.setText("Activar")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Arduino no conectado.")
