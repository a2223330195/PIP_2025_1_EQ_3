from matplotlib import pyplot as plt
import math

lim_inferior = -10
lim_superior = 0
funcion = "math.sin(45)"
val = 45
funcion = funcion.replace("x", str(val))
resultado = eval(funcion)
print(resultado)

x = list(range(lim_inferior, lim_superior + 1))
print(x)

m = 2
b = 4
y = [m * xi + b for xi in x]
print("y", y)

plt.plot(x, y)
plt.show()

y_sin = [math.sin(xi) for xi in x]
print("y_sin", y_sin)

plt.plot(x, y_sin)
plt.show()