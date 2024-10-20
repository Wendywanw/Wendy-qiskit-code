
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
        uc_override_pad = '300nm',        # jj_gap_actual = '0.2um',
        # Lj = '10',
        resolution = '5',
        # Jc = '0.1',
        orientation = '0',
        pin_layer = '0',
        gap_area_layer = '1',
        dimension_text = 'False',
        jj_orientation = '180',
        uc_override = '30nm',)
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
        jj_gap = p.jj_gap
        finger_length = total_height - jj_gap
        top_finger_len = finger_length/2-top_bot_offset + jj_extra
        bot_finger_len = finger_length/2+top_bot_offset + jj_extra

        resolution = p.resolution

        pad_pin = rec2(w_pad_pin, d_pin,)
        pad_u = rec2(w_pad_u, d_u)

        top_pin = rec2(w_top_pin, top_finger_len)
        bot_pin = rec2(w_bot_pin, bot_finger_len)

        finger_u = rec2(max(w_top_u,w_bot_u), total_height+jj_extra*2+p.uc_override_pad*2)

        top_pad_pin = draw.translate(pad_pin, 0, total_height/2-d_pin/2)
        bot_pad_pin = draw.translate(pad_pin, 0, -total_height/2+d_pin/2)
        
        top_pad_u = draw.translate(pad_u, 0, total_height/2-d_pin/2)
        bot_pad_u = draw.translate(pad_u, 0, -total_height/2+d_pin/2)

        top_finger_pin = draw.translate(top_pin, 0, top_finger_len/2+jj_gap/2 )
        bot_finger_pin = draw.translate(bot_pin, 0, -bot_finger_len/2-jj_gap/2)

        metal_all = draw.shapely.ops.unary_union([top_pad_pin, bot_pad_pin, top_finger_pin, bot_finger_pin])

        under_cut  = draw.shapely.ops.unary_union([top_pad_u, bot_pad_u,finger_u])

        cut = under_cut.difference(metal_all)
        
        components = draw.rotate([metal_all, cut], p.orientation, origin = (0,0))
        all,cut = draw.translate(components, p.pos_x, p.pos_y)
        
        # if p.dimension_text:
        #     pass
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(all=all),
                           chip=chip, layer = p.pin_layer)

        self.add_qgeometry('poly', dict(cut = cut), 
                           subtract=False, layer=p.gap_layer,
                           chip=chip)