import math
import numpy
import matplotlib.pyplot

h = 0.1 # s
g = 9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 120000. # m / s


def trajectory():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 300000
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        ###Your code here.
        angle_rad = math.pi/180. * angle
        x[0,0] = 0
        x[0,1] = 0
        v[0,0] = initial_speed*math.cos(angle_rad)
        v[0,1] = initial_speed*math.sin(angle_rad)
        for i in range(num_steps):
            x[i+1] = x[i]+h*v[i]
            v[i+1] = v[i]+h*acceleration
           
        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    matplotlib.pyplot.show()
    return x, v
    #matplotlib.pyplot.show() 
trajectory()
