import astropy.units as u
import numpy as np
import astropy.constants as c
import scipy.optimize as optimize

# define constants for LL designs
sub_t = 350*u.um #substrate thickness (Si in this case)
metal_t = 250*u.nm #Deposited metal thickness (Al)
Sc = 67*u.fF/(u.um)**2 #JJ specific capacitance
epsilon = 11.45
W_jj = 200*u.nm #junction width
phi0 = c.h/2/c.e.si
T = 30*u.mK

import qiskit_metal.analyses as analyses

def find_guided_wavelength(freq, line_width, line_gap):
    target_length = analyses.cpw_calculations.guided_wavelength(freq.to(u.Hz).value,
                                     line_width.to(u.m).value,
                                     line_gap.to(u.um).value,
                                     sub_t.to(u.m).value,
                                     metal_t.to(u.m).value,
                                     epsilon)[0]*u.m

    filling_factor = analyses.cpw_calculations.guided_wavelength(freq.to(u.Hz).value,
                                     line_width.to(u.m).value,
                                     line_gap.to(u.um).value,
                                     sub_t.to(u.m).value,
                                     metal_t.to(u.m).value,
                                     epsilon)[1]
    return target_length

def find_actual_frequency(length, line_width, line_gap, qwave = True):
    freq =  7*u.GHz
    len = find_guided_wavelength(freq, line_width, line_gap)
    if qwave:
        frequency = freq*len/length/4
    else:
        frequency = freq*len/length/8
    return frequency.to(u.GHz)

def transmon_freq(Cq, Lj):
    Ec = (c.e.si**2/2/Cq).to(u.J)
    Ej = ((phi0/2/np.pi)**2/Lj).to(u.J)
    # epsilon1 = -Ec*2**9
    wq = (np.sqrt(8*Ej*Ec)-Ec)/c.hbar
    fq = wq/2/np.pi
    alpha = Ec/c.h
    return(fq.to(u.GHz), alpha.to(u.MHz))