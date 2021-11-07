import numpy as np
randnums = np.random.randint(0, 9, size=(3, 3, 3))
print(randnums)
#Punto 7


print(np.where(randnums == np.amin(randnums)))
print(np.amin(randnums))
print(np.where(randnums == np.amax(randnums)))
print(np.amax(randnums))
#print(np.argmax(randnums))