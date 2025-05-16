import numpy as n

archivo = open("instancias.txt")
contenido = archivo.readlines()

X = contenido[3:3 + int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3 + int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

print("X:")
print(X)
print("Y:")
print(Y)
print("Elementos: ", X.shape)
print("Elementos: ", Y.shape)

porcentaje_entrenamiento = 0.8
Clases = ["Base de datos", "Diseño de puertos", "Medio Ambiente"]

n.random.seed(42)
indices_mezclados = n.random.permutation(X.shape[1])
X_mezclado = X[:, indices_mezclados]
Y_mezclado = Y[:, indices_mezclados]

media_global = n.mean(X_mezclado, axis=1, keepdims=True)
desv_global = n.std(X_mezclado, axis=1, keepdims=True)
X_norm = (X_mezclado - media_global) / desv_global

num_ejemplos = X_norm.shape[1]
num_entrenamiento = int(num_ejemplos * porcentaje_entrenamiento)

X_entreno = X_norm[:, :num_entrenamiento]
Y_entreno = Y_mezclado[:, :num_entrenamiento]

X_prueba = X_norm[:, num_entrenamiento:]
Y_prueba = Y_mezclado[:, num_entrenamiento:]

print("\n--- Split Validation ---")
print(f"Conjunto de entrenamiento: {X_entreno.shape[1]} ejemplos")
print(f"Conjunto de prueba: {X_prueba.shape[1]} ejemplos")

matriz_pesos = Y_entreno.dot(n.linalg.pinv(X_entreno))

casosCorrectos = 0

print("Prueba...")

for i in range(X_prueba.shape[1]):
    print("Prueba del Caso ", i + 1)
    casoi = X_prueba[:, i]
    print("Caso Analizado: ")
    print(casoi)

    Ycasoi = matriz_pesos.dot(casoi)
    print("Salidas Generadas: ")
    print(Ycasoi)

    print("Salida Real: ")
    Yrealcasoi = Y_prueba[:, i]
    print(Yrealcasoi)

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos += 1

    print("Clase Asignada: ", Clases[IndexMaxYcasoi])
    print("Clase Real: ", Clases[IndexMaxYrealcasoi])
    print()

total = X_prueba.shape[1]
print("Total de Casos Analizados: ", total)
print("Total de Casos Correctos: ", casosCorrectos)
print("Eficiencia del Split Validation: ", casosCorrectos/total*100.0)