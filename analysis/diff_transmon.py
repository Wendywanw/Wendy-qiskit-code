import copy
import astropy.units as u
import astropy.constants as c 
import numpy as np 
from Transmon import find_junction_area

def pad_len_from_C(c):
    slope = (900-500)/(101.367-61.365)
    intercept = 500 - slope*61.365
    
    return slope*c.to(u.fF).value + intercept 
def unitless_find_j_area(L):
    return find_junction_area(L*u.nH,Jc = 0.42*u.uA/u.um**2).to(u.um**2).value

def unitless_find_pad_len(C):
    slope = (900-500)/(101.367-61.365)
    intercept = 500 - slope*61.365
    
    return slope*C + intercept
def convert_capacitance_to_energy(capacitance):
    C = capacitance*u.fF
    return (c.e.si**2 / (2 * C)/c.h).to(u.GHz)

def get_cap_params(caps, cj):
    cap_matrix = copy.deepcopy(caps)
    T = np.array([[1,0,-1,0],
              [0,1,0,0],
              [1,0,1,0],
              [0,0,0,1]])
    cap_matrix[0,2] -= cj
    cap_matrix[2,0] -= cj
    cap_matrix[2,2] += cj
    cap_matrix[0,0] += cj
    differential_cap_matrix = np.linalg.inv(T).T@(cap_matrix)@np.linalg.inv(T)
    inverse = np.linalg.inv(differential_cap_matrix)
    qubit_capacitance = np.reciprocal(inverse)[0,0]
    coupling_capacitance = np.reciprocal(inverse)[0,1]
    Ec = convert_capacitance_to_energy(qubit_capacitance)
    g = 8*convert_capacitance_to_energy(coupling_capacitance).to(u.MHz)
    return [Ec,g,qubit_capacitance,coupling_capacitance]
    