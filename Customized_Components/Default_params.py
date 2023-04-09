from qiskit_metal import designs, Dict
import astropy.units as u

from qiskit_metal.analyses.quantization import LOManalysis
from qiskit_metal.analyses.quantization import EPRanalysis

#This imports the necessary path to draw the single pad transmon design. 
import sys
sys.path.append('Customized_Components')
import Transmon_property as trans_p
import Transmon_specifications as jj

import shapely
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

design = designs.DesignPlanar({}, True)
design.overwrite_enabled = True
design.chips.main.size['size_x'] = '20 mm'
design.chips.main.size['size_y'] = '10 mm'

design.variables['cpw_width'] = '15 um'
design.variables['cpw_gap'] = '9 um'

design.variables['trace_width'] = '12.4 um'
cpw_pin_width = 12.4*u.um
design.variables['trace_gap'] = '7 um'
cpw_gap = 7*u.um

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


TQ_options = dict(prime_width = design.variables['cpw_width'],
               prime_gap = design.variables['cpw_gap'],
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
        lead = dict(start_straight='20um', end_straight = '50um'),
        pin_inputs=Dict(
            start_pin=Dict(component='Q1', pin='a'),
            end_pin=Dict(component='TQ1', pin='second_end')), )

pin_inputs = Dict(
            start_pin=Dict(component='Q1', pin='a'),
            end_pin=Dict(component='TQ1', pin='second_end'))

trans_options = Dict(hfss_wire_bonds = True,
                     q3d_wirebonds = True,
               pin_inputs=Dict(
                 start_pin=Dict(
                     component='TQ1',
                     pin='prime_start'),
                 end_pin=Dict(
                     component='TQ2',
                     pin='prime_end')))


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
