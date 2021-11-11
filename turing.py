import numpy as np
import matplotlib.pyplot as plt
from configparser import ConfigParser


parser = ConfigParser()
parser.read('configuration.txt')

# Simulation parameters
n = parser.get('settings','n') # grid size
delta_x = 1. / n # spatial resolution, assuming space is [1,0] * [0,1]
delta_t = parser.get('settings','delta_t') # temporal resolution
simulation_steps = parser.get('settings','simulation_steps') # number of delta_t steps performed 

n = int(n)
delta_t = float(delta_t)
simulation_steps = int(simulation_steps)



# parameter values for reaction term:
a, b, c, d, h, k = 1., -1., 2., -1.5, 1., 1.  
 
# diffusion coefficients of u and v                                             
diff_u = 0.0001 
diff_v = 0.0006

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
    
