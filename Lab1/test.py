import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

reader = np.loadtxt('toy_data.csv', delimiter='\t', unpack=True)
labels = np.array(reader[0])
d = np.array(reader[1:3])
data = np.transpose(d)
print(np.sum(data, axis=0).shape)
print(np.array([ 185.6102,  202.9751]).shape)
print(np.allclose(np.array(np.sum(data, axis=0)),np.array([185.6102, 202.9751])))
colors = ['r','b']
x,y = np.array(reader[1]), np.array(reader[2])
plt.scatter(x,y, c = labels, cmap=matplotlib.colors.ListedColormap(colors))
plt.show()
