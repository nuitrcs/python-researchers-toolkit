import h5py
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
f = h5py.File("../data/Temperature.h5","r")
data=f['/Temperature']
delta=7./64.
x = np.arange(0,7, delta)
y = np.arange(0,7, delta)
X, Y = np.meshgrid(x,y)
dd=data
dd=np.power(10,dd)
dproj=np.sum(dd,axis=2)
dproj=np.log10(dproj)
plt.contourf(X,Y,dproj,50,cmap='hot')
plt.ylabel('x (Mpc/h)')
plt.xlabel('y (Mpc/h)')
plt.title('2D Projection of gas-Temperature redshift=3')
plt.savefig('projtemp.png')
plt.show()
f.close()
