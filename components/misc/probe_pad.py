

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

import numpy as np
import astropy.units as u
from qiskit_metal import draw, Dict
from qiskit_metal.qlibrary.core import QComponent

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'analysis'))

from components.misc import rec2




class ProbePad(QComponent):
    """A dose array coponent 

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
        w_pocket = '350 um',
        h_pocket = '200 um',
        w_pad = '150 um',
        h_pad = '100 um',
        pad_gap = '7 um',
        orientation = '0',
        layer = '0',
        )
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

        # since we will reuse these options, parse them once and define them as varaibles
        w_pocket = p.w_pocket
        h_pocket = p.h_pocket
        w_pad = p.w_pad
        h_pad = p.h_pad
        pad_gap = p.pad_gap

        pocket = rec2(w_pocket, h_pocket)
        pad = rec2(w_pad, h_pad)

        pad_left = draw.translate(pad, -w_pad/2-pad_gap/2, 0)
        pad_right = draw.translate(pad, w_pad/2 + pad_gap/2, 0)

        all = draw.union(pad_left, pad_right)
        cut = pocket

        components = draw.rotate([all,cut], p.orientation, origin=(0,0))
        all, cut = draw.translate(components, p.pos_x, p.pos_y)

        
        
        # Use the geometry to create Metal qgeometry
        self.add_qgeometry('poly',
                           dict(all=all),
                           chip=chip, layer = p.layer)

        self.add_qgeometry('poly', dict(cut = cut), 
                           subtract=True, layer=p.layer,
                           chip=chip)
