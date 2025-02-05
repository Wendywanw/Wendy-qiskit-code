import numpy as np
import astropy.units as u
import astropy.constants as c

phi0 = c.h/2/c.e.si
T = 30*u.mK
epsilon_r = 11.45
z0 = 50*u.Ohm


Cq = 20*u.fF
Lj = 13*u.nH
Ec = (c.e.si**2/2/Cq)/c.h

def g_alexPage(c1 = None,wr = 6*u.GHz, Lj = 13*u.nH):
    df = c1.sim.capacitance_matrix
    c_1 = -df['pad_left_Q1']['resonator_pad_Q1']*u.fF
    c_2 = -df['pad_right_Q1']['ground_main_plane']*u.fF
    c_3 = -df['pad_right_Q1']['resonator_pad_Q1']*u.fF
    c_4 = -df['pad_left_Q1']['ground_main_plane']*u.fF
    ct = -df['pad_left_Q1']['pad_right_Q1']*u.fF

    c_phi = (c_2+c_3)*(c_1+c_4)/(c_1+c_2+c_3+c_4)+2*u.fF+ct
    c_ceff = (c_1**2-c_3*c_4)/(c_1+c_2+c_3+c_4+ct)
    beta = (c_1*c_2-c_3*c_4)/((c_2+c_3)*(c_1+c_4)+ct*(c_1+c_2+c_3+c_4))
    Ec = (c.e.si**2/2/c_phi)/c.h
    Ej = ((phi0/2/np.pi)**2/Lj)/c.h
    w01 = np.sqrt(8*Ec*Ej)
    delta = wr-w01
    c_res = np.pi/2/wr/z0
    Vrms = np.sqrt(c.hbar*wr/2/c_res)
    g = c.e.si*Vrms*beta/c.hbar*np.sqrt(2)*(Ej/8/Ec)**0.25
    return g.to(u.MHz), Ec.to(u.MHz), Ej.to(u.GHz), w01.to(u.GHz)