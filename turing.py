import numpy as np
import matplotlib.pyplot as plt
from configparser import ConfigParser
import os



def file_read(filename):
    
    """Checks the existence of the configuration file and reads the simulation parameters from it
       
    Parameters
        filename : name of the configuration file
    
    Returns:
        Values for n, delta_t, simulation_steps, a,b,c,d,h,k, diff_u, diff_v
        
    Raise:
        ValueError if the configuration file name is not found."""
        
    if os.path.isfile(filename):
        parser = ConfigParser()
        parser.read(filename)
        n = parser.getint('settings','n') # grid size
        delta_t = parser.getfloat('settings','delta_t') # temporal resolution
        simulation_steps = parser.getint('settings','simulation_steps') # number of delta_t steps performed
        
        # parameter values for reaction term:
        a = parser.getfloat('reaction','a')
        b = parser.getfloat('reaction','b')
        c = parser.getfloat('reaction','c')
        d = parser.getfloat('reaction','d')
        h = parser.getfloat('reaction','h')
        k = parser.getfloat('reaction','k')
        
        # diffusion coefficients of u and v  
        diff_u = parser.getfloat('diffusion','diff_u')
        diff_v = parser.getfloat('diffusion','diff_v')
        
    else:
        raise ValueError('Filename ' +filename+ ' not found')
    
    return n,delta_t,simulation_steps,a,b,c,d,h,k,diff_u,diff_v


# Read parameters from filename
n,delta_t,simulation_steps,a,b,c,d,h,k,diff_u,diff_v = file_read('configuration.txt')


delta_x = 1. / n # spatial resolution, assuming space is [1,0] * [0,1]


# Generates the random seeds
u = 1 + np.random.rand(n,n) * 0.06 - 0.03 
v = 1 + np.random.rand(n,n) * 0.06 - 0.03 


# Initializes the empty matrices for the loop
next_u = np.zeros((n,n))
next_v = np.zeros((n,n))



def simulation(u,v):
    for x in range(n):
        for y in range(n):
            
            u_center = u[x,y]
            u_right = u[(x+1)%n,y]
            u_left = u[(x-1)%n,y]
            u_up = u[x,(y+1)%n]
            u_down = u[x,(y-1)%n]
            
            v_center = v[x,y]
            v_right = v[(x+1)%n,y]
            v_left = v[(x-1)%n,y]
            v_up = v[x,(y+1)%n]
            v_down = v[x,(y-1)%n]
                        
            laplacian_u = (u_right + u_left + u_up + u_down - 4 * u_center) / delta_x**2
            laplacian_v = (v_right + v_left + v_up + v_down - 4 * v_center) / delta_x**2
    
            next_u[x,y] = u_center + (a*(u_center-h) + b*(v_center-k) + diff_u * laplacian_u) * delta_t
            next_v[x,y] = v_center + (c*(u_center-h) + d*(v_center-k) + diff_v * laplacian_v) * delta_t
            
    return next_u,next_v

            
def observe(u):
    
    plt.title('Time=%d'%i)
    plt.imshow(u, cmap='binary')
    plt.show()
    
    
#%% 

for i in range(simulation_steps):
    u,v = simulation(u,v)
    if i % 20 == 0:
        observe(u)
    
