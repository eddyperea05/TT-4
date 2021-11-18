import matplotlib.pyplot as plt

inicio = int(input('Introduce el año inicial de ventas: '))

fin = int(input('Introduce el año final de ventas: '))

ventas = {}

for i in range(inicio, fin+1):
    
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))

fig, ax = plt.subplots()

ax.plot(ventas.keys(), ventas.values())

plt.show()