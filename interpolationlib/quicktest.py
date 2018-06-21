import trigonometric_interpolation as trig
import numpy as np
import matplotlib.pyplot as plot

g = [i for i in range(0,11)]
h = [np.sin(i) for i in range(0,11)]
x = [np.sin(i) for i in range(0,11)]
u,v = trig.trig_interpolate(x,0,11)
plot.subplot(2,1,1)
plot.plot(u,v)
plot.subplot(2,1,2)
plot.plot(g,h)
plot.show()
