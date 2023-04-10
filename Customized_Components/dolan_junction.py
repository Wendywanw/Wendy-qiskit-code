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
    """A rrectangle with rounded corners.

    Inherits QComponent class.

    # 
                 +1                            +1
                ________________________________
            -1  |______ ____           __________|   +1     Y
                |      |____|         |____|     |          ^
                |        __________________      |          |
                |       |     island       |     |          |----->  X
                |       |__________________|     |
                |                 |              |
                |  pocket         x              |
            -1  |_________________|______________|   +1
                 
                 -1                            -1

    # .. meta::
    #     Circle Raster

    Default Options:
        * chip = 'main',
        * pos_x: '0um'
        * pos_y: '0um' 
        * pad_width: '20 um'
        * pad_height: '30 um'
        * total_length: '80 um'
        * Lj: '10 nH'
        * resolution: '5'
        * Fillet: '5 um'
        * fat_finger_width: '6 um'
        * Jc: '0.1' 
        * rotation: '0'
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
        fillet = '5 um',
        fat_finger_width = '6 um',
        thin_finger_len = '1.36um',
        taper_len = '0.5um',
        Jc = '0.1',
        rotation = '0',
        layer = '0')
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

        pad = rec(pad_width, pad_height, fillet, resolution)
        pad_top = draw.translate(pad, 0, +total_height/2.-pad_height/2.)
        pad_bot = draw.translate(pad, 0, -(total_height/2.-pad_height/2.))

        fat_finger = rec2(fat_finger_width, fat_finger_len)
        finger_top = draw.translate(fat_finger, 0,fat_finger_len/2.+l/2)
        finger_bot = draw.translate(fat_finger, 0,-fat_finger_len/2.-l/2)

        

        thin_finger_width = (jj.find_junction_area(Lj, Jc)/(p.jj_gap_actual*u.mm)).to(u.mm).value
        thin_finger = rec2(thin_finger_width, p.thin_finger_len)
        d = -(l - p.thin_finger_len)/2+jj_gap
        thin_finger = draw.translate(thin_finger, 0, d)

        h = total_height/2-pad_height-fat_finger_len+l/2
        taper = draw.Polygon([(-fat_finger_width/2,h/2),
                              (fat_finger_width/2,h/2),
                              (thin_finger_width/2, d+p.thin_finger_len/2),
                              (-thin_finger_width/2, d+p.thin_finger_len/2)])

        top = draw.shapely.ops.unary_union([pad_top, finger_top, thin_finger, taper])
        bot = draw.shapely.ops.unary_union([pad_bot, finger_bot])

        components = [top, bot]
        components = draw.rotate(components, p.rotation, origin=(0, 0))
        components = draw.translate(components, p.pos_x, p.pos_y)
        top, bot = components
        
        
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(top_j=top),
                           chip=chip, layer = p.layer)
        self.add_qgeometry('poly',
                           dict(bot_j=bot),
                           chip=chip, layer = p.layer)
        # self.add_qgeometry('poly', dict(sub = rec2(p.pad_width, p.total_length)), 
        #                    subtract=True, 
        #                    chip=chip)