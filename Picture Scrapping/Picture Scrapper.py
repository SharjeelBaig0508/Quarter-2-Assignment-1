# %matplotlib inline
import numpy as np
import matplotlib.pylab as plt
list1 = []
for i in range(20):
    ch = chr(ord('A') + i)
    print("Storing :",'Balloon-' + ch + '.png')
    # list1.append(plt.imread('Balloon-' + ch + '.png')[ : 300 , : 300 , : ])
    list1.append(plt.imread('Balloon-' + ch + '.png'))

nparray = np.array(list1)
plt.imshow(nparray[11])
plt.show()
print(nparray)
