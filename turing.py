import numpy as np
import matplotlib.pyplot as plt


n = 100 # grid size
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

# def simulation(u,v,next_u,next_v):
    
def observe(u,v):
    
    plt.subplot(1,2,1)
    plt.cla()
    plt.imshow(u)
    plt.title('u')

    plt.subplot(1,2,2)
    plt.cla()
    plt.imshow(v)
    plt.title('v')



observe(u,v)
