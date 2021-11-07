import numpy as np
lista = np.arange(0,5)
lista = np.tile(lista,5)
lista =  lista.reshape(5,5)
print(lista)