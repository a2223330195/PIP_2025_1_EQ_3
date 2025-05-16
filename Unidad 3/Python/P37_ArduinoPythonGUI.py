import sys
from PyQt5 import uic, QtWidgets
import serial as placa
qtCreatorFile="P37_ArduinoPythonGui.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.arduino=None
        self.btn_accion.clicked.connect(self.accion)
    #area de los slots
    def accion(self):
        try:
            texto=self.btn_accion.text().upper()
            if texto == "CONECTAR":#iniciar la cmunicacion y la apetura
                com="COM"+self.txt_com.text()
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
                self.arduino= placa.Serial(com,baudrate=9600,timeout=1)
            elif texto == "DESCONECTAR":#cierra la comunicacion
                 self.btn_accion.setText("RECONECTAR")
                 self.txt_estado.setText("DESCONECTADO")
                 self.arduino.close()
            else:#reapertura la comunicacion
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
                self.arduino.open()
        except Exception as error:
            print(error)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())