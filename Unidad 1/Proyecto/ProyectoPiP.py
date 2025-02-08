import sys, statistics
from PyQt5 import uic, QtWidgets

qtCreatorFile = "ProyectoPiP.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.guardar.clicked.connect(self.escribir)
        self.borrarb.clicked.connect(self.borrartodo)
        self.calcularb.clicked.connect(self.calcular_y_mostrar)
        self.guardarb.clicked.connect(self.guardarresultados)
        self.cargarrb.clicked.connect(self.mostrarresultados)
        self.borrarub.clicked.connect(self.borrarultimonumero)

    def es_float(self, cadena):  # self agregado
        try:
            float(cadena)
            return True
        except ValueError:
            return False

    def escribir(self):
        texto = self.numeros.text()
        if texto.isdigit():
            try:
                numero = int(texto)
                archivo = open("ProyectoPiP.txt", "a")
                archivo.write(str(numero) + ",")
                archivo.close()
                self.numeros.clear()
            except ValueError:
                self.resultado.setText("Error al convertir a entero")

        elif self.es_float(texto):
            try:
                numero = float(texto)
                archivo = open("ProyectoPiP.txt", "a")
                archivo.write(str(numero) + ",")
                archivo.close()
                self.numeros.clear()
                self.resultado.clear()
            except ValueError:
                self.resultado.setText("Error al convertir a float")
        else:
            self.resultado.setText("Ingrese un número")

        self.mostrar()  # Llamada al método mostrar

    def mostrar(self):
        self.resultado.clear()
        try:
            archivo = open("ProyectoPiP.txt", "r")
            contenido = archivo.read()
            if(contenido == ""):
                self.resultado.setText("No hay datos guardados")
            else:
                self.resultado.setText(contenido)
            archivo.close()
        except FileNotFoundError:
            self.resultado.setText("No hay datos guardados")

    def borrartodo(self):
        archivo = open("ProyectoPiP.txt", "w")
        archivo.close()
        self.resultado.clear()

    def calcular_y_mostrar(self):  # Nueva función
        try:
            lista_str = self.crearlista()

            if not lista_str:  # Lista vacía o error al leer el archivo
                self.resultado.setText("No hay datos para calcular o archivo vacío")
                return

            lista_num = []
            for elemento in lista_str:
                try:
                    num = float(elemento)
                    lista_num.append(num)
                except ValueError:
                    self.resultado.setText("Error: Datos inválidos en el archivo")  # Manejo de error
                    return  # Sale de la funcion para evitar errores posteriores

            valormin = min(lista_num)
            media = statistics.mean(lista_num)
            mediana = statistics.median(lista_num)
            try:
                moda = statistics.mode(lista_num)
            except statistics.StatisticsError:
                moda = "No hay moda única"
            desviacion = statistics.stdev(lista_num)
            varianza = statistics.variance(lista_num)
            self.ValorMenor.setText(str(valormin))
            self.ValorMayor.setText(str(max(lista_num)))
            self.ValorMedia.setText(str(media))
            self.ValorMediana.setText(str(mediana))
            self.ValorModa.setText(str(moda))
            self.ValorDesviacion.setText(str(desviacion))
            self.ValorVarianza.setText(str(varianza))


        except FileNotFoundError:
            self.resultado.setText("No hay datos para calcular")
        except ValueError as e:  # Manejo de errores generales
            self.resultado.setText(f"Error en los cálculos: {e}")

    def crearlista(self):
        try:
            archivo = open("ProyectoPiP.txt", "r")
            contenido = archivo.read()
            archivo.close()

            if not contenido:
                return []

            lista = contenido.split(",")
            lista.pop()
            return lista
        except FileNotFoundError:
            return []  # Devuelve una lista vacía si el archivo no existe

    def crearlistaresultados(self):
        try:
            archivo = open("ProyectoPiPResultados.txt", "w+")
            contenido = archivo.read()
            archivo.close()

            if not contenido:
                return []

            lista = contenido.split(",")
            lista.pop()
            return lista
        except FileNotFoundError:
            return []

    def guardarresultados(self):
        try:
            nuevos_resultados = ",".join([
                self.ValorMenor.text(),
                self.ValorMayor.text(),
                self.ValorMedia.text(),
                self.ValorMediana.text(),
                self.ValorModa.text(),
                self.ValorDesviacion.text(),
                self.ValorVarianza.text()
            ])

            # Abrir archivo en modo "w" para guardar
            archivo = open("ProyectoPiPResultados.txt", "w")
            archivo.write(nuevos_resultados)
            archivo.close()

        except ValueError:
            self.resultado.setText("Error al guardar resultados")

    def mostrarresultados(self):
        try:
            # Abrir archivo en modo "r" para cargar
            archivo = open("ProyectoPiPResultados.txt", "r")
            contenido = archivo.read()
            archivo.close()

            if contenido:  # Verificar si el archivo no está vacío
                lista = contenido.split(",")

                if len(lista) == 7:
                    self.ValorMenor.setText(lista[0])
                    self.ValorMayor.setText(lista[1])
                    self.ValorMedia.setText(lista[2])
                    self.ValorMediana.setText(lista[3])
                    self.ValorModa.setText(lista[4])
                    self.ValorDesviacion.setText(lista[5])
                    self.ValorVarianza.setText(lista[6])
                else:
                    self.resultado.setText("Error: Lista de resultados incompleta")
            else:
                self.resultado.setText("No hay resultados guardados")  # Mostrar mensaje si el archivo está vacío

        except FileNotFoundError:
            self.resultado.setText("No hay resultados guardados")
    def borrarultimonumero(self):
        try:
            archivo = open("ProyectoPiP.txt", "r")
            contenido = archivo.read()
            archivo.close()
            lista = contenido.split(",")
            lista.pop()
            lista.pop()
            archivo = open("ProyectoPiP.txt", "w")
            for elemento in lista:
                archivo.write(elemento + ",")
            archivo.close()
            self.mostrar()
        except FileNotFoundError:
            self.resultado.setText("No hay datos para borrar")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())