#http://matplotlib.org/users/pyplot_tutorial.html
#http://mple.m-artwork.eu/

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import mpl_toolkits.mplot3d.axes3d as axes3d

#Simple Graph
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

#Multiple plots
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


#Create multiple panels of plots (subplots) 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

#create and plot histogram of data
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


#Plot sin with labels and reference lines
fig = plt.figure(figsize=(4, 5))

ax = fig.add_subplot(111)

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(x)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.plot(x, y,linewidth="3", alpha=0.3)

ax.plot([0, np.pi/2], [1, 1], ls="--", color="green", linewidth="3",alpha=0.5)
ax.plot([np.pi/2, np.pi/2], [1, 0], ls="--", color="red", linewidth="3",alpha=0.5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')


ax.set_xlim(-2*np.pi, 2*np.pi)

xticker = np.arange(-np.pi-np.pi/2, np.pi+np.pi, np.pi/2)
xlabels = [r"$\frac{-3\pi}{2}$", r"${-\pi}$",r"$\frac{-\pi}{2}$","",r"$\frac{pi}{2}$",r"${\pi}$",r"$\frac{3\pi}{2}$"]

ax.set_xticks(xticker)
ax.set_xticklabels(xlabels, size=17)

ax.text(np.pi, 1.1, "y=sin(x)")

ax.set_ylim(-1.5, 1.5)
yticker = np.arange(-1, 2, 1)
ax.set_yticks(yticker)

plt.show()

#Surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Data
fx = [0.673574075,0.727952994,0.6746285,0.797313558,0.37664721,0.67939197,0.748490102,0.722048276,0.767189284,0.768296082,0.732383162,0.748429373,0.751570337,0.698977802,0.703398777,0.802607746,0.786242535,0.366661714,0.792490268,0.698636545,0.769904493,0.762656928,0.478595152,0.759151743,0.728607906,0.778099194,0.728575153,0.703794547]
fy = [0.331657721,0.447817839,0.37733386,0.306640864,0.107229109,0.329287287,0.758907052,0.310634309,0.277462605,0.333935925,0.326699919,0.72242944,0.358848707,0.298222369,0.306303486,0.43058538,0.373973649,0.117132288,0.432939444,0.255479494,0.384761779,0.382446444,0.35914706,0.298360515,0.391041147,0.363895412,0.312359532,0.343344197]
fz = [18.13629648,8.620699842,9.807536512,17.40105183,24.44101897,18.81025228,8.075948931,18.10817229,22.24192367,13.8497555,13.28436202,4.472128831,14.53195939,15.93922217,0,0,11.28194885,0,0,26.12423918,9.200498046,14.01392223,14.14545413,17.8320704,8.985897324,10.53443457,12.48561226,11.80438073]

#generate data for regression equation
Xs = np.arange(0.4, 0.8, 0.005)
Ys = np.arange(0.2, 0.7, 0.005)
Xs, Ys = np.meshgrid(Xs, Ys)

#3D regression solved using DataFit(R), http://www.oakdaleengr.com/
Zs = 41.0909875400163+15.3581432751401*np.log(Xs)+-90.9714747515509*Ys+64.9652271333282*Ys**2

ax.plot(fx, fy, fz, linestyle="none", marker="o", mfc="none", markeredgecolor="red")

#plot wireframe
#ax.plot_wireframe(Xs, Ys, Zs, rstride=4, cstride=4, alpha=0.4)

#plot surface, more colormaps: http://matplotlib.sourceforge.net/examples/pylab_examples/show_colormaps.html
ax.plot_surface(Xs, Ys, Zs, rstride=4, cstride=4, alpha=0.4,cmap=cm.jet)

plt.show()
