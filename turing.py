import numpy as np
import matplotlib.pyplot as plt
from configparser import ConfigParser
import os


def config_read(filename):
    
    """Checks the existence of the configuration file and reads the simulation parameters from it
       
    Parameters
        filename : name of the configuration file
    
    Returns:
        Values for n, delta_t, simulation_steps, plot_steps, a,b,c,d,h,k, diff_u, diff_v
        
    Raise:
        ValueError if the configuration file name is not found."""
        
    if os.path.isfile(filename):
        parser = ConfigParser()
        parser.read(filename)
        
        #Settings for the matrices and simulation
        n = parser.getint('settings','n') # grid size
        delta_t = parser.getfloat('settings','delta_t') # temporal resolution
        simulation_steps = parser.getint('settings','simulation_steps') # number of delta_t steps performed
        plot_steps = parser.getint('settings','plot_steps') # Time spacing between 2 consecutive plots
        
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
    
    return n,delta_t,simulation_steps,plot_steps,a,b,c,d,h,k,diff_u,diff_v


# Read parameters from filename
n,delta_t,simulation_steps,plot_steps,a,b,c,d,h,k,diff_u,diff_v = config_read('configuration.txt')


delta_x = 1. / n # spatial resolution, assuming space is [1,0] * [0,1]




def starting_state(n):
    """This method generates 2 random concentration matrices for the reagents u and v.
       
    Parameters
        n : length and width of the square lattice.
    
    Returns:
        The state of the initial configuration of the (N*M) spins. 
        
    Raise:
        ValueError if length or width of the lattice is less than 1."""
    if n < 1:
        raise ValueError('The dimension of the lattice must be > 1, but is {}'.format(n))
    np.random.seed(1)
    init_state = 1 + np.random.rand(n,n) * 0.06 - 0.03
    next_state = np.zeros((n,n))
    return init_state, next_state


# Generates the initial random concentration distributions
u = starting_state(n)[0]
v = starting_state(n)[0]


# Initializes the empty matrices for the loop
next_u = starting_state(n)[1]
next_v = starting_state(n)[1]



def simulation(u,v):
    
    """Performs the reaction diffusion simulation starting from 2 random matrices of concentrations u and v
       
    Parameters
        u : concentration matrix for reagent u
        v : concentration matrix for reagent v
    
    Returns:
        Matrices next_u, next_v with the concentrations updated by the reaction diffusion equation"""
        
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
    
    """Plots the concentration matrix in a 2D binary colormap visualization
       
    Parameters
        u : concentration matrix for reagent u
    
    Returns:
        2D plot for the concentration matrix u"""
    
    plt.title('Time=%d'%i)
    plt.imshow(u, cmap='binary')
    plt.show()
    
    
#%% Loop performing the simulation and plotting the result every "plot_steps" number of steps

for i in range(simulation_steps):
    u,v = simulation(u,v)
    if i % plot_steps == 0:
        observe(u)
    
