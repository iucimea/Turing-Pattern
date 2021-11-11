# Turing-Pattern

Reaction-diffusion systems are continuous ﬁeld models whose equations are made of only reaction terms and diffusion terms, as shown below:

![alt text](https://github.com/iucimea/Turing-Pattern/blob/main/Images/CodeCogsEqn.gif)


Reaction terms ( Ri(...) ) describe only local dynamics, without any spatial derivatives involved. 
Diffusion terms ( Di ∇2 fi ) are limited to the Laplacian of the state variable itself. 


The clear separation between non-spatial and spatial dynamics makes the modeling and simulation tasks easy, 
but despite the simplicity of their mathematical form, reaction-diffusion systems can show strikingly rich, 
complex spatio-temporal dynamics. 

Alan Turing’s partial differential equation models were among the ﬁrst reaction-diffusion systems developed in the early 1950s. 
A simple linear version of Turing’s equations is the following:

![alt text](https://github.com/iucimea/Turing-Pattern/blob/main/Images/CodeCogsEqn%20(1).gif)

![alt text](https://github.com/iucimea/Turing-Pattern/blob/main/Images/CodeCogsEqn%20(2).gif)

The state variables  u  and  v  represent concentrations of two chemical species.
a,b,c,  and  d  are parameters that determine the behavior of the reaction terms, while  h  and  k  are constants. 
Finally,  Du  and  Dv  are diffusion constants.

## Structure of the project
The following are the steps in order to start the program and to plot the results:

1) Firstly, the user has to enter the simulation parameters in the file [configuration.txt](https://github.com/iucimea/Turing-Pattern/blob/main/configuration.txt).
He has to specify the lattice size "n", the simulation time step "delta_t", the number of steps "simulation_steps" and the step number between 2 consecutive plots "plot_steps".
Furthermore, the reaction and diffusion coefficients can be modified.

2) Then, to start the Turing-Pattern simulation preparation the user has to run the file [turing.py](https://github.com/iucimea/Turing-Pattern/blob/main/turing.py) which imports its parameters from [configuration.txt](https://github.com/iucimea/Turing-Pattern/blob/main/configuration.txt) using the ConfigParser library.
This step initializes the matrices that are needed for the simulation and loads the simulation function.

3) The last lines of the code launch a for loop that performs the simulation over the given time steps and plots the result at regular intervals.
