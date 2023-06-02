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
"""Transmon Pocket.

.. code-block::
     ________________________________
    |______ ____           __________|
    |      |____|         |____|     |
    |        __________________      |
    |       |                  |     |
    |       |__________________|     |
    |                 |              |
    |                 x              |
    |_________________|______________|
"""

import numpy as np
import astropy.units as u
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import QComponent

import sys
sys.path.append('/Users/wendy/Desktop/Wendy-qiskit-code/Customized_Components')
from rounded_rectangle import rounded_rec_only as rec
from rounded_rectangle import rounded_rec as rec2
import Transmon_specifications as jj



class DolanJunction(QComponent):
    """A dolan junction that complies with the Lincoln lab design rules.

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
        pad_width = '20 um',
        pad_height = '30 um',
        total_length = '80 um',
        jj_gap = '0.14um',
        jj_gap_actual = '0.2um',
        Lj = '10',
        resolution = '5',
        fillet = '3 um',
        fat_finger_width = '6 um',
        thin_finger_len = '1.36um',
        taper_len = '0.5um',
        Jc = '0.1',
        rotation = '0',
        layer = '0',
        area_layer = '1',
        area_layer_opt = 'False',
        jj_orientation = '180')
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
        # pos_x = '0um',
        # pos_y = '0um',
        # pad_width = '20 um',
        # pad_height = '30 um',
        # total_length = '80 um',
        # jj_gap = '0.2um',
        # Lj = '10',
        # resolution = '5',
        # fillet = '5 um',
        # fat_finger_width = '6 um',
        # Jc = '0.1',
        # rotation = '0'
        # self.p allows us to directly access parsed values (string -> numbers) form the user option
        p = self.p

        # extract chip name
        chip = p.chip
        special_jj = (np.absolute((p.orientation - p.jj_orientation)%180) == 90)

        # since we will reuse these options, parse them once and define them as varaibles
        pad_width = p.pad_width
        pad_height = p.pad_height
        total_height = p.total_length
        taper_top = total_height/2 - pad_height
        taper_bot = taper_top-p.taper_len+p.jj_gap
        resolution = p.resolution
        Jc = p.Jc*u.uA/(u.um)**2
        Lj = p.Lj*u.nH
        jj_gap = p.jj_gap
        fillet = p.fillet
        l = p.taper_len+p.thin_finger_len+p.jj_gap
        fat_finger_width = p.fat_finger_width
        fat_finger_len = (total_height-pad_height*2-l)/2
        fat_finger_len0 = fat_finger_len

        if special_jj:
            fat_finger_len += fat_finger_width + (p.thin_finger_len+p.taper_len+p.jj_gap)

        pad = rec(pad_width, pad_height, fillet, resolution)
        pad_top = draw.translate(pad, 0, +total_height/2.-pad_height/2.)
        pad_bot = draw.translate(pad, 0, -(total_height/2.-pad_height/2.))
        if not special_jj:
            fat_finger = rec2(fat_finger_width, fat_finger_len)
            finger_top = draw.translate(fat_finger, 0,fat_finger_len0/2.+l/2)
            finger_bot = draw.translate(fat_finger, 0,-fat_finger_len0/2.-l/2)
        else:
            fat_fingerb = rec2(fat_finger_width-1e-3, fat_finger_len)
            fat_finger = rec2(fat_finger_width, fat_finger_len)
            finger_top = draw.translate(fat_finger, 0,fat_finger_len0/2.+l/2)
            finger_bot = draw.translate(fat_fingerb, 0,-fat_finger_len0/2.-l/2)
            translation = fat_finger_width/2 + (p.thin_finger_len+p.taper_len+p.jj_gap)/2
            finger_top = draw.translate(finger_top, -translation,0)
            finger_bot = draw.translate(finger_bot, translation,0)

        
        thin_len = p.thin_finger_len
        thin_finger_width = (jj.find_junction_area(Lj, Jc)/(p.jj_gap_actual*u.mm)).to(u.mm).value
        thin_finger = rec2(thin_finger_width, thin_len)
        thin_finger_long = rec2(thin_finger_width, thin_len+jj_gap*2)
        d = -(l - thin_len)/2+jj_gap
        thin_finger = draw.translate(thin_finger, 0, d)
        thin_finger_long = draw.translate(thin_finger_long, 0, d)

        h = total_height/2-pad_height-fat_finger_len0+l/2
        taper = draw.Polygon([(-fat_finger_width/2,h/2+1e-3),
                              (fat_finger_width/2,h/2+1e-3),
                                (fat_finger_width/2,h/2),
                              (thin_finger_width/2, d+thin_len/2),
                              (-thin_finger_width/2, d+thin_len/2),
                              (-fat_finger_width/2,h/2),])

        top = draw.shapely.ops.unary_union([pad_top, finger_top])
        finger = draw.shapely.ops.unary_union([thin_finger, taper])
        bot = draw.shapely.ops.unary_union([pad_bot, finger_bot])
        jj_poly = draw.shapely.ops.unary_union([thin_finger_long, taper])
        
        components = [top, bot, ]
        if p.orientation%180 != 0:
            components = draw.rotate(components, p.orientation, origin=(0, 0))
        components = draw.translate(components, p.pos_x, p.pos_y)
        if special_jj:
            components = draw.translate(components, -1e-3, 0)
            top, bot,  = components
            bot = draw.translate(bot, 1e-3/2, 0)
        else: 
            top, bot,  = components
        
        components = draw.rotate([finger,jj_poly], p.jj_orientation, origin = (0,0))
        finger, jj_poly = draw.translate(components, p.pos_x, p.pos_y)

        all = draw.shapely.ops.unary_union([top,finger, bot])
        
        
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(all=all),
                           chip=chip, layer = p.layer)
        # self.add_qgeometry('poly',
        #                    dict(bot_j=bot),
        #                    chip=chip, layer = p.layer)
        if p.area_layer_opt == 'True':
            self.add_qgeometry('poly',
                            dict(jj_poly=jj_poly),
                            chip=chip, layer = p.area_layer)
        # self.add_qgeometry('poly', dict(sub = rec2(p.pad_width, p.total_length)), 
        #                    subtract=True, 
        #                    chip=chip)