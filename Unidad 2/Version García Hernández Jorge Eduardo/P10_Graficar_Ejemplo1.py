from matplotlib import pyplot as plt
lim_inferior=-10
lim_superior=-10
x=[]
for i in range (lim_inferior,1):
    x.append(i)
print(x)
m=2
b=4
y=[]
for i in range(len(x)):
        y.append(m*x[i]+b)
print("y", y)
plt.plot(x,y)
plt.show()
