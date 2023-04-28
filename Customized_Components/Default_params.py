
import astropy.units as u
import numpy as np
import pandas as pd
import astropy.constants as c

from qiskit_metal import designs, Dict
from qiskit_metal.qlibrary.tlines.mixed_path import RouteMixed
from qiskit_metal.analyses.quantization import LOManalysis
from qiskit_metal.analyses.quantization import EPRanalysis

#This imports the necessary path to draw the single pad transmon design. 
import sys
sys.path.append('Customized_Components')
import Transmon_property as trans_p
import Transmon_specifications as jj
import Transmon_specifications as jj
from dolan_junction import DolanJunction as junction
from rounded_single_pad import Round_TransmonPocket_Single as transmon

import shapely
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

design = designs.DesignPlanar({}, True)
design.overwrite_enabled = True
design.chips.main.size['size_x'] = '10 mm'
design.chips.main.size['size_y'] = '10 mm'

# design.variables['cpw_width'] = '15.95 um'
# design.variables['cpw_gap'] = '9 um'

design.variables['cpw_wdith'] = '12.4 um'
design.variables['cpw_gap'] = '6.99 um'


design.variables['trace_width'] = '12.4 um'
cpw_pin_width = 12.4*u.um
design.variables['trace_gap'] = '6.99 um'
cpw_gap = 6.99*u.um

design.variables['pad_buffer_radius'] = '30 um'
design.variables['buffer_resolution'] = '10'
design.variables['connection_pad_buffer_radius'] = '2 um'

renderer_hfss = design.renderers.hfss
renderer_q3d = design.renderers.q3d

qb_options = dict(
pad_pocket_distance_top = '40um',
connection_pads = dict(
    a = dict(loc_W  = 0, 
            loc_H =  1, 
            pad_gap = '15um',
            pad_height = '15um',
            pad_width = '80um',
            pad_cpw_extent =  '10um',
            pocket_rise = '0um',
            cpw_extend = '0um',
            pocket_extent = '0um')))


TQ_options = dict(coupling_length='120 um',
                prime_width = design.variables['trace_width'],
               prime_gap = design.variables['trace_gap'],
               second_width = design.variables['trace_width'],
               second_gap = design.variables['trace_gap'],
               down_length = '60um',
               coupling_space = '5um',
               fillet = '30um',
               open_termination=False,
               hfss_wire_bonds = False,
               q3d_wire_bonds = False)

CPW_options = Dict(trace_width = design.variables['trace_width'],
               trace_gap  = design.variables['trace_gap'],
        total_length='5 mm',
        hfss_wire_bonds = True,
        q3d_wire_bonds = True,
        fillet='30 um',
        lead = dict(start_straight='15um', end_straight = '20um'),
        pin_inputs=Dict(
            start_pin=Dict(component='Q1', pin='a'),
            end_pin=Dict(component='TQ1', pin='second_end')), )

pin_inputs = Dict(
            start_pin=Dict(component='Q1', pin='a'),
            end_pin=Dict(component='TQ1', pin='second_end'))

trans_options = Dict(trace_width = design.variables['trace_width'],
               trace_gap  = design.variables['trace_gap'],
               lead = dict(start_straight='5um', end_straight = '5um'),
               fillet = '30um',
               total_length = '0.5mm',
               hfss_wire_bonds = True,
                     q3d_wirebonds = True,
               pin_inputs=Dict(
                 start_pin=Dict(
                     component='TQ1',
                     pin='prime_start'),
                 end_pin=Dict(
                     component='TQ2',
                     pin='prime_end')))

pocket_options = dict(
        pos_x = '0mm', 
        pos_y = '0mm', 
        orientation = '0',
        frequency = 5.2,
        guess_path = r'/Users/wendy/Desktop/Wendy-qiskit-code/data/educated_guess_0403.csv',
        coupling_path = '',
        sim = True,
        coord = '(0,0)',
        qubit_layer = 5,
        junction_layer = 2, 
        ab_layer = 8,
        ab_square_layer = 9,
        ab_distance = '70um'
        )


def init_q3d_sim(max_passes = 20, min_passes =10, wb_threshold = '72um'):
    renderer_q3d = design.renderers.q3d
    c1 = LOManalysis(design, "q3d")
    q3d = c1.sim.renderer
    c1.sim.setup.min_passes  = min_passes
    c1.sim.setup.max_passes = max_passes
    c1.sim.setup.freq_ghz = 5

    c1.sim.renderer.options['wb_threshold'] = wb_threshold
    c1.sim.renderer.options['x_buffer_width_mm'] = 0.5
    c1.sim.renderer.options['y_buffer_width_mm'] = 0.5

    return c1, renderer_q3d, q3d

def init_hfss_sim(nmode = 2, Ljs = ['13nH'], max_passes = 30, min_passes = 10, conv_threshold = 0.1, wb_threshold = '72um',):
    eig_all = EPRanalysis(design, 'hfss')
    renderer_hfss = design.renderers.hfss
    hfss = eig_all.sim.renderer
    eig_all.sim.renderer.options['wb_threshold'] = wb_threshold

    eig_all.sim.setup.max_passes = max_passes
    eig_all.sim.setup.min_passes = min_passes
    eig_all.sim.setup.max_delta_f = conv_threshold
    eig_all.sim.setup.n_modes = nmode
    eig_all.sim.renderer.options['x_buffer_width_mm'] = 0.5
    eig_all.sim.renderer.options['y_buffer_width_mm'] = 0.5
    for i,Lj in enumerate(Ljs):
        eig_all.sim.setup.vars ['Lj'.format(i+1)] = Lj
        eig_all.sim.setup.vars ['Cj'.format(i+1)] = jj.find_junction_capacitance(float(Lj[:-2]))
    return eig_all, renderer_hfss, hfss

def change_inductance(Ljs, eig_all, c1):
    for i,Lj in enumerate(Ljs):
        eig_all.sim.setup.vars ['Lj'.format(i+1)] = Lj
        c1.sim.setup.vars ['Lj'.format(i+1)] = Lj
        cc = jj.find_junction_capacitance(float(Lj[:-2]))
        eig_all.sim.setup.vars ['Cj'.format(i+1)] = cc
        c1.sim.setup.vars ['Cj'.format(i+1)] = cc

def construct_cpw(q,j, TQ, pad_size, offset, extend, gapp, Lj, Cj, TQx,TQy, small, TQ_mir,gui, design, displacement = '0um', buffer = 150*u.um, sim  = True, eig_all = ''):
    gap1 = 0.056
    gap = 30*u.um
    # print(pad_size)
    size = pad_size.to(u.um)
    pocket_width = size+2*gap
    cpw_name = 'cpw_'+ q.name[-1:]
    design.delete_component(cpw_name)
    coupling_len = extend
    q.options['pad_height'] = '{}'.format(size)
    q.options['pad_width'] = '{}'.format(size)
    q.options['pocket_width'] = '{}'.format(pocket_width)
    q.options['connection_pads']['a']['pad_width'] = '{}'.format(coupling_len)
    q.options['connection_pads']['a']['pad_height'] = '30um-{}'.format(gapp)
    q.options['connection_pads']['a']['pad_gap'] = '{}'.format(gapp)
    q.options.hfss_inductance = Lj
    q.options.q3d_inductance =  Lj
    q.options.hfss_capacitance = Cj
    q.options.q3d_capacitance =  Cj
    gui.rebuild()
    y_pos = (q.options.pad_height) + '/2' + '+' + (q.options.jj_length) +'-'+ (j.options.total_length)+'/4'
    x_pos  = q.options.pos_x
    j.options.pos_x = x_pos
    j.options.pos_y = '-'+'('+y_pos+')'+ '+'+q.options.pos_y
    # print(j.options.pos_y)

    gui.rebuild()


    l_name = 'Lj'+ q.name[-1:]
    c_name = 'Cj'+ q.name[-1:]

    if sim:
        eig_all.sim.renderer.options[l_name] = Lj
        eig_all.sim.renderer.options[c_name] = Cj
        eig_all.sim.setup.vars = {l_name:Lj, c_name:Cj}

    TQ.options.pos_x = TQx + '+' + displacement
    q.options.pos_x = displacement
    q.options.pos_y = '-'+TQy
    TQ.options.mirror = TQ_mir
    TQ.options.pos_y = '0um'
    gui.rebuild()

    anchors = trans_p.anchor_CPW_round(q, buffer, gap1, 2, small = small, last_offset = offset)
    design.delete_component(cpw_name)
    
    pin_inputs = Dict(
                start_pin=Dict(component=q.name, pin='a'),
                end_pin=Dict(component=TQ.name, pin='second_end'))

    CPW_options['pin_inputs'] = pin_inputs

    qa = RouteMixed(design, 'cpw_'+q.name[-1:], options = Dict(anchors = anchors, **CPW_options))

    gui.rebuild()
    
    return q,j, qa, TQ, design, gui

def slice_data(data, freq):
    diff = freq-4
    ind = round(diff/0.2)
    return data.iloc[ind]

def construct_cpw_qubit(q,j, TQ, freq, gui, design, eig_all = '', displacement = '0um', guess_path = r'data/educated_guess_0403.csv',sim = True):
    guess_all = pd.read_csv(guess_path)
    guesses = slice_data(guess_all, freq)
    size = guesses['Sizes (um)']*u.um
    # print(size)
    buffer = guesses['Buffers (um)']*u.um
    offset = guesses['Offsets (mm)']
    coupling_len = guesses['Coupling_len(um)']*u.um
    coupling_gap = guesses['Coupling_gap(um)']*u.um
    Lj = guesses['Ljs']
    Cj = jj.find_junction_capacitance(int(Lj[:-2])*u.nH)
    
    Cj1 = str(Cj.to(u.fF).value)+' fF'
    size = size.to(u.um)

    TQx = guesses['TQx']
    TQy = guesses['TQy']
    TQ_mir = guesses['TQ_mir']
    small = guesses['Small']
    
    q,j, cpw, TQ, design,gui = construct_cpw(q,j, TQ, size, offset, coupling_len, coupling_gap, Lj, Cj1, TQx,TQy, small, TQ_mir,gui, design,displacement, buffer, sim, eig_all)
    return q,j,cpw, TQ, design,gui

def make_qubit_from_scratch(design,gui, eig_all = '',sim = True):
    p = self.options
        # q,j, TQ, freq, gui, design, 
    guess_all = pd.read_csv(p.guess_path)
    guesses = slice_data(guess_all, p.frequency)
    size = guesses['Sizes (um)']*u.um
    buffer = guesses['Buffers (um)']*u.um
    offset = guesses['Offsets (mm)']
    coupling_len = guesses['Coupling_len(um)']*u.um
    coupling_gap = guesses['Coupling_gap(um)']*u.um
    Lj = guesses['Ljs']
    Cj = jj.find_junction_capacitance(int(Lj[:-2])*u.nH)
    
    Cj1 = str(Cj.to(u.fF).value)+' fF'
    size = size.to(u.um)

    TQx = guesses['TQx']
    TQy = guesses['TQy']
    TQ_mir = guesses['TQ_mir']
    small = guesses['Small']

    feedline_coupling_space = guesses['Coupling_gap_feedline(um)']
    

    #start making the components
    cpw_name = 'cpw_'+ q.name[-1:]
    design.delete_component(cpw_name)

    #make the qubit
    gap = 30*u.um
    size = size.to(u.um)
    pocket_width = size+2*gap
    
    
    qb_x = p.pos_x
    qb_y = p.pos_y+'-'+TQy
    qb_options = Dict(pos_x = qb_x,
                      pos_y = qb_y,
                      pad_height = '{}'.format(size), 
                      pad_width = '{}'.format(size), 
                      pocket_width = '{}'.format(pocket_width), 
                      hfss_inductance = Lj,
                      q3d_inductance =  Lj,
                      hfss_capacitance = Cj,
                      q3d_capacitance =  Cj,
                      layer = p.qubit_layer
                      **dp.qb_options)
    q = transmon(design,'Q1',options = qb_options)
    q.options['connection_pads']['a']['pad_width'] = '{}'.format(coupling_len)
    q.options['connection_pads']['a']['pad_height'] = '30um-{}'.format(coupling_gap)
    q.options['connection_pads']['a']['pad_gap'] = '{}'.format(coupling_gap)
    gui.rebuild()

    #make the junction
    y_pos = '-'+'('+(q.options.pad_height) + '/2' + '+' + (q.options.jj_length) +'-'+ (j.options.total_length)+'/4''+'+q.options.pos_y
    x_pos  = q.options.pos_x
    jj_options = Dict(pos_x = x_pos, 
                      pos_y = y_pos, 
                      taper_len='0.5um',
                      jj_gap = '0.14um',
                      Lj = Lj, 
                      layer = p.junction_layer)
    j = junction(design, 'd', options = jj_options)
    # j.options.pos_x = x_pos
    # j.options.pos_y = '-'+'('+y_pos+')'+ '+'+q.options.pos_y
    # j.options.layer = p.junction_layer
    gui.rebuild()


    l_name = 'Lj'+ q.name[-1:]
    c_name = 'Cj'+ q.name[-1:]

    if sim:
        eig_all.sim.renderer.options[l_name] = Lj
        eig_all.sim.renderer.options[c_name] = Cj
        eig_all.sim.setup.vars = {l_name:Lj, c_name:Cj}

    #make the coupled_line_tee
    TQ = dp.TQ_options['down_length'] = '40 um'
    TQ1 = CoupledLineTee(design, 'TQ1', options=dict(pos_x=TQx + '+' + p.pos_x,
                                                pos_y=p.pos_y,
                                                mirror = TQ_mir,
                                                layer = p.qubit_layer,
                                                **dp.TQ_options))
    gui.rebuild()

    #make the cpw
    gap1 = 0.056
    anchors = trans_p.anchor_CPW_round(q, buffer, gap1, 2, small = small, last_offset = offset)
    design.delete_component(cpw_name)
    
    pin_inputs = Dict(
                start_pin=Dict(component=q.name, pin='a'),
                end_pin=Dict(component=TQ.name, pin='second_end'))

    CPW_options['pin_inputs'] = pin_inputs

    cpw = RouteMixed(design, 'cpw_'+q.name[-1:], options = Dict(anchors = anchors, **CPW_options))

    gui.rebuild()
    return q,j,cpw, TQ, design,gui