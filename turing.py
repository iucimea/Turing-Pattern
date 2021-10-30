import numpy as np
import matplotlib.pyplot as plt

#%% 
n = 200 # grid size
delta_x = 1. / n # spatial resolution, assuming space is [0,1] * [0,1]
delta_t = 0.02 # temporal resolution

a, b, c, d, h, k = 1., -1., 2., -1.5, 1., 1. # parameter values for reaction term: 
                                             # 
diff_u = 0.0001 # diffusion constant of u
diff_v = 0.0006 # diffusion constant of v

u = 1 + np.random.rand(n,n) * 0.06 - 0.03 #
v = 1 + np.random.rand(n,n) * 0.06 - 0.03 #

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
            
            v_center = u[x,y]
            v_right = u[(x+1)%n,y]
            v_left = u[(x-1)%n,y]
            v_up = u[x,(y+1)%n]
            v_down = u[x,(y-1)%n]
                        
            laplacian_u = (u_right + u_left + u_up + u_down - 4 * u_center) / delta_x**2
            laplacian_v = (v_right + v_left + v_up + v_down - 4 * v_center) / delta_x**2
    
            next_u[x,y] = u_center + (a*(u_center-h) + b*(v_center-k) + diff_u * laplacian_u) * delta_t
            next_v[x,y] = v_center + (c*(u_center-h) + d*(v_center-k) + diff_v * laplacian_v) * delta_t
            
    return next_u,next_v

    
            
def observe(u,v):
    
    plt.cla()
    plt.imshow(u)
    plt.title('u')

    # plt.subplot(1,2,2) 
    plt.cla()
    plt.imshow(v)
    plt.title('v')
    
    
#%% 
for i in range(1000):
    u,v = simulation(u, v)

#%%
observe(u,v)
