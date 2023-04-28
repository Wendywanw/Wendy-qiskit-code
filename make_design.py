import os
import shutil
import time

import astropy.units as u
import numpy as np
import pandas as pd
import astropy.constants as c

#Import the necessary path to draw the single pad transmon design. 
import sys
sys.path.append('Customized_Components')
from rounded_single_pad import Round_TransmonPocket_Single as transmon
import Transmon_property as trans_p
import Transmon_specifications as jj
from dolan_junction import DolanJunction as junction
import Default_params as dp
from pocket import TransmonPocket as pocket

from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond
from qiskit_metal import MetalGUI, Dict
from qiskit_metal.qlibrary.couplers.coupled_line_tee import CoupledLineTee

gui = MetalGUI(dp.design)
design = dp.design

qubit_layer = 5
junction_layer = 2
ab_layer = 8
ab_square_layer = 9

top_leftx = -5
top_lefty = 5
left_wb_xs = [1.6, 0.5-0.3]
left_wb_ys = [5-0.5+0.3]
left_wb_ys.append(5-1.6)
for i in range(8):
    new_y = left_wb_ys[-1]-0.85
    new_x = 0.5-0.3
    left_wb_xs.append(new_x)
    left_wb_ys.append(new_y)
# left_wb_ys.append(-5)

left_wb_xs = np.array(left_wb_xs)+top_leftx
left_wb_ys = np.array(left_wb_ys)

orientations_left = [270,0,0,0,0,0,0,0,0,0]

top_rightx = 5
top_righty = 5
right_wb_xs = [5-1.6,4.5+0.3]
right_wb_ys = [5-0.5+0.3]
right_wb_ys.append(5-1.6)
for i in range(8):
    new_y = right_wb_ys[-1]-0.85
    right_wb_ys.append(new_y)
    new_x = 5-0.5+0.3
    right_wb_xs.append(new_x)
right_wb_ys = np.array(right_wb_ys)

orientations_right = [270,180,180,180,180,180,180,180,180,180]
Wirebond_left_opt = Dict(trace_width=design.variables['trace_width'],
                           trace_gap=design.variables['trace_gap'],
                           lead_length='8um',
                           pad_width='200um',
                           pad_height='100um',
                           pad_gap='50um',
                           taper_height='50um',
                           layer = str(qubit_layer))


left_lauch_pads = []
for i in range(10):
    left_lauch_pads.append(LaunchpadWirebond(design,'wb_left'+str(i), options = Dict(pos_x = '{}mm'.format(left_wb_xs[i]),pos_y = '{}mm'.format(left_wb_ys[i]),orientation = orientations_left[i],**Wirebond_left_opt)))

right_lauch_pads = []
for i in range(10):
    right_lauch_pads.append(LaunchpadWirebond(design,'wb_right'+str(i), options = Dict(pos_x = '{}mm'.format(right_wb_xs[i]),pos_y = '{}mm'.format(right_wb_ys[i]),orientation = orientations_right[i],**Wirebond_left_opt)))


ind_odd = np.array((4, 9, 3, 8, 2, 6, 0, 5, 1, 7))
ind_even = np.array((9, 4, 8, 3, 7, 1, 5, 0, 6, 2))

freq_odd = 3.8+0.2*ind_odd
freq_even = 3.8+0.2*ind_even

pocket_options = dict(
        pos_x = '0mm', 
        pos_y = '0mm', 
        orientation = '0',
        frequency = 5.2,
        guess_path = r'/Users/wendy/Desktop/Wendy-qiskit-code/data/educated_guess_all_new.csv',
        coupling_path = '',
        sim = True,
        coord = '(0,0)',
        qubit_layer = 5,
        junction_layer = 2, 
        ab_layer = 8,
        ab_square_layer = 9,
        ab_distance = '70um',
        rotation = 90
        )

qubit_y1 = ['3.8mm','3.65mm','2.70000mm','1.750000mm','0.8000mm',
            '-0.150000mm','-1.10000mm','-2.050000mm','-3.0000mm','-3.950000mm']

qubit_x0 = ['-3.9mm', '-3.1mm', '-2.2mm', 
            '-1.3mm', '-0.4mm', '0.5mm',
            '1.4mm', '2.3mm','3.2mm', '4.05mm']
qubit_y0 = ['4.5mm'] + ['3.8mm']*8 + ['4.4mm']
qubit_angles0 = [90,180,180,180,180,180,180,180,180,270]

pockets = []
for i in range(10):
    j = i
    pocket_options['pos_x'] = qubit_x0[j]
    pocket_options['pos_y'] = qubit_y0[j]
    pocket_options['frequency'] = freq_even[j]
    pocket_options['coord'] = '({},0)'.format(j)
    pocket_options['rotation'] = qubit_angles0[j]
    p = pocket(gui, design,options = pocket_options)
    pockets.append(p)
    if i ==0:
        pass
    else:
        pockets[i].connect(pockets[i-1])

pockets[-1].connect(right_lauch_pads[0])
pockets[0].connect(left_lauch_pads[0])

distance = 0.93
xs = []
x0 = -4.2
for i in range(10):
    print(x0+distance*i)
    xs.append(str(x0+distance*i)+'mm')

for i in range(1,10):
    poc = []
    for j in range(10):
        pocket_options['pos_x'] = xs[j]
        pocket_options['pos_y'] = qubit_y1[i]
        pocket_options['coord'] = '({},{})'.format(j,i)
        if i%2 == 1:
            pocket_options['frequency'] = freq_odd[j]
        else:
            pocket_options['frequency'] = freq_even[j]
        pocket_options['rotation'] = 0 #qubit_angles0[j]
        p = pocket(gui, design,options = pocket_options)
        poc.append(p)
        if j ==0:
           poc[j].connect(left_lauch_pads[i], buffer = 0.0) 
        elif j == 9:
            poc[j].connect(poc[j-1])
            poc[j].connect(right_lauch_pads[i], buffer = 0.0)
        else:
            poc[j].connect(poc[j-1])
    pockets.append(poc)

gui.rebuild()
print('done rebuilding structure!')

def export_gds(name = 'export_test_2.gds'):
    a_gds = design.renderers.gds
    a_gds.options.cheese.edge_nocheese = '100um'
    a_gds.options.no_cheese.buffer = '50um'
    a_gds.options.cheese.cheese_1_radius = '70um'

    a_gds.options['cheese']['view_in_file']['main'][qubit_layer] = True
    a_gds.options['no_cheese']['view_in_file']['main'][qubit_layer] = True
    a_gds.options['cheese']['view_in_file']['main'][junction_layer] = False
    a_gds.options['no_cheese']['view_in_file']['main'][junction_layer] = True
    a_gds.options['cheese']['view_in_file']['main'][ab_layer] = False
    a_gds.options['no_cheese']['view_in_file']['main'][ab_layer] = True
    a_gds.options['cheese']['view_in_file']['main'][ab_square_layer] = False
    a_gds.options['no_cheese']['view_in_file']['main'][ab_square_layer] = True
    a_gds.options['cheese']['view_in_file']['main'][1] = True
    a_gds.options['no_cheese']['view_in_file']['main'][1] = True

    a_gds.export_to_gds(name)