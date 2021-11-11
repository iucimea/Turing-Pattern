import numpy as np
import matplotlib.pyplot as plt

#%% 
n = 100 # grid size
delta_x = 1. / n # spatial resolution, assuming space is [0,1] * [0,1]
delta_t = 0.02 # temporal resolution
simulation_steps = 200

a, b, c, d, h, k = 1., -1., 2., -1.5, 1., 1. # parameter values for reaction term: 
                                             # 
diff_u = 0.0001 # diffusion constant of u
diff_v = 0.0006 # diffusion constant of v

u = 1 + np.random.rand(n,n) * 0.06 - 0.03 #
v = 1 + np.random.rand(n,n) * 0.06 - 0.03 #

start_u = u
start_v = v

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
    
    plt.title(i)
    plt.imsave(str(i), u, cmap='binary')
    
    plt.imshow(u, cmap='binary')

    
    
#%% 

# image_list = []

for i in range(simulation_steps):
    u,v = simulation(u,v)
    if i % 10 == 0:
        observe(u)
        # image_list.append(observe(u))
    
#%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

hmpf = np.ones([4,4])
hmpf[2][1] = 0
imagelist = [ hmpf*i*255./19. for i in range(20) ]

fig = plt.figure() # make figure

# make axesimage object
# the vmin and vmax here are very important to get the color map correct
im = plt.imshow(imagelist[0], cmap=plt.get_cmap('jet'), vmin=0, vmax=255)

# function to update figure
def updatefig(j):
    # set the data in the axesimage object
    im.set_array(imagelist[j])
    # return the artists set
    return [im]
# kick off the animation
ani = animation.FuncAnimation(fig, updatefig, frames=range(20), 
                              interval=50, blit=True)
plt.show()
