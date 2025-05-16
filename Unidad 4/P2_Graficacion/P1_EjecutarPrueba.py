import sys
from PyQt5 import uic, QtWidgets
#qtCreatorFile = "P00_Introduccion.ui" #Nombre del archivo aqui
#Ui_MainWindows, QtBaseClass = uic.loadUiType(qtCreatorFile)

import P4_plantilla_Grafica as interfaz
import matplotlib.pyplot as plt
class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_graficar.clicked.connect(self.graficar)
        #Area de los Slots
        #valorres por defecto:
        self.configuracion = {
            "estilo_linea":":",
            "color_linea":"black",
            "ancho_linea":1
        }
        self.limite = {
            "x": [1, 10, 10], #min, max, division
            "y": [1, 10, 10]  #min, max, division
        }
    #Area de los Slots
    def graficar(self):
        polinomio = self.txt_polinomio.text() #Ej: 2x^2+3x+4
        polinomio = polinomio.replace("^", "**") #Ej: 2x**2+3x+4

        #tabular valores de x con base en los cuales pueda obtener los valores de y
        X = [i for i in range(self.limite["x"][0], self.limite["x"][1])] #lista de comprension
        print("Valores de X: ")
        print(X)

        y = [eval(polinomio.replace("x","*("+str(x)+")")) for x in X]
        print("Valores de Y: ")
        print(y)

        self.ax.plot(X, y,
                 linestyle = self.configuracion["estilo_linea"],
                 color = self.configuracion["color_linea"],
                 linewidth = self.configuracion["ancho_linea"],
                 marker = ".",
                 markersize = 4,
                 markerfacecolor = "yellow",
                 markeredgewidth = 1,
                 markeredgecolor = "blue",
                 dash_capstyle = "butt",
                 dash_joinstyle = "miter"
                 )
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


