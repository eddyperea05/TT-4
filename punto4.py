import numpy as np
lista = [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
lista = np.array(lista)
indices = np.where(lista != 0)
print(indices)