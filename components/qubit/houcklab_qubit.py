

# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import sys

import numpy as np
from qiskit_metal import Dict, draw
from qiskit_metal.qlibrary.core import BaseQubit
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'analysis'))
from analysis import Transmon_specifications as jj
from components.misc import rec2
from components.misc import rec


class DiffTransmonRounded(BaseQubit):  # pylint: disable=invalid-name
    """The base `DiffTransmonRounded` class.

    Inherits `BaseQubit` class.

    Simple Metal Transmon Cross object. Creates the X cross-shaped island,
    the "junction" on the south end, and up to 3 connectors on the remaining arms
    (claw or gap).

    'claw_width' and 'claw_gap' define the width/gap of the CPW line that
    makes up the connector. Note, DC SQUID currently represented by single
    inductance sheet

    Add connectors to it using the `connection_pads` dictionary. See BaseQubit for more
    information.

    Sketch:
        Below is a sketch of the qubit
        ::

                                        claw_length
            Claw:       _________                    Gap:
                        |   ________________             _________    ____________
                  ______|  |                             _________|  |____________
                        |  |________________
                        |_________


    .. image::
        transmon_cross.png

    .. meta::
        Transmon Cross

    BaseQubit Default Options:
        * connection_pads: Empty Dict -- The dictionary which contains all active connection lines for the qubit.
        * _default_connection_pads: empty Dict -- The default values for the (if any) connection lines of the qubit.

    Default Options:
        * cross_width: '20um' -- Width of the CPW center trace making up the Crossmon
        * cross_length: '200um' -- Length of one Crossmon arm (from center)
        * cross_gap: '20um' -- Width of the CPW gap making up the Crossmon
        * cross_radius: '8um' -- Radius of the corners of the Crossmon
        * _default_connection_pads: Dict
            * connector_type: '0' -- 0 = Claw type, 1 = gap type
            * claw_length: '30um' -- Length of the claw 'arms', measured from the connector center trace
            * ground_spacing: '5um' -- Amount of ground plane between the connector and Crossmon arm (minimum should be based on fabrication capabilities)
            * claw_width: '10um' -- The width of the CPW center trace making up the claw/gap connector
            * claw_gap: '6um' -- The gap of the CPW center trace making up the claw/gap connector
            * connector_location: '0' -- 0 => 'west' arm, 90 => 'north' arm, 180 => 'east' arm
    """

    default_options = Dict(
        cut_l='1000um',
        cut_h='1200um',
        gap='15um',
        jj_gap='2um',
        jj_contact_size='5um',
        w = '120um',
        l = '600um',
        r = '60um',
        cpw_l = '50um',
        coupling_gap = '30um',
        JJ_cutout_w = '70um',
        JJ_cutout_h = '70um',
        JJ_cutout_r = '15um',
        JJ_c_contact_l = '40um',
        JJ_c_contact_r = '2.5um',
        JJ_c_contact_w = '10um',
        JJ_c_contact_shortl = '10um',
        coupling_d = '350um',
        coupling_pad_w = '120um',
        coupling_stub_w = '50um',
        coupling_r = '15um',
        cpw_pin = '5um',
        chip='main',
        resolution = '10',
        junction = 'False',
        orientation = '0',
        istunnel = 'True', 
        junction_taper_r = '10um',)
    """Default options."""

    component_metadata = Dict(short_name='DiffRound',
                              _qgeometry_table_poly='True',
                              _qgeometry_table_junction='True')
    """Component metadata"""

    TOOLTIP = """Simple Rounded Differnetial Transmon"""

    ##############################################MAKE######################################################


    def make(self):
        """Makes a basic Differential Rounded Transmon"""

        # self.p allows us to directly access parsed values (string -> numbers) form the user option
        p = self.p

        cut_l = p.cut_l
        cut_h = p.cut_h
        gap = p.gap
        w = p.w
        r = min(p.r,w/2)
        l = p.l
        cpw_l = p.cpw_l
        coupling_gap = p.coupling_gap
        JJ_cutout_w = p.JJ_cutout_w
        JJ_cutout_h = p.JJ_cutout_h
        JJ_cutout_r = p.JJ_cutout_r
        JJ_c_contact_l = p.JJ_c_contact_l
        JJ_c_contact_r = p.JJ_c_contact_r
        JJ_c_contact_w = p.JJ_c_contact_w
        coupling_d = p.coupling_d
        coupling_pad_w = p.coupling_pad_w
        resolution = p.resolution
        coupling_stub_w = p.coupling_stub_w
        coupling_r = min(coupling_pad_w/2,p.coupling_r, coupling_d/2)
        coupling_r_stub = min(coupling_stub_w/2,p.coupling_r)
        JJ_c_contact_shortl = p.JJ_c_contact_shortl
        istunnel = p.istunnel
        
        right_pad_location = cpw_l+coupling_d+coupling_gap+w/2*3+gap
        left_pad_location = cpw_l+coupling_d+coupling_gap+w/2
        
        coupling_stub_x = cpw_l+(coupling_d+coupling_gap)/2
        coupling_stub_y = w+coupling_gap
        
        coupling_r_stub = min((l - 2*r)/2 - coupling_stub_y - coupling_stub_w/2, coupling_r_stub)

        # access to chip name
        chip = p.chip

        # Creates the cross and the etch equivalent.
        # cross_line = draw.shapely.ops.unary_union([
        #     draw.LineString([(0, cross_length), (0, -cross_length)]),
        #     draw.LineString([(cross_length, 0), (-cross_length, 0)])
        # ])

        # cross = cross_line.buffer(cross_width / 2, cap_style=2)
        # cross_etch = cross.buffer(cross_gap, cap_style=3, join_style=2)

        cutout_pad = rec(cut_l, cut_h,  r, resolution = resolution)
        cutout_pad = draw.translate(cutout_pad, cut_l/2, 0)
        
        pad = rec(w,l,  r, resolution = resolution)
        

        junction_location = cpw_l+coupling_d+coupling_gap+w+gap/2
        
        JJ_cutouthalf_w = JJ_cutout_w/2-gap/2
        JJ_cutout_r = min(JJ_cutout_r, JJ_cutouthalf_w/2)
        
        JJ_cutout = rec2(JJ_cutouthalf_w, 
                         JJ_cutout_h, 
                         r = JJ_cutout_r, 
                         same_radius = True,  
                         resolution = resolution,
                         d1 = [-1,1],
                         d4 = [-1,-1])
        JJ_cutout_right = draw.translate(JJ_cutout,
                                        junction_location+gap/2+JJ_cutouthalf_w/2, 
                                        0)
        JJ_cutout_left = draw.rotate(JJ_cutout, 180, origin = (0,0))
        JJ_cutout_left = draw.translate(JJ_cutout_left, 
                                         junction_location-gap/2-JJ_cutouthalf_w/2, 
                                         0)
        JJ_cutouts = draw.union([JJ_cutout_left, JJ_cutout_right])
        
        
        
        jj_contact1 = rec(JJ_c_contact_w,JJ_c_contact_l,JJ_c_contact_r, resolution = resolution)
        JJ_contact1 = draw.translate(jj_contact1, -JJ_c_contact_w, 0)
        jj_contact2 = rec2(JJ_c_contact_shortl,
                           JJ_c_contact_w,
                           r = JJ_c_contact_r,
                           same_radius = True, 
                           resolution = resolution,
                           d1 = [-1,1], 
                           d2 = [1,1],
                           d3 = [1,-1],
                           d4 = [-1,-1])
        JJ_contact = draw.union([JJ_contact1, jj_contact2])
        
        JJ_contact_left = draw.translate(JJ_contact, junction_location-gap/2-JJ_c_contact_w/2-JJ_cutouthalf_w, 0)
        JJ_contact_right = draw.rotate(JJ_contact, 180, origin = (0,0))
        JJ_contact_right = draw.translate(JJ_contact_right, junction_location+gap/2+JJ_c_contact_w/2+JJ_cutouthalf_w, 0)
        
        
        # 
        JJ_cutouts1 = draw.union([JJ_contact_left, JJ_contact_right])
        # if p.junction
        JJ_cutouts = draw.union([JJ_cutouts, JJ_cutouts1])
        
        
        pad_right = draw.translate(pad, right_pad_location, 0)
        pad_left = draw.translate(pad, left_pad_location, 0)
        
        
        
        angle = p.orientation
        cos = np.cos(np.radians(angle))
        sin = np.sin(np.radians(angle))
        
        coupling_stub_x = cpw_l+(coupling_d+coupling_gap)/2
        coupling_stub_y = coupling_stub_w/2+coupling_pad_w/2+coupling_gap
        
        # coupling_stub = rec(w,coupling_d+coupling_gap-w, coupling_r, resolution = resolution,connection = True,connection_direction = 270)
        # coupling_stub = draw.translate(coupling_stub,w/2 , 0)
        # sub_rounded = rec(w*2,w,r, resolution = resolution)
        # sub_rounded = draw.translate(sub_rounded, -coupling_d/2+w, 0)
        
        # coupling_stub = draw.union([coupling_stub, sub_rounded])
        if p.coupling_arm == 'False':
            pass
        else:
            coupling_stub_top = rec2(coupling_d+coupling_gap, 
                                coupling_stub_w,
                            same_radius = False,  
                            r1 = coupling_r_stub,
                            r2 = coupling_r_stub,
                            r3 = coupling_r_stub,
                            r4 = coupling_r,
                            resolution = resolution,
                            d1 = [-1,1],
                            d2 = [1,-1],
                            d3 = [1,1],
                            d4 = [-1,-1]
                            )
            
            coupling_stub_bot = rec2(coupling_d+coupling_gap, 
                                coupling_stub_w,
                            same_radius = False,  
                            r1 = coupling_r,
                            r2 = coupling_r_stub,
                            r3 = coupling_r_stub,
                            r4 = coupling_r_stub,
                            resolution = resolution,
                            d1 = [-1,1],
                            d2 = [1,-1],
                            d3 = [1,1],
                            d4 = [-1,-1]
                            )
            
            coupling_stub_top = draw.rotate(coupling_stub_top, 180, origin = (0,0))
            coupling_stub_bot = draw.rotate(coupling_stub_bot, 180, origin = (0,0))

            
            coupling_stub_top = draw.translate(coupling_stub_top, coupling_stub_x+1e-9, coupling_stub_y)
            coupling_stub_bot = draw.translate(coupling_stub_bot, coupling_stub_x+1e-9, -coupling_stub_y)
            
        coupling_pad_r = min(r, coupling_pad_w/2, coupling_d/2)
        self.options.coupling_pad_r = coupling_pad_r
        coupling_pad = rec(coupling_d,coupling_pad_w,  coupling_pad_r, resolution = resolution)
        
        coupling_pad = draw.translate(coupling_pad, cpw_l+coupling_d/2, 0)
        
        # cpw_stub = rec(cpw_l*2,p.cpw_pin,0, resolution = 1)
        
        cpw_taper_r = np.absolute(min(cpw_l/2, 
                                      (coupling_pad_w-coupling_pad_r*2-p.cpw_pin)/2))
        
        cpw_stub = rec2(cpw_l,
                            p.cpw_pin,
                            same_radius = False,
                            r1 = cpw_taper_r,
                            r2 = 0,
                            r3 = 0,
                            r4 = cpw_taper_r,
                            resolution = int(p.junction_taper_r/0.002),
                            d1 = [-1,1],
                            d2 = [1,-1],
                            d3 = [1,1],
                            d4 = [-1,-1]
                            )
        cpw_stub = draw.rotate(cpw_stub, 180, origin = (0,0))
        cpw_stub = draw.translate(cpw_stub, cpw_l/2, 0)
        
        
        ## add taper to reduce junction length
        jj_gap = p.jj_gap
        jj_contact_size = p.jj_contact_size
        taper_r = p.jj_taper_r
        jj_contact_width = (gap-jj_gap)/2
        taper = rec2(jj_contact_width, 
                     jj_contact_size, 
                     same_radius = False,  
                     r1 = taper_r,
                     r2 = 0,
                     r3 = 0,
                     r4 = taper_r,
                     resolution = int(taper_r/0.002),
                     d1 = [-1,1],
                     d2 = [1,-1],
                     d3 = [1,1],
                     d4 = [-1,-1]
                     )
        taper_left = draw.translate(taper, junction_location-gap/2+jj_contact_width/2, 0)
        taper_right = draw.rotate(taper, 180, origin = (0,0))
        taper_right = draw.translate(taper_right, junction_location+gap/2-jj_contact_width/2, 0)

        # #rotate and translate
        connector_pad = draw.union([coupling_pad, cpw_stub, taper_left, taper_right])
        if p.coupling_arm == 'False':
            pass
        else:
            pad_left = draw.union([pad_left, coupling_stub_top, coupling_stub_bot])
        
        # poly_metal = draw.union([pad_right, pad_left, coupling_stub_top, coupling_stub_bot, coupling_pad, cpw_stub])
        if istunnel == 'True':
            pad_left = pad_left.difference(JJ_cutouts)
            pad_right = pad_right.difference(JJ_cutouts)
        else:
            pass
        jj_x, jj_y = self.get_jj_location0()
        rect_jj = draw.LineString([(jj_x-jj_gap/2, +jj_y), 
                                   (jj_x+jj_gap/2, jj_y)])
        polys = [pad_right, pad_left, connector_pad, rect_jj, cutout_pad]
        polys = draw.rotate(polys, p.orientation, origin=(0, 0))
        polys = draw.translate(polys, p.pos_x, p.pos_y)
        
        
        
        cpw_pin_start = [p.pos_x + cos*cpw_l,p.pos_y+sin*cpw_l]
        cpw_pin_end = [p.pos_x,p.pos_y]
        
        self.add_pin('cpw_stub', 
                     [cpw_pin_start,cpw_pin_end], 
                     width = p.cpw_pin,
                     input_as_norm=True,)
        # [center_metal, center_metal_top, center_metal_bot, center_metal_etch, center_metal_top_etch, center_metal_bot_etch, rect_jj] = polys

        # generate qgeometry
        self.add_qgeometry('poly', 
                           dict(pad_left=polys[1], pad_right = polys[0],resonator_pad = polys[2],), 
                           chip=chip)
        self.add_qgeometry('poly', 
                           dict(center_metal_etch=polys[4]), 
                           chip=chip, 
                           subtract=True)
        # print(p.junction)
        if p.junction == 'False' or p.junction == False:
            self.add_qgeometry('junction',
                           dict(rect_jj=polys[3]),
                           width=min(jj_contact_width,0.003),
                           chip=chip)
            # print('junction added')
        
        # self.add_qgeometry('poly',
        #                    dict(cross_etch=cross_etch),
        #                    subtract=True,
        #                    chip=chip)
        # if p.junction == 'False':
        #     self.add_qgeometry('junction',
        #                    dict(rect_jj=rect_jj),
        #                    width=cross_width,
        #                    chip=chip)
    def get_jj_location(self):
        p = self.p
        junction_displacement = p.cpw_l+p.coupling_d+p.coupling_gap+p.w+p.gap/2
        junction_loc_x = junction_displacement*np.cos(np.radians(p.orientation))+p.pos_x
        junction_loc_y = junction_displacement*np.sin(np.radians(p.orientation))+p.pos_y
        return (junction_loc_x, junction_loc_y)
    
    def get_jj_location0(self):
        p = self.p
        junction_displacement = p.cpw_l+p.coupling_d+p.coupling_gap+p.w+p.gap/2
        jj_x = junction_displacement
        jj_y = 0
        return (jj_x, jj_y)

