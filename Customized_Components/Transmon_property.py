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
from qiskit_metal import designs
design = designs.DesignPlanar({}, True)

def find_guided_wavelength(freq, line_width, line_gap):
    target_length = analyses.cpw_calculations.guided_wavelength(freq.to(u.Hz).value,
                                     line_width.to(u.m).value,
                                     line_gap.to(u.m).value,
                                     sub_t.to(u.m).value,
                                     metal_t.to(u.m).value,
                                     epsilon)[0]*u.m

    filling_factor = analyses.cpw_calculations.guided_wavelength(freq.to(u.Hz).value,
                                     line_width.to(u.m).value,
                                     line_gap.to(u.m).value,
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

def freq_from_cap(cap, Lj = 13*u.nH):
    Ec = (c.e.si**2/2/Cq).to(u.J)
    Ej = ((phi0/2/np.pi)**2/Lj).to(u.J)
    # epsilon1 = -Ec*2**9
    wq = (np.sqrt(8*Ej*Ec)-Ec)/c.hbar
    fq = wq/2/np.pi
    alpha = Ec/c.h
    return fq, (wq, alpha)

import numpy as np
from collections import OrderedDict

def slice_dict(n,anchor):
    res = OrderedDict()
    if n<0:
        m = len(anchor)+n
    else:
        m = min(n,len(anchor))
    for i in range(m):
        res[i] = anchor[i]
    return res

def pins_for_spiral(radius,gap,n,dis = (0,0), r = np.inf, right = True):
    spiral_list = OrderedDict()
    x,y = dis
    print('1',x,y)
    i = 0
    if right:
        for step in range(n):
            point_value = radius / 2 + step * (0 + gap)
            spiral_list[step*4] = np.array([x+point_value, y-point_value])
            spiral_list[step*4+1] = np.array([x-point_value, y-point_value])
            spiral_list[step*4+2] = np.array([x-point_value, y+point_value])
            spiral_list[step*4+3] = np.array([x+point_value + (0 + gap), y+point_value])

        point_value = radius / 2 + (step + 1) * (0 + gap)
    else:
        for step in range(n):
            point_value = radius / 2 + step * (0 + gap)
            spiral_list[step*4] = np.array([x-point_value, y+point_value])
            spiral_list[step*4+1] = np.array([x+point_value, y+point_value])
            spiral_list[step*4+2] = np.array([x+point_value, y-point_value])
            spiral_list[step*4+3] = np.array([x-point_value + (0 - gap), y+point_value])

        point_value = radius / 2 + (step + 1) * (0 + gap)
        spiral_list[step*4+4] = np.array([point_value, point_value])
    
    final_list = slice_dict(r,spiral_list)
    
    return(final_list)

def anchor_CPW(qubit:designs.QDesign, buffer:float, wrap_gap:float, n:int, r = np.Inf, right = True):
    pocket_width = design.parse_value(qubit.options['pocket_width'])*u.mm
    cpad_height = design.parse_value(qubit.options['pad_height'])*u.mm
    distance_top = design.parse_value(qubit.options['pad_pocket_distance_top'])*u.mm
    jj_len = design.parse_value(qubit.options['jj_length'])*u.mm
    pocket_height = cpad_height + distance_top + jj_len
    
    wrap_r = max(pocket_width,pocket_height)+buffer
    
    x =design.parse_value(qubit.options['pos_x'])
    y =design.parse_value(qubit.options['pos_y'])
    
    
    anchors = pins_for_spiral(wrap_r.value, wrap_gap, n, dis = (x,y), right = right, r = r)
    return anchors

def find_wrap_size(qubit: designs.QDesign, buffer):
    pocket_width = design.parse_value(qubit.options['pocket_width'])*u.mm
    cpad_height = design.parse_value(qubit.options['pad_height'])*u.mm
    distance_top = design.parse_value(qubit.options['pad_pocket_distance_top'])*u.mm
    jj_len = design.parse_value(qubit.options['jj_length'])*u.mm
    pocket_height = cpad_height + distance_top + jj_len
    wrap_r = max(pocket_width,pocket_height)+buffer
    return wrap_r.to(u.mm).value

def find_total_len(cpw, qubit, TQ1, count_extend = False):
    pocket_width = design.parse_value(qubit.options['pocket_width'])*u.mm
    cpad_height = design.parse_value(qubit.options['pad_height'])*u.mm
    gap = (pocket_width-cpad_height)/2
    TQs = TQ1.options['down_length'] + '+' + TQ1.options['coupling_length'] + '+' + TQ1.options['down_length']
    
    if count_extend:
        QBextended = qubit.options['connection_pads']['a']['pad_width'] + '+'+ qubit.options['connection_pads']['a']['cpw_extend']
    else:
        QBextended = '0'
        
    cpw_length = gap + cpw.length*u.mm + design.parse_value(TQs  + '+' + QBextended )*u.mm
    
    return(cpw_length)