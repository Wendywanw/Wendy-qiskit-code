
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
"""Dolan Junction."""

import sys

import astropy.units as u
import numpy as np
from qiskit_metal import Dict, draw
from qiskit_metal.qlibrary.core import QComponent

sys.path.append('/Users/wendy/Desktop/Wendy-qiskit-code/Customized_Components')
import Transmon_specifications as jj
from rounded_rectangle import rounded_rec as rec2
from rounded_rectangle import rounded_rec_only as rec


class DolanJunctionBandage(QComponent):
    """A dolan junction that complies with the Lincoln lab design rules with bandage.

    Inherits QComponent class.

    # .. meta::
    #     Circle Raster

    Default Options:
        * chip = 'main'
        * pos_x: '0um' -- x position of the center
        * pos_y: '0um' -- y position of the center
        * pad_width: '20 um' -- width of the big pads that connect to the transmon
        * pad_height: '30 um' -- height of the big pads that connect to the transmon
        * total_length: '80 um' -- total length of the junction, including the pads
        * Lj: '10 nH' -- inductance of the junction
        * resolution: '5' -- number of points used to draw the rounded rectangle
        * Fillet: '5 um' -- radius of the fillet/rounded corners
        * fat_finger_width: '6 um' -- width of the fat finger, i.e. the part that tapers down to the junction finger
        * Jc: '0.1' -- critical current density of the junction
        * rotation: '0' -- rotation of the junction
        * layer: '0' -- layer of the junction
        * area_layer: '1' -- layer of the area that defines the junction
        * area: 'False' -- whether to draw the area that defines the junction
    """
    default_options = Dict(
        pos_x = '0um', 
        pos_y = '0um',
        w_pad_pin = '2 um',
        maximum_jj_width = '500nm',
        small_jj_length = '20nm',
        w_pad_u = '2.8 um',
        d_pin = '250 nm',
        d_u = '600 nm',
        total_length = '10 um',
        w_top_pin = '250 nm',
        w_top_u = '300 nm',
        w_bot_pin = '200 nm',
        w_bot_u = '300 nm',
        top_bot_offset = '0 nm' ,
        jj_extra = '400nm',
        jj_gap = '0.2um',
        fillet = '30 nm',
        uc_override_pad = '300nm', 
        bandage = 'False',
        bandage_h = '20um',
        bandage_w = '20um',
        bandage_layer = '299',
        bandage_uc_layer = '699',
        # jj_gap_actual = '0.2um',
        # Lj = '10',
        resolution = '5',
        # Jc = '0.1',
        orientation = '0',
        pin_layer = '0',
        gap_area_layer = '1',
        dimension_text = 'False',
        jj_orientation = '180',
        uc_override = '30nm',
        tapered = 'False',
        taper_r = '10um',
        bandage_loc = '0um',
        uc_override_band = '1um',)
    """Default drawing options"""

    component_metadata = Dict(short_name='Pocket',
                              _qgeometry_table_path='True',
                              _qgeometry_table_poly='True',
                              _qgeometry_table_junction='True')
    """Component metadata"""

    TOOLTIP = """A dolan junction"""

    def make(self):
        """Define the way the options are turned into QGeometry.

        The make function implements the logic that creates the geoemtry
        (poly, path, etc.) from the qcomponent.options dictionary of
        parameters, and the adds them to the design, using
        qcomponent.add_qgeometry(...), adding in extra needed
        information, such as layer, subtract, etc.
        """
        """Making the dolan junction."""
        p = self.p

        # extract chip name
        chip = p.chip
        special_jj = (np.absolute((p.orientation - p.jj_orientation)%180) == 90)

        # since we will reuse these options, parse them once and define them as varaibles
        w_pad_pin = p.w_pad_pin
        w_pad_u = p.w_pad_u
        d_pin = p.d_pin
        d_u = p.d_u

        w_top_pin = p.w_top_pin
        w_top_u = max(p.w_top_u,w_top_pin+2*p.uc_override)
        w_bot_pin = p.w_bot_pin
        w_bot_u = max(p.w_bot_u,w_bot_pin+2*p.uc_override)

        jj_extra = p.jj_extra

        top_bot_offset = p.top_bot_offset
        total_height = p.total_length
        small_jj_length = p.small_jj_length
        
        maximum_jj_width = p.maximum_jj_width
        
        
        
        
        jj_gap = p.jj_gap
        finger_length = total_height - jj_gap
        top_finger_len = max(finger_length/2-top_bot_offset + jj_extra-small_jj_length,0)
        bot_finger_len = max(finger_length/2+top_bot_offset + jj_extra-small_jj_length,0)

        resolution = p.resolution
        if p.tapered == 'True':
            taper_r = p.taper_r
            pad = rec2(w_pad_pin, 
                     d_pin, 
                     same_radius = False,  
                     r1 = 0,
                        r2 = 0,
                        r3 = taper_r,
                        r4 = taper_r,
                        resolution = int(taper_r/0.002),
                        d1 = [-1,-1],
                        d2 = [-1,1],
                        d3 = [-1,1],
                        d4 = [1,1]
                        )
            pad = draw.translate(pad, 0, taper_r/2)
            rectangle = rec2(w_pad_pin*10, d_pin*10,)
            rectangle = draw.translate(rectangle, 0, d_pin*10/2+d_pin)            
            pad_pin = pad.difference(rectangle)
            pad_u = draw.shapely.buffer(pad, p.uc_override_pad)
            pad_u = pad_u.difference(pad)
        else:
            pad_pin = rec2(w_pad_pin, d_pin,)
            pad_u = rec2(w_pad_u, d_u)

        top_pin = rec2(maximum_jj_width, top_finger_len)
        bot_pin = rec2(maximum_jj_width, bot_finger_len)

        finger_u = rec2(max(w_top_u,w_bot_u), total_height+jj_extra*2+p.uc_override_pad*2)
        
        if p.tapered == 'False':
            top_pad_pin = draw.translate(pad_pin, 0, total_height/2-d_pin/2)
            bot_pad_pin = draw.translate(pad_pin, 0, -total_height/2+d_pin/2)
        else:
            top = pad_pin
            bot = draw.rotate(pad_pin, 180, origin = (0,0))
            top_pad_pin = draw.translate(top, 0, total_height/2-d_pin)
            bot_pad_pin = draw.translate(bot, 0, -total_height/2+d_pin)
        
        b_w = p.bandage_w
        b_h = p.bandage_h
        dis = p.bandage_loc
        bandage_pad = rec2(b_w, b_h)
        bandage_pad_top = draw.translate(bandage_pad, 0, total_height/2+b_h/2-d_pin/4*3+dis)
        bandage_pad_bot = draw.translate(bandage_pad, 0, -total_height/2-b_h/2+d_pin/4*3-dis)
        bandage_pads = draw.shapely.ops.unary_union([bandage_pad_top, bandage_pad_bot])
        
        bandage_pad_uc = rec2(b_w+p.uc_override_band, b_h+p.uc_override_band)
        bandage_pad_uc = bandage_pad_uc.difference(bandage_pad)
        bandage_pad_top_uc = draw.translate(bandage_pad_uc, 0, total_height/2+b_h/2-d_pin/4*3+dis)
        bandage_pad_bot_uc = draw.translate(bandage_pad_uc, 0, -total_height/2-b_h/2+d_pin/4*3-dis)
        bandage_pads_uc = draw.shapely.ops.unary_union([bandage_pad_top_uc, bandage_pad_bot_uc])
        
        finger_top = rec2(w_top_pin, small_jj_length)
        finger_bot = rec2(w_bot_pin, small_jj_length, )
        
        # finger_top = rec2( small_jj_length,w_top_pin,)
        # finger_bot = rec2(w_bot_pin, small_jj_length, )
        
        
        finger_top = draw.translate(finger_top, 0, small_jj_length/2+jj_gap/2)
        finger_bot = draw.translate(finger_bot, 0, -small_jj_length/2-jj_gap/2)
        
        top_pad_u = draw.translate(pad_u, 0, total_height/2-d_pin/2)
        bot_pad_u = draw.translate(pad_u, 0, -total_height/2+d_pin/2)

        top_finger_pin = draw.translate(top_pin, 0, top_finger_len/2+jj_gap/2 + small_jj_length )
        bot_finger_pin = draw.translate(bot_pin, 0, -bot_finger_len/2-jj_gap/2-small_jj_length)

        metal_all = draw.shapely.ops.unary_union([top_pad_pin, bot_pad_pin, top_finger_pin, bot_finger_pin, finger_top, finger_bot])

        under_cut  = draw.shapely.ops.unary_union([top_pad_u, bot_pad_u,finger_u])

        cut = under_cut.difference(metal_all)
        
        components = draw.rotate([metal_all, cut, bandage_pads,bandage_pads_uc], p.orientation, origin = (0,0))
        all,cut, bandage_pads,bandage_pads_uc = draw.translate(components, p.pos_x, p.pos_y)
        
        # if p.dimension_text:
        #     pass
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(all=all),
                           chip=chip, layer = p.pin_layer)

        self.add_qgeometry('poly', dict(cut = cut), 
                           subtract=False, layer=p.gap_layer,
                           chip=chip)
        if p.bandage == True or p.bandage == 'True':
            self.add_qgeometry('poly', dict(bandage_pads = bandage_pads), 
                           subtract=False, layer=p.bandage_layer,
                           chip=chip)
            self.add_qgeometry('poly', dict(bandage_pads_uc = bandage_pads_uc),
                            subtract=False, layer=p.bandage_uc_layer,
                            chip=chip)