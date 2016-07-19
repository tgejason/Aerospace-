import math
import numpy
import matplotlib.pyplot

h = .10 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    ###Your code here.
    vector_to_earth= -spaceship_position
    acceleration_spacecraft =gravitational_constant*( earth_mass/numpy.linalg.norm(vector_to_earth)**3
                                                            *vector_to_earth) 
    return acceleration_spacecraft
    
def ship_trajectory():
    num_steps = 1300000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

	###Your code here. This code should call the above 
	###acceleration function.
    for i in range(num_steps):
            x[i+1] = x[i]+h*v[i]
            v[i+1] = v[i]+h*acceleration(x[i])
    return x, v

x, v = ship_trajectory()

def plot_me():        
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0) #earth
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
plot_me()
    
