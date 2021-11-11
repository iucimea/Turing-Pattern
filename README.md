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

∂u∂t=a(u−h)+b(v−k)+DuΔ2u
∂u∂t=c(u−h)+d(v−k)+DuΔ2u

The state variables  u  and  v  represent concentrations of two chemical species.
a,b,c,  and  d  are parameters that determine the behavior of the reaction terms, while  h  and  k  are constants. 
Finally,  Du  and  Dv  are diffusion constants.

