import astropy.units as u
import numpy as np
import astropy.constants as c


Jc = 0.1*u.uA/(u.um)**2
Sc = 67*u.fF/(u.um)**2

Phi0 = c.h/2/c.e.si

def find_junction_area(Lj, Jc = Jc):
    Ej = ((Phi0/2/np.pi)**2/Lj).to(u.J)
    ic = Ej*2*np.pi/Phi0
    return ((ic/Jc).to(u.um**2))

def find_junction_capacitance(Lj):
    return((find_junction_area(Lj)*Sc).to(u.fF))

def place_junction(q,junction):
    y_pos = (q.options.pad_height) + '/2' + '+' + (q.options.jj_length) +'-'+ (junction.options.total_length)+'/4'
    x_pos  = q.options.pos_x

    junction.options.pos_x = x_pos
    junction.options.pos_y = '-'+'('+y_pos+')'+'+'+q.options.pos_y
    return q, junction