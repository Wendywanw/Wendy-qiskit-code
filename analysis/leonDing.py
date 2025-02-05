import astropy.units as u 
import astropy.constants as c
import numpy as np
from dr_calc import get_cap_params, get_cap_params_dim4,qubit_zpf, res_zpf
import copy
from dr_calc import ReadoutResonator as res


phi0 = c.h/2/c.e.si
epsilon_r = 11.45
z0 = 50*u.Ohm

def g_leonDing_old(dim = 4, c1 = None, cj = 2, Lj = 13*u.nH):
    df = c1.sim.capacitance_matrix
    df1 = copy.deepcopy(df)
    df1['ground_main_plane']['ground_main_plane'] += res.C.to(u.fF).value
    df1['resonator_pad_Q1']['resonator_pad_Q1'] += res.C.to(u.fF).value
    df1['resonator_pad_Q1']['ground_main_plane'] -= res.C.to(u.fF).value
    df1['ground_main_plane']['resonator_pad_Q1'] -= res.C.to(u.fF).value
    cap = df1.to_numpy()
    if dim == 3:
        capp = cap[1:,1:]
        Ec, J,_,_ = get_cap_params(capp,cj)
    elif dim == 4:
        capp = cap
        Ec, J,_,_ = get_cap_params_dim4(capp,cj) 
        
    
    # Ec = (c.e.si**2/2/Cq)/c.h
    Ej = ((phi0/2/np.pi)**2/Lj)/c.h   
    g = (qubit_zpf(Ej,Ec)*J*res_zpf()).to(u.MHz)
    
    
    
    return g, Ec, Ej, 
def g_leonDing(dim = 4, c1 = None, cj = 2, Lj = 13*u.nH):
    df = c1.sim.capacitance_matrix
    df1 = copy.deepcopy(df)
    
    
    # df1['ground_main_plane']['ground_main_plane'] += res.C.to(u.fF).value
    # df1['resonator_pad_Q1']['resonator_pad_Q1'] += res.C.to(u.fF).value
    # df1['resonator_pad_Q1']['ground_main_plane'] -= res.C.to(u.fF).value
    # df1['ground_main_plane']['resonator_pad_Q1'] -= res.C.to(u.fF).value
    cap = df1.to_numpy()
    cap[1,1] += cap[0,1]
    cap[2,2] += cap[0,2]
    cap[3,3] += cap[0,3]
    
    cap[0,3] += res.C.to(u.fF).value
    cap[3,0] += res.C.to(u.fF).value
    cap[0,0] -= res.C.to(u.fF).value
    cap[3,3] -= res.C.to(u.fF).value
    
    
    if dim == 3:
        capp = cap[1:,1:]
        Ec, J,_,_ = get_cap_params(capp,cj)
    elif dim == 4:
        capp = cap
        Ec, J,_,_ = get_cap_params_dim4(capp,cj) 
        
    
    # Ec = (c.e.si**2/2/Cq)/c.h
    Ej = ((phi0/2/np.pi)**2/Lj)/c.h   
    g = (qubit_zpf(Ej,Ec)*J*res_zpf()).to(u.MHz)
    
    
    
    return g, Ec, Ej, 