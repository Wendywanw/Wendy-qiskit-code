import scqubits as scq
import numpy as np
import astropy.units as u
import astropy.constants as c

from scipy.optimize import root_scalar

import analysis.Transmon_property as tp

import scipy.optimize as optimize

# define constants for LL designs
sub_t = 350*u.um #substrate thickness (Si in this case)
metal_t = 100*u.nm #Deposited metal thickness (Al)
Sc = 67*u.fF/(u.um)**2 #JJ specific capacitance
epsilon = 11.45
W_jj = 200*u.nm #junction width
Z0 = 50*u.Ohm #characteristic impedance
import qiskit_metal.analyses as analyses

ratio = 65
Phi0 = (c.h / (2 * c.e.si))  # Flux quantum in Weber

def inductance_to_cap(L,ratio = ratio):
    EJ = (((Phi0/2/np.pi)**2/L).to(u.J)/c.h).to(u.GHz)
    EC = EJ/ratio
    return (c.e.si**2 / (2 * EC)/c.h).to(u.fF)

def target_function(L, desired_frequency, ratio):
    L = L * u.nH  # Convert L to nanohenrys
    calculated_frequency = calculate_qubit_freq(L, ratio)
    return calculated_frequency - desired_frequency
def calculate_qubit_freq(L,ratio = ratio):
    
    EJ = (((Phi0/2/np.pi)**2/L).to(u.J)/c.h).to(u.GHz)
    EC = EJ/ratio
    ng = 0.0   # Offset charge
    nlev = 10  # Number of energy levels to consider

    # Create a Transmon object
    transmon = scq.Transmon(EJ=EJ.value, EC=EC.value, ng=ng, ncut=30, truncated_dim=nlev)

    # Calculate the eigenenergies
    eigenenergies = transmon.eigenvals()

    # Calculate the transition frequencies (in GHz)
    transition_frequencies = np.diff(eigenenergies)

    # Calculate the anharmonicity (in GHz)
    anharmonicity = transition_frequencies[1] - transition_frequencies[0]
    return transition_frequencies[0]
    
class TransmonQubit():
    def __init__(self, freq, ratio):
        self.freq = freq
        self.ratio = ratio
        self.C = None,
        self.L = None
        self.EJ = None
        self.EC = None
        self.update_params()
        self.alpha = self.EC
        
    def update_params(self):
        self.C, self.L = self.qubit_freq_to_cap()
        Phi0 = (c.h / (2 * c.e.si))  # Flux quantum in Weber

        # Calculate the Josephson energy EJ and charging energy EC
        EJ = (((Phi0/2/np.pi)**2/self.L).to(u.J)/c.h).to(u.GHz)#, equivalencies=u.spectral())  # Convert to GHz
        EC = (c.e.si**2 / (2 * self.C)/c.h).to(u.GHz)
        self.EJ = EJ
        self.EC = EC
        
    def get_params(self):
        return [self.freq, self.ratio, self.qubit_capacitance, self.qubit_inductance, self.EJ, self.EC]
    def get_qcap(self):
        return self.C
    
    def get_qind(self):
        return self.L
    
    def get_EJ(self):
        return self.EJ
    
    def get_EC(self):
        return self.EC
    
    def qubit_freq_to_cap(self, ):
        desired_frequency = self.freq   # Desired frequency in GHz
        ratio = self.ratio
        # Use scipy.optimize.root_scalar to find the root
        def target_function(L, desired_frequency,):
            self.L = L * u.nH  # Convert L to nanohenrys
            self.calculate_qubit_freq()
            calculated_frequency = self.freq.to(u.GHz).value
            return calculated_frequency - desired_frequency
        result = root_scalar(target_function, args=(desired_frequency.to(u.GHz).value,), bracket=[1, 100], method='brentq')

        # Print the result
        if result.converged:
            L_optimal = result.root
            print(f"Optimal inductance L: {L_optimal} nH")
        else:
            print("Root finding did not converge")
        c_optimal = inductance_to_cap(L_optimal*u.nH, ratio = ratio)
        return c_optimal, L_optimal*u.nH
    def calculate_qubit_freq(self,):
        L = self.L
        ratio = self.ratio
        EJ = (((Phi0/2/np.pi)**2/L).to(u.J)/c.h).to(u.GHz)
        #, equivalencies=u.spectral())  # Convert to GHz
        EC = EJ/ratio
        ng = 0.0   # Offset charge
        nlev = 10  # Number of energy levels to consider

        # Create a Transmon object
        transmon = scq.Transmon(EJ=EJ.value, EC=EC.value, ng=ng, ncut=30, truncated_dim=nlev)

        # Calculate the eigenenergies
        eigenenergies = transmon.eigenvals()

        # Calculate the transition frequencies (in GHz)
        transition_frequencies = np.diff(eigenenergies)

        # Calculate the anharmonicity (in GHz)
        anharmonicity = transition_frequencies[1] - transition_frequencies[0]
        self.freq = transition_frequencies[0]*u.GHz
        self.alpha = anharmonicity*u.GHz
        
class ReadoutResonator():
    def __init__(self, freq, short_on_one_end = False,optimal_pin = None, optimal_gap = None ):
        self.freq = freq
        self.short_on_one_end = short_on_one_end
        self.substrate_thickness = 350*u.um
        self.film_thickness = 100*u.nm
        if (optimal_gap is None) and (optimal_pin is None):
            self.pin = 15*u.um
            self.optimize_gap()
        elif optimal_gap is None:
            self.pin = optimal_pin
            self.optimize_gap()
        elif optimal_pin is None:
            self.gap = optimal_gap
            self.optimize_pin()
        
        self.param_from_res_freq(freq, short_on_one_end = short_on_one_end)
        self.C = np.pi/2/self.freq/2/np.pi/self.Z0
        
    def get_params(self):
        return [self.L, self.C, self.target_length]
    
    def get_L(self):
        return self.L
    
    def get_C(self):
        return self.C
    
    def get_target_length(self):
        return self.target_length
    
    def param_from_res_freq(self,freq, short_on_one_end = False):
        self.Lk, self.Lext,self.Cl,self.G,self.Z0,self.etf,self.Cstar = analyses.cpw_calculations.lumped_cpw(freq = self.freq.to(u.Hz).value,
                                        line_width=self.pin.to(u.m).value,
                                        line_gap=self.gap.to(u.m).value,
                                        substrate_thickness=self.substrate_thickness.to(u.m).value,
                                        film_thickness=self.film_thickness.to(u.m).value,)
        self.Lk*=u.H
        self.Lext*=u.H
        self.Cl*=u.F/u.m
        
        self.G*=u.S
        self.Z0*=u.Ohm
        self.etf*=u.H/u.m
        self.Cstar*=u.F
        target_length = analyses.cpw_calculations.guided_wavelength(freq = self.freq.to(u.Hz).value,
                                        line_width=self.pin.to(u.m).value,
                                        line_gap=self.gap.to(u.m).value,
                                        substrate_thickness=self.substrate_thickness.to(u.m).value,
                                        film_thickness=self.film_thickness.to(u.m).value,)[0]*u.m
        if short_on_one_end:
            target_length /= 4
        else:
            target_length /= 2
        self.len = target_length
    def optimize_gap(self):
        def f(line_gap):
            return(analyses.cpw_calculations.lumped_cpw(self.freq.to(u.Hz).value,
                                            self.pin.to(u.m).value,
                                            line_gap,
                                            self.substrate_thickness.to(u.m).value,
                                            self.film_thickness.to(u.m).value)[4]-50)
        optimized_gap = optimize.fsolve(f,self.pin.si.value)[0]*u.m
        self.gap = optimized_gap.to(u.um)
    def optimize_pin(self):
        def f(line_width):
            return(analyses.cpw_calculations.lumped_cpw(self.freq.to(u.Hz).value,
                                            line_width,
                                            self.gap.si.value,
                                            self.substrate_thickness.to(u.m).value,
                                            self.film_thickness.to(u.m).value)[4]-50)
        optimized_pin = optimize.fsolve(f,self.gap.si.value)[0]*u.m
        self.pin = optimized_pin.to(u.um)
        
class DispersiveReadout():
    def __init__(self, qubit, res, T1, c_qr = None, c_tr = None):
        self.qubit = qubit
        self.res = res
        self.pT1 = T1
        self.optimize_cqr()
        self.optimize_ctr()
        
    def get_params(self):
        return [self.qubit, self.res, self.c_qr, self.c_tr]
    
    def get_cqr(self):
        return self.c_qr
    
    def get_ctr(self):
        return self.c_tr
    
    def get_qubit(self):
        return self.qubit
    
    def get_res(self):
        return self.res
    def calc_g(self):
        c_qr = self.c_qr
        Cq = self.qubit.C
        Cr = self.res.C
        wq = self.qubit.freq*np.pi*2
        wr = self.res.freq*np.pi*2
        EJ = self.qubit.EJ
        EC = self.qubit.EC
        return c_qr/Cq*np.sqrt(c.e.si**2*wr/c.hbar/Cr)*(EJ/8/EC)**0.25
    def update_g(self):
        self.g = self.calc_g()
    def calc_kappa(self):
        res = self.res
        c_tr = self.c_tr
        argv = [res.freq.si.value, 
                c_tr.si.value, 
                res.len.si.value, 
                res.pin.si.value, 
                res.gap.si.value, 
                2]
        
        return (analyses.em.kappa_calculation.kappa_in(res.freq.si.value, 
                c_tr.si.value, 
                res.len.si.value, 
                res.pin.si.value, 
                res.gap.si.value, 
                2)*u.Hz).to(u.MHz)
    def update_kappa(self):
        self.kappa = self.calc_kappa()
    def calc_chi(self):
        qubit = self.qubit
        resonator = self.res
        delta = (qubit.freq-resonator.freq)*2*np.pi
        sum_freq = (qubit.freq+resonator.freq)*2*np.pi
        alpha = qubit.EC
        return 2*self.g**2*(alpha/delta/(delta+alpha)+alpha/sum_freq/(sum_freq+alpha))
    def update_chi(self):
        self.chi = self.calc_chi()
    def calc_purcellT1(self,):
        qubit = self.qubit
        res = self.res
        
        delta = (qubit.freq-res.freq)*2*np.pi
        
        purcellGamma = self.g**2*self.kappa/delta**2
        
        return 1/purcellGamma/2/np.pi
    def calc_purcellT1q(self,update_g = True, update_chi = True):
        '''taking kappa = 2*chi for the optimal SNR, can directly get the T1q'''
        c_qr = self.c_qr
        qubit = self.qubit
        res = self.res
        if update_g:
            self.update_g()
        if update_chi:
            self.update_chi()
        delta = (qubit.freq-res.freq)*2*np.pi
        
        kappa_val = self.chi*2
        
        purcellGamma = self.g**2*kappa_val/delta**2
        return 1/purcellGamma/2/np.pi
    def optimize_cqr(self,):
        '''find the optimal coupling capacitance'''
        target_t1 = self.pT1
        c_qr = 1*u.fF
        self.c_qr = c_qr
        while self.calc_purcellT1q().to(u.ms) > 1.01*target_t1:
            c_qr += .1*u.fF
            self.c_qr = c_qr
        return c_qr
    def optimize_ctr(self, target_kappa=None):
        '''find the optimal coupling capacitance'''
        # if target_kappa is None:
        #     target_kappa = self.chi*2
        # c_tr = 1*u.fF
        # self.c_tr = c_tr
        # self.update_kappa()
        # while self.kappa < target_kappa:
        #     c_tr += .1*u.fF
        #     self.c_tr = c_tr
        #     self.update_kappa()
        # return c_tr
        self.c_tr = 1*u.fF
        return self.c_tr
