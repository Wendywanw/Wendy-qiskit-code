import astropy.units as u
import numpy as np
import astropy.constants as c


Jc = 0.5*u.uA/(u.um)**2
Sc = 67*u.fF/(u.um)**2

Phi0 = c.h/2/c.e.si

def find_junction_area(Lj):
    Ej = ((Phi0/2/np.pi)**2/Lj).to(u.J)
    ic = Ej*2*np.pi/Phi0
    return ((ic/Jc).to(u.um**2))

def find_junction_capacitance(Lj):
    return((find_junction_area(Lj)*Sc).to(u.fF))