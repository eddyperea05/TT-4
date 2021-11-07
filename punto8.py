import numpy as np

cuadrado = np.ones((10,10))
cuadrado[1:-1,1:-1] = 0
print(cuadrado)