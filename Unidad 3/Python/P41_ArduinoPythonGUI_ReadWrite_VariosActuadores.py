import sys
from PyQt5 import uic, QtWidgets,QtCore
import serial as placa
qtCreatorFile="P41_ArduinoPythonGui_ReadWrite_VariosActuadores.ui"#Nombre del archivo
Ui_MainWindow, QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #area de los signals
        self.arduino=None
        self.btn_accion.clicked.connect(self.accion)
        self.btn_led0.clicked.connect(self.control)
        self.btn_led1.clicked.connect(self.control)
        self.btn_led2.clicked.connect(self.control)
        #self.segundoPlano=QtCore.QTimer()
        #self.segundoPlano.timeout.connect(self.lecturas)
    #area de los slots
    def lecturas(self):
       if self.arduino.isOpen():#ña cpmunicacioon esta abierta
          if self.arduino.inWaiting():#hay informacion que leer...
              lectura = self.arduino.readline().decode().strip()
              if lectura !="":
                  print(lectura)
                  #Preocesamiento de los datos
                  lectura=lectura.split("@")
                  lectura = lectura[:-1]
                  lectura=[int(i)for i in lectura]
                  self.lista_datos.addItem(str(lectura[0]))
                  self.lista_datos.setCurrentRow(self.lista_datos.count()-1)
    def control(self):
        try:
           objeto = self.sender()
           if self.arduino.isOpen():
               led = objeto.objectName()[-1]
               texto = objeto.text()
               if texto=="Prender":
                   objeto.setText("Apagar")
                   c = led + "1"
                   self.arduino.write(c.encode())
               else:
                   objeto.setText("Prender")
                   c = led + "0"
                   self.arduino.write(c.encode())
        except Exception as error:
            print(error)
    def accion(self):
        try:
            texto=self.btn_accion.text().upper()
            if texto == "CONECTAR":#iniciar la cmunicacion y la apetura
                com="COM"+self.txt_com.text()
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("CONECTADO")
                self.arduino= placa.Serial(com,baudrate=9600,timeout=1)
                #self.segundoPlano.start(100)
            elif texto == "DESCONECTAR":#cierra la comunicacion
                 self.btn_accion.setText("RECONECTAR")
                 self.txt_estado.setText("DESCONECTADO")
                #self.segundoPlano.stop()
                 self.arduino.close()
            else:#reapertura la comunicacion
                self.btn_accion.setText("DESCONECTAR")
                self.txt_estado.setText("RECONECTADO")
                self.arduino.open()
                #self.segundoPlano.start(100)
        except Exception as error:
            print(error)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())