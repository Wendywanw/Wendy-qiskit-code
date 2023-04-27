import pandas as pd
import numpy as np
import astropy.units as u
from collections import OrderedDict

from qiskit_metal import Dict
from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight
from qiskit_metal.qlibrary.tlines.mixed_path import RouteMixed
from qiskit_metal.qlibrary.tlines.anchored_path import RouteAnchors
from qiskit_metal.qlibrary.couplers.coupled_line_tee import CoupledLineTee

import sys
sys.path.append('/Users/wendy/Desktop/Wendy-qiskit-code/Customized_Components')
from rounded_single_pad import Round_TransmonPocket_Single as transmon
import Transmon_property as trans_p
import Transmon_specifications as jj
from dolan_junction import DolanJunction as junction
import Default_params as dp
from Airbridge import airbridges as ab
from short_line_Segment import ShortRoute as short_path


class TransmonPocket():
    default_options = dict(
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
        ab_distance = '70um',
        rotation = 0
        )
    '''Default options for the transmon pocket.'''
    def __init__(self,
                gui,
                 design: 'QDesign',
                 eig_all = '', 
                 sim:bool = False,
                 options: Dict = default_options,):
        self.gui = gui
        self.design = design
        self.options = options
        self.eig_all = eig_all
        self.sim = sim
        self.make_qubit_from_scratch()#design, gui, eig_all, sim)
        self.connection_cpws = []
        self.connection_ab = []

    

    def make_qubit_from_scratch(self):
        design = self.design
        gui = self.gui 
        eig_all = self.eig_all
        sim = self.sim
        p = self.options
        rotation = p['rotation']
        rot_angle = np.radians(rotation)
            # q,j, TQ, freq, gui, design, 
        # print(p)
        guess_all = pd.read_csv(p['guess_path'])
        guesses = dp.slice_data(guess_all, p['frequency'])
        size = guesses['Sizes (um)']*u.um
        buffer = guesses['Buffers (um)']*u.um
        offset = guesses['Offsets (mm)']
        coupling_len = guesses['Coupling_len(um)']*u.um
        coupling_gap = guesses['Coupling_gap(um)']*u.um
        Lj = guesses['Ljs']
        Cj = jj.find_junction_capacitance(int(Lj[:-2])*u.nH)

        c_gap = guesses['Coupling_gap_feedline(um)']
        
        Cj1 = str(Cj.to(u.fF).value)+' fF'
        size = size.to(u.um)

        TQx = guesses['TQx']
        TQy = guesses['TQy']
        TQ_mir = guesses['TQ_mir']
        small = guesses['Small']

        feedline_coupling_space = 0.002#guesses['Coupling_gap_feedline(um)']
        components = self.design.components
        delete = []
        for component in components:
            if (p['coord']) in component:
                delete.append(component)
        for names in delete:
            design.delete_component(names)
        # #start making the components
        cpw_name = 'cpw_'+ p['coord']
        # design.delete_component(cpw_name)

        #make the qubit
        gap = 30*u.um
        size = size.to(u.um)
        pocket_width = (size+2*gap).to(u.um)
        
        x = design.parse_value(p['pos_x'])
        y = design.parse_value(p['pos_y'])

        y_dis = design.parse_value(TQy)

        x -= np.sin(rot_angle)*y_dis
        y -= np.cos(rot_angle)*y_dis
        qb_options = Dict(pos_x = str(x),
                        pos_y = str(y),
                        orientation = -rotation,
                        pad_height = '{}'.format(size), 
                        pad_width = '{}'.format(size), 
                        pocket_width = '{}'.format(pocket_width), 
                        hfss_inductance = Lj,
                        q3d_inductance =  Lj,
                        hfss_capacitance = Cj,
                        q3d_capacitance =  Cj,
                        layer = p['qubit_layer'],
                        junction = 'True',
                        **dp.qb_options)
        q = transmon(design,'qubit'+p['coord'],options = qb_options)
        q.options['connection_pads']['a']['pad_width'] = '{}'.format(coupling_len)
        q.options['connection_pads']['a']['pad_height'] = '30um-{}'.format(coupling_gap)
        q.options['connection_pads']['a']['pad_gap'] = '{}'.format(coupling_gap)
        # gui.rebuild()

        self.qubit = q

        #make the junction
        x_pos  = q.options.pos_x
        y_pos = q.options.pos_y
        jj_options = Dict(pos_x = str(x_pos), 
                        pos_y = str(y_pos), 
                        orientation = -rotation,
                        taper_len='0.5um',
                        jj_gap = '0.14um',
                        Lj = Lj[:-2], 
                        layer = p['junction_layer'])
        # print(jj_options,'a')
                        
        j = junction(design, 'jj'+p['coord'], options = jj_options)
        y_pos = (q.options.pad_height) + '/2' + '+' + (q.options.jj_length) +'-'+ (j.options.total_length)+'/4'#+'+'+q.options.pos_y
        parsed_ypos= design.parse_value(y_pos)
        parsed_diff = design.parse_value(q.options.pos_y)
        # if rotation==0:
        #     j.options.pos_y = str(-parsed_ypos+parsed_diff)
        # else:
        x = design.parse_value(q.options.pos_x)
        y = design.parse_value(q.options.pos_y)
        # print(x,y)
        x += np.sin(rot_angle)*(-parsed_ypos)
        y += np.cos(rot_angle)*(-parsed_ypos)
        # print(x,y)
        j.options.pos_y = y
        j.options.pos_x = x
        # # j.options.pos_y = y_pos
        # # j.options.pos_x = x_pos
        
        # # j.options.layer = p.junction_layer
        # gui.rebuild()
        self.junction = j


        l_name = 'Lj'+ p['coord']
        c_name = 'Cj'+ p['coord']

        if sim:
            eig_all.sim.renderer.options[l_name] = Lj
            eig_all.sim.renderer.options[c_name] = Cj
            eig_all.sim.setup.vars = {l_name:Lj, c_name:Cj}

        #make the coupled_line_tee
        dp.TQ_options['down_length'] = '40 um'
        dp.TQ_options['coupling_space'] = '{}um'.format(c_gap)
        tqx = design.parse_value(TQx)
        tqy= design.parse_value(TQy)
        qb_x= design.parse_value(q.options.pos_x)
        qb_y = design.parse_value(q.options.pos_y)

        tq_x = qb_x + np.cos(rot_angle)*tqx+np.sin(rot_angle)*tqy
        tq_y = design.parse_value(p['pos_y'])-tqx*np.sin(rot_angle)


        TQ1 = CoupledLineTee(design, 'TQ'+p['coord'], options=dict(pos_x=str(tq_x),
                                                    pos_y=str(tq_y),
                                                    mirror = TQ_mir,
                                                    layer = p['qubit_layer'], 
                                                    orientation = -rotation,
                                                    **dp.TQ_options))
        # gui.rebuild()
        # print(TQ1.pins['second_end'], 'pin')
        self.Tee = TQ1

        #make the cpw
        gap1 = 0.056
        anchors = trans_p.anchor_CPW_round(q, buffer, gap1, 2, small = small, last_offset = offset)
        anchor_new = OrderedDict()
        for ind in anchors:
            x,y = anchors[ind]
            x-= qb_x
            y -= qb_y
            x_new = np.cos(rot_angle)*x + np.sin(rot_angle)*y
            y_new = np.cos(rot_angle)*y - np.sin(rot_angle)*x

            x_new += qb_x
            y_new += qb_y

            anchor_new[ind] = (x_new, y_new)
        anchors = anchor_new
        # print(anchors)
        # print('aa')
        design.delete_component(cpw_name)
        
        pin_inputs = Dict(
                    start_pin=Dict(component=q.name, pin='a'),
                    end_pin=Dict(component=TQ1.name, pin='second_end'))
        
        dp.CPW_options['pin_inputs'] = pin_inputs
        dp.CPW_options['layer'] = p['qubit_layer']
        # print(anchors)
        # print(dp.CPW_options)
        # print(dp.CPW_options)
        # try:
        # cpw = dp.RouteMixed(design, 'cpw_'+p['coord'], options = Dict(anchors = anchors, **dp.CPW_options))
        cpw = RouteAnchors(design, 'cpw_'+p['coord'], options = Dict(anchors = anchors, **dp.CPW_options))

    # except:
    #     design.delete_component('cpw_'+p['coord'])
    #     print('there is a cpw building error')
        # print(anchors, dp.CPW_options)
        
    # else:
        # gui.rebuild()
        self.resonator = cpw

        ab_options = Dict(cpw_name = cpw.name, distance = p['ab_distance'], dis = '50um', layer_ab_square = str(p['ab_square_layer']), layer_ab = str(p['ab_layer']), total_length = '80 um', chip = 'main', seg_num = '0')
        airb = ab(design, 'airbridges' + p['coord'], ab_options)
        
        # gui.rebuild()
        self.airbridge = airb

        # self.qubit = q
        # self.junction = j
        # self.resonator = cpw
        # self.Tee = TQ1
        # self.airbridge = airb

        # return q,j,cpw, TQ, design,gui, airb
    def connect(self,component, buffer = 0):
        
        design = self.design
        x = design.parse_value(self.Tee.options.pos_x)
        y = design.parse_value(self.Tee.options.pos_y)
        anchor = OrderedDict()

        dp.trans_options['layer'] = self.options['qubit_layer']
        ys = [3.8,3.65,2.70000,1.750000,0.8000,
            -0.150000,-1.10000,-2.050000,-3.0000,-3.950000]

        if 'pocket' in str(type(component)):
            name = component.qubit.name[5:]
            self_name = self.qubit.name[5:]
            flag = False
            x_com = design.parse_value(component.Tee.options.pos_x)
            y_com = design.parse_value(component.Tee.options.pos_y)
            if x<x_com:
                start_name = self.Tee.name
                pin_start = 'prime_end'
                end_name = component.Tee.name
                pin_end = 'prime_start'
            elif self.qubit.options['orientation'] == -180:
                if x>=x_com:
                    start_name = self.Tee.name
                    pin_start = 'prime_end'
                    end_name = component.Tee.name
                    pin_end = 'prime_start'
                else:
                    start_name = self.Tee.name
                    pin_start = 'prime_end'
                    end_name = component.Tee.name
                    pin_end = 'prime_start'
            else:
                start_name = self.Tee.name
                pin_start = 'prime_start'
                end_name = component.Tee.name
                pin_end = 'prime_end'

            if (self.qubit.options['orientation'] == -180)& (x<=-2.7):
                pin_start = 'prime_end'
                pin_end = 'prime_end'
                start_name = self.Tee.name
                end_name = component.Tee.name
                anchor[0] = (x_com,y)
                flag = True
            elif (self.qubit.options['orientation'] == -270) & (x>=3):
                print('oops')
                pin_start = 'prime_start'
                pin_end = 'prime_start'
                start_name = self.Tee.name
                end_name = component.Tee.name
                anchor[0] = (x,y_com)
                flag = True
            pin_inputs = Dict(
                start_pin=Dict(component=start_name, pin=pin_start),
                end_pin=Dict(component=end_name, pin=pin_end))
            dp.trans_options['pin_inputs'] = pin_inputs
            if flag:
                cpw = RouteMixed(self.design, self_name + 'CPW'+ name,
                            options = Dict(anchors = anchor, **dp.trans_options))
            else:
                cpw = short_path(self.design, self_name + 'CPW'+ name,
                            options = dp.trans_options)
        elif 'pad' in str(type(component)):
            self_name = self.qubit.name[5:]
            
            x_com = design.parse_value(component.options.pos_x)
            # print(component.name)
            y_com = design.parse_value(component.options.pos_y)
            
            name = component.name
            ind = int(name[-1])
            
            if (y>=4.1 and x <-2):
                start_name = component.name
                pin_start= 'tie'
                end_name = self.Tee.name
                pin_end = 'prime_start'
                anchor[0] = (-3.9, 4.75)
                # anchor[1] = (-3.65, 4.5)
            elif (y>=3.9 and x >2):
                start_name = component.name
                pin_start= 'tie'
                end_name = self.Tee.name
                pin_end = 'prime_end'
                anchor[0] = (3.9, 4.75)
            elif x<x_com:
                # print('1')
                anchor[0] = (x_com-0.05-buffer,ys[ind])
                # anchor[1] = (x_com-0.075+buffer,ys[ind])
                end_name = self.Tee.name
                pin_end = 'prime_end'
                start_name = component.name
                pin_start = 'tie'
            else:
                # print('2')
                anchor[0] = (x_com+0.05+buffer,ys[ind])
                # anchor[1] = (x_com+0.075+buffer,ys[ind])
                end_name = self.Tee.name
                pin_end = 'prime_start'
                start_name = component.name
                pin_start = 'tie'
            pin_inputs = Dict(
                    start_pin=Dict(component=start_name, pin=pin_start),
                    end_pin=Dict(component=end_name, pin=pin_end))
            dp.trans_options['pin_inputs'] = pin_inputs
            ops = Dict(anchors = anchor, **dp.trans_options)
            if np.absolute(y-y_com)<0.06:
                # dp.trans_options['fillet'] = str(np.absolute(x-x_com)/2)
                anchor = OrderedDict()
                anchor[0] = (x_com-(buffer+0.05)*np.sign(x_com),np.sign(y)*(max(np.absolute(y_com),np.absolute(y))-0.14))
                anchor[1] = (x_com-(buffer+0.13)*np.sign(x_com),ys[ind])
                print('short_segment!', anchor)
            dp.trans_options['fillet'] = '30um'
            # print(anchor, x_com)
            cpw = RouteMixed(self.design, self_name + 'CPW'+ name,
                            options = Dict(anchors = anchor, **dp.trans_options))
        
        self.connection_cpws.append(cpw)
        # self.gui.rebuild()

        ab_options = Dict(cpw_name = cpw.name, 
                          distance = self.options['ab_distance'], 
                          dis = '0um', 
                          layer_ab_square = str(self.options['ab_square_layer']), 
                          layer_ab = str(self.options['ab_layer']), 
                          total_length = '80 um', 
                          chip = 'main', 
                          seg_num = '0')
        airb = ab(self.design, 'airbridge_connects' + self.options['coord'] + name, ab_options)
        self.connection_ab.append(airb)
        # self.gui.rebuild()
        


